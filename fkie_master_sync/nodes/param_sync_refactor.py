#!/usr/bin/env python
# Original code from https://github.com/jhu-lcsr-forks/fkie_multimaster/tree/param-sync
# adapt to change only local ROS Parameter Server

import rospy

from fkie_master_discovery.common import masteruri_from_master
from fkie_multimaster_msgs.msg import MasterState

def master_changed(msg, cb_args):
    param_cache, local_master, __add_ns = cb_args


    if msg.master.uri != masteruri_from_master():
        master_to = rospy.MasterProxy(masteruri_from_master())
        master_from = rospy.MasterProxy(msg.master.uri)
        for name_param_master_from in master_from:
           param_into_master_to=master_to.search_param(name_param_master_from)
           if(param_into_master_to is None):
              rospy.logdebug(name_param_master_from)
              params_from = master_from[name_param_master_from]
              rospy.logdebug("Syncing params...")
	      master_to[name_param_master_from] = params_from

def main():
    rospy.init_node('param_sync', log_level=rospy.DEBUG)

    param_cache = dict()
    local_master = list()
    masteruri_from_master()

    __add_ns = rospy.get_param('~add_ns', True)
    sub = rospy.Subscriber('master_discovery/changes', MasterState, master_changed, callback_args=(param_cache, local_master, __add_ns))

    rospy.spin()

if __name__ == '__main__':
    main()

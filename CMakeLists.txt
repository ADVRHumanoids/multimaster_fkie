cmake_minimum_required(VERSION 3.0.2)
project(multimaster_fkie)

find_package(PythonInterp REQUIRED)

option(CREATE_PYTHON_VIRENV "Enable to create a virtual python" OFF)

if(${CREATE_PYTHON_VIRENV})
	# setup venv if it doesn't exist
	if (NOT EXISTS "${CMAKE_BINARY_DIR}/${PROJECT_NAME}_venv")
	    execute_process(COMMAND "${PYTHON_EXECUTABLE}" -m virtualenv --system-site-packages "${CMAKE_BINARY_DIR}/${PROJECT_NAME}_venv")
	    execute_process(COMMAND "${CMAKE_BINARY_DIR}/${PROJECT_NAME}_venv/bin/pip" install -r ${CMAKE_SOURCE_DIR}/requirements.txt)
	endif ()
	set(PYTHON_EXECUTABLE  "${CMAKE_BINARY_DIR}/${PROJECT_NAME}_venv/bin/python")
endif()

add_subdirectory(fkie_multimaster_msgs)
add_subdirectory(fkie_node_manager_daemon)
add_subdirectory(fkie_master_discovery)
add_subdirectory(fkie_master_sync)
add_subdirectory(fkie_node_manager)

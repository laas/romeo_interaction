# Copyright (C) 2008-2013 LAAS-CNRS
#
# Author: Maximilien Naveau
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Catkin part

CMAKE_MINIMUM_REQUIRED(VERSION 2.8.1)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/ros.cmake)
INCLUDE(cmake/GNUInstallDirs.cmake)
INCLUDE(cmake/python.cmake)


PROJECT(romeo_srv)

# Define properties of the project
SET(PROJECT_NAME romeo_srv)
SET(PROJECT_DESCRIPTION "romeo_srv ROS package to interact with HRP2")
SET(PROJECT_URL "")
SET(PROJECT_VERSION "1.0.0.0")


## Find rosbuild macros and libraries
## it will use the manifest to check the
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

SETUP_PROJECT()


set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

rosbuild_genmsg()
rosbuild_gensrv()
##rosbuild_add_boost_directories()



SETUP_PROJECT_FINALIZE()

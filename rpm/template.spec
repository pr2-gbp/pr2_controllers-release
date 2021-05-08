%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-pr2-head-action
Version:        1.10.18
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS pr2_head_action package

License:        BSD
URL:            http://ros.org/wiki/pr2_head_action
Source0:        %{name}-%{version}.tar.gz

Requires:       orocos-kdl
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-pr2-controllers-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-trajectory-msgs
BuildRequires:  orocos-kdl-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-pr2-controllers-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  ros-noetic-trajectory-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The PR2 head action is a node that provides an action interface for pointing the
head of the PR2. It passes trajectory goals to the controller, and reports
success when they have finished executing.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sat May 08 2021 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.18-1
- Autogenerated by Bloom


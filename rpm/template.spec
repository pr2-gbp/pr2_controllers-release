Name:           ros-melodic-pr2-gripper-action
Version:        1.10.15
Release:        1%{?dist}
Summary:        ROS pr2_gripper_action package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_gripper_action
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-pr2-controllers-msgs
Requires:       ros-melodic-pr2-mechanism-controllers
Requires:       ros-melodic-pr2-mechanism-model
Requires:       ros-melodic-robot-mechanism-controllers
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-pr2-controllers-msgs
BuildRequires:  ros-melodic-pr2-mechanism-controllers
BuildRequires:  ros-melodic-pr2-mechanism-model
BuildRequires:  ros-melodic-robot-mechanism-controllers
BuildRequires:  ros-melodic-roscpp

%description
The pr2_gripper_action provides an action interface for using the gripper. Users
can specify what position to move to (while limiting the force) and the action
will report success when the position is reached or failure when the gripper
cannot move any longer.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Sep 20 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.15-1
- Autogenerated by Bloom

* Thu Sep 20 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.15-0
- Autogenerated by Bloom


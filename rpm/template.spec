Name:           ros-melodic-robot-mechanism-controllers
Version:        1.10.16
Release:        1%{?dist}
Summary:        ROS robot_mechanism_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_mechanism_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       libtool
Requires:       libtool-ltdl-devel
Requires:       ros-melodic-actionlib
Requires:       ros-melodic-angles
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-control-toolbox
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-filters
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-message-filters
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-pr2-controller-interface
Requires:       ros-melodic-pr2-controller-manager
Requires:       ros-melodic-pr2-controllers-msgs
Requires:       ros-melodic-pr2-mechanism-model
Requires:       ros-melodic-realtime-tools
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf-conversions
Requires:       ros-melodic-trajectory-msgs
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-control-toolbox
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-filters
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-pr2-controller-interface
BuildRequires:  ros-melodic-pr2-controller-manager
BuildRequires:  ros-melodic-pr2-controllers-msgs
BuildRequires:  ros-melodic-pr2-mechanism-model
BuildRequires:  ros-melodic-realtime-tools
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf-conversions
BuildRequires:  ros-melodic-trajectory-msgs

%description
Generic Mechanism Controller Library

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
* Fri Jul 26 2019 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.16-1
- Autogenerated by Bloom

* Thu Sep 20 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.15-1
- Autogenerated by Bloom

* Thu Sep 20 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.10.15-0
- Autogenerated by Bloom


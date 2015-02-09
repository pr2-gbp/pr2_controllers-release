Name:           ros-indigo-pr2-calibration-controllers
Version:        1.10.13
Release:        0%{?dist}
Summary:        ROS pr2_calibration_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_calibration_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-pr2-controller-interface
Requires:       ros-indigo-pr2-mechanism-controllers
Requires:       ros-indigo-pr2-mechanism-model
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-robot-mechanism-controllers
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-pr2-controller-interface
BuildRequires:  ros-indigo-pr2-mechanism-controllers
BuildRequires:  ros-indigo-pr2-mechanism-model
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-robot-mechanism-controllers
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
The pr2_calibration_controllers package contains the controllers used to bring
all the joints in the PR2 to a calibrated state.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 09 2015 Devon Ash <dash@clearpathrobotics.com> - 1.10.13-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.10.12-0
- Autogenerated by Bloom


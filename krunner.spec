#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : krunner
Version  : 5.49.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.49/krunner-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/krunner-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/krunner-5.49.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: krunner-lib
Requires: krunner-data
Requires: krunner-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kpackage-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev
BuildRequires : solid-dev
BuildRequires : threadweaver-dev

%description
Runner Template
----------------------
-- Build instructions --
cd /where/your/runner/is/installed
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=MYPREFIX ..
make
make install

%package data
Summary: data components for the krunner package.
Group: Data

%description data
data components for the krunner package.


%package dev
Summary: dev components for the krunner package.
Group: Development
Requires: krunner-lib
Requires: krunner-data
Provides: krunner-devel

%description dev
dev components for the krunner package.


%package lib
Summary: lib components for the krunner package.
Group: Libraries
Requires: krunner-data
Requires: krunner-license

%description lib
lib components for the krunner package.


%package license
Summary: license components for the krunner package.
Group: Default

%description license
license components for the krunner package.


%prep
%setup -q -n krunner-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535432094
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535432094
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/krunner
cp COPYING.LIB %{buildroot}/usr/share/doc/krunner/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.krunner1.xml
/usr/share/kdevappwizard/templates/runner.tar.bz2
/usr/share/kservicetypes5/plasma-runner.desktop
/usr/share/xdg/krunner.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KRunner/KRunner/AbstractRunner
/usr/include/KF5/KRunner/KRunner/QueryMatch
/usr/include/KF5/KRunner/KRunner/RunnerContext
/usr/include/KF5/KRunner/KRunner/RunnerManager
/usr/include/KF5/KRunner/KRunner/RunnerSyntax
/usr/include/KF5/KRunner/krunner/abstractrunner.h
/usr/include/KF5/KRunner/krunner/krunner_export.h
/usr/include/KF5/KRunner/krunner/querymatch.h
/usr/include/KF5/KRunner/krunner/runnercontext.h
/usr/include/KF5/KRunner/krunner/runnermanager.h
/usr/include/KF5/KRunner/krunner/runnersyntax.h
/usr/include/KF5/krunner_version.h
/usr/lib64/cmake/KF5Runner/KF5RunnerConfig.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerConfigVersion.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerTargets.cmake
/usr/lib64/libKF5Runner.so
/usr/lib64/qt5/mkspecs/modules/qt_KRunner.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Runner.so.5
/usr/lib64/libKF5Runner.so.5.49.0
/usr/lib64/qt5/qml/org/kde/runnermodel/librunnermodelplugin.so
/usr/lib64/qt5/qml/org/kde/runnermodel/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/krunner/COPYING.LIB

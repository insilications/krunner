#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : krunner
Version  : 5.87.0
Release  : 42
URL      : https://download.kde.org/stable/frameworks/5.87/krunner-5.87.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.87/krunner-5.87.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.87/krunner-5.87.0.tar.xz.sig
Summary  : Framework for providing different actions given a string query
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: krunner-data = %{version}-%{release}
Requires: krunner-lib = %{version}-%{release}
Requires: krunner-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kservice-dev
BuildRequires : plasma-framework-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : threadweaver-dev

%description
<!---
# SPDX-License-Identifier: CC0-1.0
-->
# KRunner
Framework for Plasma runners

%package data
Summary: data components for the krunner package.
Group: Data

%description data
data components for the krunner package.


%package dev
Summary: dev components for the krunner package.
Group: Development
Requires: krunner-lib = %{version}-%{release}
Requires: krunner-data = %{version}-%{release}
Provides: krunner-devel = %{version}-%{release}
Requires: krunner = %{version}-%{release}

%description dev
dev components for the krunner package.


%package lib
Summary: lib components for the krunner package.
Group: Libraries
Requires: krunner-data = %{version}-%{release}
Requires: krunner-license = %{version}-%{release}

%description lib
lib components for the krunner package.


%package license
Summary: license components for the krunner package.
Group: Default

%description license
license components for the krunner package.


%prep
%setup -q -n krunner-5.87.0
cd %{_builddir}/krunner-5.87.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634512358
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634512358
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krunner
cp %{_builddir}/krunner-5.87.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/krunner/ea97eb88ae53ec41e26f8542176ab986d7bc943a
cp %{_builddir}/krunner-5.87.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/krunner/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/krunner-5.87.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/3cb34cfc72e87654683f2894299adf912d14b284
cp %{_builddir}/krunner-5.87.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/krunner-5.87.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/krunner-5.87.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/krunner/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/krunner-5.87.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/krunner/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/krunner-5.87.0/src/declarative/qmldir.license %{buildroot}/usr/share/package-licenses/krunner/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/krunner-5.87.0/templates/runner/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.krunner1.xml
/usr/share/kdevappwizard/templates/runner.tar.bz2
/usr/share/kdevappwizard/templates/runnerpython.tar.bz2
/usr/share/kservicetypes5/plasma-runner.desktop
/usr/share/qlogging-categories5/krunner.categories
/usr/share/qlogging-categories5/krunner.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KRunner/KRunner/AbstractRunner
/usr/include/KF5/KRunner/KRunner/AbstractRunnerTest
/usr/include/KF5/KRunner/KRunner/QueryMatch
/usr/include/KF5/KRunner/KRunner/RunnerContext
/usr/include/KF5/KRunner/KRunner/RunnerManager
/usr/include/KF5/KRunner/KRunner/RunnerSyntax
/usr/include/KF5/KRunner/krunner/abstractrunner.h
/usr/include/KF5/KRunner/krunner/abstractrunnertest.h
/usr/include/KF5/KRunner/krunner/krunner_export.h
/usr/include/KF5/KRunner/krunner/querymatch.h
/usr/include/KF5/KRunner/krunner/runnercontext.h
/usr/include/KF5/KRunner/krunner/runnermanager.h
/usr/include/KF5/KRunner/krunner/runnersyntax.h
/usr/include/KF5/krunner_version.h
/usr/lib64/cmake/KF5Runner/KF5KRunnerMacros.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerConfig.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerConfigVersion.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Runner/KF5RunnerTargets.cmake
/usr/lib64/libKF5Runner.so
/usr/lib64/qt5/mkspecs/modules/qt_KRunner.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Runner.so.5
/usr/lib64/libKF5Runner.so.5.87.0
/usr/lib64/qt5/qml/org/kde/runnermodel/librunnermodelplugin.so
/usr/lib64/qt5/qml/org/kde/runnermodel/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krunner/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/krunner/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/krunner/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/krunner/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/krunner/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/krunner/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/krunner/ea97eb88ae53ec41e26f8542176ab986d7bc943a

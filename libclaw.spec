%define	name	libclaw
%define	version	1.5.0b
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	C++ Library Absolutely Wonderful 
License:	GPL
Group:		System/Libraries
URL:		http://libclaw.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake jpeg-devel libpng-devel

%description
CLAW is a C++ Library Absolutely Wonderful providing useful classes 
from the simplest AVL binary search trees to the complex meta programming 
tools, including image manipulation, a generic alpha-beta algorithm, 
sockets implemented as std::stream and more.

%package devel
Summary: development package for libclaw
Group: Development/C
Requires: jpeg-devel libpng-devel

%description devel
This package provides the necessary development headers and libraries
to allow you to build programs that use libclaw.

%prep
%setup -q -n %{name}-%{version}
sed -ie 's/CLAW_INSTALLDIR_LIB lib/CLAW_INSTALLDIR_LIB %_lib/' CMakeLists.txt

%build
cmake -D CMAKE_INSTALL_PREFIX=%_prefix .
%make

%install
rm -rf  $RPM_BUILD_ROOT

%makeinstall_std

# install files

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %name -p /sbin/ldconfig
%postun -n %name -p /sbin/ldconfig

%files 
%defattr(-, root, root)
%doc COPYING
%{_libdir}/*.so

%files devel
%defattr(-, root, root)
%_includedir/claw
%_bindir/claw-config
%_datadir/cmake-2.5/Modules/FindCLAW.cmake

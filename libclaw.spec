%define	name	libclaw
%define	version	1.5.3
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	C++ Library Absolutely Wonderful 
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libclaw.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libclaw-1.5.3-fix-libdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake jpeg-devel libpng-devel
BuildRequires:	doxygen

%description
CLAW is a C++ Library Absolutely Wonderful providing useful classes 
from the simplest AVL binary search trees to the complex meta programming 
tools, including image manipulation, a generic alpha-beta algorithm, 
sockets implemented as std::stream and more.

#-----------------------------------------------------------------------

%define major 1
%define libname %mklibname claw 1

%package -n %libname
Summary: Library files for libclaw
Group: System/Libraries
Obsoletes: %name < %version

%description -n %libname
CLAW is a C++ Library Absolutely Wonderful providing useful classes
from the simplest AVL binary search trees to the complex meta programming
tools, including image manipulation, a generic alpha-beta algorithm,
sockets implemented as std::stream and more.

%files -n %libname
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

#-----------------------------------------------------------------------

%define develname %mklibname -d claw

%package -n %develname
Summary: Development package for libclaw
Group: Development/C
Requires: jpeg-devel libpng-devel
Requires: %{libname} = %{version}
Obsoletes: %{name}-devel < %{version}
Provides: %{name}-devel = %{version}

%description -n %develname
This package provides the necessary development headers and libraries
to allow you to build programs that use libclaw.

%files -n %develname
%defattr(-, root, root)
%doc ChangeLog build/doc/html
%_libdir/*.so
%_libdir/*.a
%_includedir/claw
%_bindir/claw-config
%_datadir/cmake-2.6/Modules/FindCLAW.cmake

#-----------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%cmake
%make

%install
rm -rf  $RPM_BUILD_ROOT
%makeinstall_std -C build

rm -fr %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

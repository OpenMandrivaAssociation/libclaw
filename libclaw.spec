%define major 1
%define libname %mklibname claw 1
%define develname %mklibname claw -d

Summary:	C++ Library Absolutely Wonderful 
Name:		libclaw
Version:	1.6.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libclaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/libclaw/libclaw/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	jpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CLAW is a C++ Library Absolutely Wonderful providing useful classes 
from the simplest AVL binary search trees to the complex meta programming 
tools, including image manipulation, a generic alpha-beta algorithm, 
sockets implemented as std::stream and more.

%package -n %{libname}
Summary:	Library files for libclaw
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n %{libname}
CLAW is a C++ Library Absolutely Wonderful providing useful classes
from the simplest AVL binary search trees to the complex meta programming
tools, including image manipulation, a generic alpha-beta algorithm,
sockets implemented as std::stream and more.

%package -n %{develname}
Summary:	Development package for libclaw
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package provides the necessary development headers and libraries
to allow you to build programs that use libclaw.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DCLAW_INSTALLDIR_LIB=%_lib
%make

%install
rm -rf  %{buildroot}
%makeinstall_std -C build

rm -f %buildroot%_datadir/doc

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-, root, root)

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc ChangeLog build/doc/html
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/claw
%{_bindir}/claw-config
%{_datadir}/cmake/Modules/FindCLAW.cmake

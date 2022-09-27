%define		major 1
%define		libname %mklibname claw 1
%define		develname %mklibname claw -d

Summary:	C++ Library Absolutely Wonderful 
Name:		libclaw
Version:	1.7.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libclaw.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libclaw/libclaw/%{name}-%{version}.tar.gz
Patch0:		libclaw-1.7.0-libdir.patch
Patch1:		libclaw-1.7.0-zlib.patch
Patch2:		libclaw-1.6.1-nostrip.patch
Patch3:		libclaw-1.7.4-compile.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	doxygen

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
%autosetup -p1
%cmake

%build
# Workaround for the build process not
# liking parallel builds at all
for i in `seq 1 10`; do
	%make_build -C build || :
done
make -C build

%install
%make_install -C build

rm -fr %{buildroot}%{_datadir}/doc

%__mkdir_p %{buildroot}%{_datadir}/cmake/Modules
%__mv %{buildroot}%{_datadir}/cmake/libclaw/libclaw-config.cmake %{buildroot}%{_datadir}/cmake/Modules/Findlibclaw.cmake

%find_lang %{name}

%files -f %{name}.lang
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
%{_datadir}/cmake/Modules/Findlibclaw.cmake
%{_datadir}/cmake/libclaw

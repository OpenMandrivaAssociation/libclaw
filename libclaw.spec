%define		major 1
%define		libname %mklibname claw 1
%define		develname %mklibname claw -d

Summary:	C++ Library Absolutely Wonderful 
Name:		libclaw
Version:	1.7.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libclaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/libclaw/libclaw/%{name}-%{version}.tar.gz
Patch0:		libclaw-1.7.0-libdir.patch
Patch1:		libclaw-1.7.0-zlib.patch
Patch2:		libclaw-1.6.1-nostrip.patch
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
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .libdir~
%patch1 -p1 -b .zlib~
%patch2 -p1 -b .nostrip~

%build
%cmake
%make

%install
%__rm -rf  %{buildroot}
%makeinstall_std -C build

rm -fr %{buildroot}%{_datadir}/doc

%__mkdir_p %{buildroot}%{_datadir}/cmake/Modules
%__mv %{buildroot}%{_datadir}/cmake/libclaw/libclaw-config.cmake %{buildroot}%{_datadir}/cmake/Modules/Findlibclaw.cmake

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

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


%changelog
* Sat Jan 14 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.0-1mdv2011.0
+ Revision: 760782
- Update BuildRequires
- New version 1.7.0

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2011.0
+ Revision: 609856
- fix libdir
- new version 1.6.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Sat Sep 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.4-1mdv2010.0
+ Revision: 449506
- update to new version 1.5.4
- spec file clean

* Thu Mar 26 2009 Funda Wang <fwang@mandriva.org> 1.5.3-2mdv2009.1
+ Revision: 361254
- rebuild for new cmake

* Wed Aug 06 2008 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2009.0
+ Revision: 264647
- New version 1.5.3
- use versioned lib package
- fix libdir suffix

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix summary-not-capitalized

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jan 14 2008 Olivier Blin <blino@mandriva.org> 1.5.2b-1mdv2008.1
+ Revision: 151138
- 1.5.2b

* Tue Jan 08 2008 Olivier Blin <blino@mandriva.org> 1.5.0b-2mdv2008.1
+ Revision: 146855
- require library in devel package
- merge cmake file in devel package (like pkgconfig files)

* Tue Jan 08 2008 Olivier Blin <blino@mandriva.org> 1.5.0b-1mdv2008.1
+ Revision: 146644
- fix libdir for x86_64
- fix jpeg-devel requires
- fix ldconfig calls (there is no __ldconfig macro)
- drop hardcoded requires
- fix buildrequires

  + Anne Nicolas <ennael@mandriva.org>
    - add  buildrequire
    - clean requires
    - import libclaw



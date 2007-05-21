%define	name	ecore
%define	version 0.9.9.038
%define release %mkrel 1

%define major 	1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment event/X abstraction layer
Name: 		%{name}
Version: 	%{version}
Epoch:		1
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel eet-devel
BuildRequires:	openssl-devel X11-devel
BuildRequires:	multiarch-utils

%description
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{epoch}:%{version}
Requires: %name = %{epoch}:%{version}
Provides: lib%{name}-devel %{epoch}:%{version}-%{release}
Provides: %name-devel = %{epoch}:%{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x --enable-ecore-fb
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_config

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h
%{_bindir}/%name-config
%multiarch %multiarch_bindir/%name-config
#%{_datadir}/aclocal/*.m4



%changelog
* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.9.037-1mdv2008.0
+ Revision: 17657
- Put back ecore package, /usr/bin/ecore_config still exists
- Don't require ecore, it no longer exists
- New snapshot
- Remove main binary as /usr/bin/* and /usr/share/ecore are no longer there

  + Mandriva <devel@mandriva.com>


* Sun Dec 03 2006 Pascal Terjan <pterjan@mandriva.org> 0.9.9.025-0.20060323.2mdv2007.0
+ Revision: 90216
- Require main package in -devel

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1:0.9.9.025-0.20060323.2mdv2007.0
+ Revision: 53298
- rebuild && %%mkrel
- Import ecore

* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.9.9.025-0.20060323.1mdk
- new cvs checkout

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.9.9.023-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.9.9.023-0.20060117.1mdk
- new cvs checkout

* Thu Jan 12 2006 Austin Acton <austin@mandriva.org> 1:0.9.9.022-0.20060111.1mdk
- new cvs checkout

* Thu Nov 24 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.018-0.20051124.1mdk
- new cvs checkout
- disable directfb support

* Thu Nov 17 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.9.9.018-0.20051109.2mdk
- rebuild against openssl-0.9.8

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.018-0.20051109.1mdk
- new cvs checkout

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.018-0.20051104.1mdk
- new cvs checkout

* Tue Sep 06 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.013-0.20050904.1mdk
- new cvs checkout

* Mon Aug 15 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.013-0.20050813.1mdk
- new cvs checkout

* Tue Jun 28 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.010-0.20050627.1mdk
- new cvs checkout

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.008-0.20050608.1mdk
- new cvs checkout

* Thu May 26 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050524.2mdk
- multiarch binaries

* Thu May 26 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050524.1mdk
- new cvs checkout

* Mon May 16 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.2mdk
- clean up spec

* Fri May 13 2005 Austin Acton <austin@mandriva.org> 1:0.9.9.007-0.20050511.1mdk
- epoch 1 for current cvs version
- use my own spec file (sorry)

* Sat Sep 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-0.20040913.1mdk
- 1.0.0 20040913
- adjust buildrequires


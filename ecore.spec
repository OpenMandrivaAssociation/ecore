#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/ecore ecore; \
#cd ecore; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf ecore-$PKG_VERSION.tar.xz ecore/ --exclude .svn --exclude .*ignore

%define snapshot 0

%if %snapshot
%define	svndate	20120103
%define	svnrev	66771
%endif

%define	major 1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Enlightenment event/X abstraction layer
Name:		ecore
Epoch:		3
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.3
%else
Version:	1.7.3
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(eet) >= 1.4.0
BuildRequires:	pkgconfig(eina) >= 1.0.0
BuildRequires:	pkgconfig(evas) >= 1.0.0
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(tslib-0.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xtst)

%description
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--enable-ecore-x \
	--enable-ecore-fb \
	--enable-ecore-directfb \
	--enable-ecore-con \
	--enable-ecore-file \
	--enable-ecore-sdl \
	--enable-ecore-evas \
	--enable-ecore-evas-fb \
	--enable-ecore-evas-software-x11 \
	--enable-ecore-evas-opengl-x11 \
	--enable-ecore-evas-opengl-sdl \
	--enable-ecore-evas-software-16-x11 \
	--enable-gnutls \
	--enable-curl \
	--enable-cares \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/ecore/immodules/xim.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/ecore*



%changelog
* Tue Jun 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 3:1.2.1-1
+ Revision: 807057
- version update 1.2.1

* Tue May 15 2012 Crispin Boylan <crisb@mandriva.org> 3:1.1.99.66771-0.20120103.3
+ Revision: 798898
- Rebuild
- Rebuild for new directfb

* Wed Jan 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 3:1.1.99.66771-0.20120103.1
+ Revision: 755399
- added back epoch
- fixed typoes,
- removed old configure option
- fixed files list
- new version/snapshot 1.1.99.66771
- cleaned up spec and merged with Unity Linux spec
- disabled static build
- switch openssl for gnutls, eet was already built with gnutls

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 3:1.0.1-1
+ Revision: 681650
- update to new version 1.0.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 3:1.0.0-1
+ Revision: 633924
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 3:1.0.0-0.beta3.1mdv2011.0
+ Revision: 622783
- 1.0 beta3

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 3:1.0.0-0.beta2.1mdv2011.0
+ Revision: 597517
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 3:1.0.0-0.beta.1mdv2011.0
+ Revision: 585305
- 1.0.0 beta

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 3:0.9.9.49898-1mdv2011.0
+ Revision: 550112
- update file list
- new version 0.9.9.49898

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 3:0.9.9.063-1mdv2010.1
+ Revision: 478113
- drop old condition
- new version 0.9.9.063

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3:0.9.9.062-3mdv2010.0
+ Revision: 455797
- rebuild for new curl SSL backend

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 3:0.9.9.062-2mdv2010.0
+ Revision: 411214
- enable sdl backend

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 3:0.9.9.062-1mdv2010.0
+ Revision: 411120
- 0.9.9.062

* Tue Jul 07 2009 Funda Wang <fwang@mandriva.org> 3:0.9.9.061-2mdv2010.0
+ Revision: 393239
- rebuild

* Wed Jul 01 2009 Frederik Himpe <fhimpe@mandriva.org> 3:0.9.9.061-1mdv2010.0
+ Revision: 391345
- update to new version 0.9.9.061

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 3:0.9.9.060-1mdv2010.0
+ Revision: 370657
- New version 0.9.9.060

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 3:0.9.9.050-6mdv2009.1
+ Revision: 347886
- fix build on 2009.0 release

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 3:0.9.9.050-5mdv2009.1
+ Revision: 347663
- fix provides

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 3:0.9.9.050-4mdv2009.1
+ Revision: 347589
- remove epoch

* Sat Feb 28 2009 Antoine Ginies <aginies@mandriva.com> 3:0.9.9.050-3mdv2009.1
+ Revision: 345908
- adjust the patch
- SVN SNAPSHOT 20090227, release 0.9.9.050, update eet buildrequires

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 3:0.9.9.050-2mdv2009.1
+ Revision: 301344
- rebuild for new xcb

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 3:0.9.9.050-1mdv2009.1
+ Revision: 292070
- raise versioned BR
- New snapshot

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3:0.9.9.043-2mdv2009.0
+ Revision: 266609
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 3:0.9.9.043-1mdv2009.0
+ Revision: 213978
- drop -L/usr/lib from SDL_LIBS, otherwise it will confuse compiler
- New version 0.9.9.043

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 3:0.9.9.042-4mdv2008.1
+ Revision: 168909
- fix typo in configure option
- remove old release
- cvs snapshot 20080215, add some buildrequires, update configure build options

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 3:0.9.9.042-3mdv2008.1
+ Revision: 161536
- bump epoch; major went backward

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 1:0.9.9.042-2mdv2008.1
+ Revision: 161519
- bump release
- no major in devel package

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 1:0.9.9.042-1mdv2008.1
+ Revision: 161316
- new version
- tidy spec
- fix URL
- drop ecore-config

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Austin Acton <austin@mandriva.org> 1:0.9.9.041-4mdv2008.1
+ Revision: 108057
- tidy and adjust configure options

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.041-3mdv2008.1
+ Revision: 104087
- update buildrequires
- CVS SNAPSHOT 20071031, release 0.9.9.041

* Thu Aug 30 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.041-2mdv2008.0
+ Revision: 76308
- fix missing file ecore-config
- fix path in tarball
- CVS SNAPSHOT 20070830, release 0.9.9.041

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1:0.9.9.038-8mdv2008.0
+ Revision: 36145
- rebuild with correct optflags

* Tue Jun 05 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-7mdv2008.0
+ Revision: 35857
- CVS SNAPSHOT 20070605, release 0.9.9.038

* Mon Jun 04 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-6mdv2008.0
+ Revision: 35227
- increase mkrel

* Mon Jun 04 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-5mdv2008.0
+ Revision: 35058
- CVS snapshot 20070604
- restore use of epoch
- remove epoch

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-4mdv2008.0
+ Revision: 32622
- CVS SNAPSHOT 20070529, release 0.9.9.038

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-3mdv2008.0
+ Revision: 30752
- increase mkrel

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-2mdv2008.0
+ Revision: 30751
- adjust buildrequires to a specific release of evas and eet
- increase mkrel
- CVS snapshot 20070524, release 0.9.9.038
- remove unwanted changelog

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1:0.9.9.038-1mdv2008.0
+ Revision: 29107
- cvs snapshot 20070516, release 0.9.9.038

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 1:0.9.9.037-1mdv2008.0
+ Revision: 17657
- Put back ecore package, /usr/bin/ecore_config still exists
- Don't require ecore, it no longer exists
- New snapshot
- Remove main binary as /usr/bin/* and /usr/share/ecore are no longer there


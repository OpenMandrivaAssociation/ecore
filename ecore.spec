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

%define snapshot 1

%if %snapshot
%define	svndate	20120103
%define	svnrev	66771
%endif


%define	major 1
%define	libname %mklibname %{name} %major
%define	develname %mklibname %{name} -d

Summary:	Enlightenment event/X abstraction layer
Name:		ecore
Epoch:		3
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.1.0
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.xz
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
	--enable-ecore-evas-software-16-x11 \
	--enable-gnutls \
	--enable-curl \
	--enable-cares \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
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


%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Enlightenment event/X abstraction layer
Name:		ecore
Epoch:		3
Version:	1.7.7
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

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

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
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

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/ecore*


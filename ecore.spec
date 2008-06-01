%define	name	ecore
%define version 0.9.9.043
%define release %mkrel 1

%define major	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment event/X abstraction layer
Name: 		%{name}
Version: 	%{version}
Epoch:		3
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
Patch0:		ecore-0.9.9.043-simplify-sdl-libs.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.042
BuildRequires:	eet-devel >= 0.9.10.042
BuildRequires:	openssl-devel curl-devel
BuildRequires:	X11-devel

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
Requires: %libname = %{epoch}:%{version}-%{release}
Provides: lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides: %name-devel = %{epoch}:%{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%setup -q
%patch0 -p0

%build
NOCONFIGURE=1 ./autogen.sh
export CFLAGS="%{optflags} -lX11 -lXext"
%configure2_5x --enable-ecore-fb \
	--enable-ecore-desktop \
	--enable-ecore-sdl \
	--enable-openssl \
	--enable-curl \
	--enable-ecore-evas-x11-gl \
	--enable-ecore-fb \
	--enable-ecore-evas-x11-16
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

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
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h


%define	name	ecore
%define version 1.0.0
%define release %mkrel -c beta2 1

%define major 1
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
Source: 	http://download.enlightenment.org/releases/%{name}-%{version}.beta2.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 1.0.0
BuildRequires:	eet-devel >= 1.4.0
BuildRequires:	openssl-devel curl-devel
BuildRequires: libx11-devel
BuildRequires: libxcomposite-devel
BuildRequires: libxcursor-devel
BuildRequires: libxdamage-devel
BuildRequires: libxext-devel
BuildRequires: libxfixes-devel
BuildRequires: libxi-devel
BuildRequires: libxinerama-devel
BuildRequires: libxrandr-devel
BuildRequires: libxrender-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: libxtst-devel
BuildRequires:	tslib-devel
BuildRequires:	SDL-devel

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
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%setup -qn %{name}-%{version}.beta2

%build
%configure2_5x --enable-ecore-fb \
	--enable-ecore-sdl \
	--enable-openssl \
	--enable-curl

# fix libtool issue on release < 2009.1
%if %mdkversion < 200910
perl -pi -e "s/^ECHO.*/ECHO='echo'\necho='echo'\n/" libtool
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*

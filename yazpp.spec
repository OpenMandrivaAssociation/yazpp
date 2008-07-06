%define	major 2
%define libname %mklibname yazpp %{major}
%define develname %mklibname yazpp -d

Summary:	Application programming interface (API) to YAZ
Name:		yazpp
Version:	1.1.1
Release:	%mkrel 1
License:	BSD
Group:		System/Libraries
Url:		http://www.indexdata.com/yazplusplus/
Source0:	http://ftp.indexdata.dk/pub/yaz++/%{name}-%{version}.tar.bz2
Patch0:		yazpp-1.0.4-config.patch
BuildRequires:	libyaz-devel >= 3.0.18
BuildRequires:	libicu-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
YAZ++ is an C++ binding to YAZ.

%package -n %{libname}
Summary:	Z39.50/SRW/SRU C++ libraries
Group:		System/Libraries

%description -n %{libname}
Z39.50/SRW/SRU C++ libraries.

%package -n %{develname}
Summary:	Yaz++ development headers (API)
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname yazpp -d 2
Provides:	%mklibname yazpp -d 2

%description -n %{develname}
YAZ++ is an application programming interface (API) to YAZ which supports 
the development of Z39.50/SRW/SRU client and server applications using C++. 
Like YAZ, it supports Z39.50-2003 (version 3) as well as SRW/SRU version 1.1 in
both the client and server roles. YAZ++ includes an implementation of the 
ZOOM C++ binding and a generic client/server API based on the 
Observer/Observable design pattern.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-shared \
	--disable-static

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
%multiarch_binaries %{buildroot}/%{_bindir}/%{name}-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root) 
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO LICENSE
%{multiarch_bindir}/%{name}-config
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/aclocal/yazpp.m4
%{_datadir}/doc/%{name}/*
%{_mandir}/man8/yazpp-config.*

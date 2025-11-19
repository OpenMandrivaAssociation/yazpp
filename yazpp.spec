%define	major 6
%define libname %mklibname yazpp %{major}
%define develname %mklibname yazpp -d

Summary:	Application programming interface (API) to YAZ
Name:		yazpp
Version:	1.9.0
Release:	1
License:	BSD-3-Clause
Group:		System/Libraries
Url:		https://www.indexdata.com/yazplusplus/
Source0:	https://download.indexdata.com/pub/yazpp/yazpp-1.9.0.tar.gz

BuildSystem:    autotools
BuildOption:   --enable-shared --disable-static

BuildRequires:	pkgconfig(yaz) >= 3.0.18
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	docbook-style-dsssl
BuildRequires:  docbook-style-xsl

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
Obsoletes:      %{mklibname -d yazpp 2} < %{EVRD}
Provides:	%mklibname yazpp -d 2

%description -n %{develname}
YAZ++ is an application programming interface (API) to YAZ which supports 
the development of Z39.50/SRW/SRU client and server applications using C++. 
Like YAZ, it supports Z39.50-2003 (version 3) as well as SRW/SRU version 1.1 in
both the client and server roles. YAZ++ includes an implementation of the 
ZOOM C++ binding and a generic client/server API based on the 
Observer/Observable design pattern.

%files -n %{libname}
%defattr(-,root,root) 
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO LICENSE
%{_bindir}/%{name}-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_datadir}/aclocal/yazpp.m4
%{_datadir}/doc/%{name}/*
%{_libdir}/pkgconfig/%name.pc
%{_mandir}/man1/%name-config.1.zst


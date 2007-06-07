%define	major 2
%define libname %mklibname yazpp %{major}

Summary:	YAZ++ is an application programming interface (API) to YAZ
Name:		yazpp
Version:	1.0.3
Release:	%mkrel 1
License:	BSD
Group:		System/Libraries
Source0:	http://ftp.indexdata.dk/pub/yaz++/%{name}-%{version}.tar.bz2
Url:		http://www.indexdata.com/yazplusplus/
BuildRequires:	libyaz-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Yaz C++ bindings.

%package -n %{libname}
Summary:	Z39.50/SRW/SRU C++ libraries
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}

%description -n %{libname}
Z39.50/SRW/SRU C++ libraries.


%package -n %{libname}-devel
Summary:	Yaz++ development headers (API)
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
YAZ++ is an application programming interface (API) to YAZ which supports 
the development of Z39.50/SRW/SRU client and server applications using C++. 
Like YAZ, it supports Z39.50-2003 (version 3) as well as SRW/SRU version 1.1 in 
both the client and server roles. YAZ++ includes an implementation of the 
ZOOM C++ binding and a generic client/server API based on the 
Observer/Observable design pattern.

%prep
%setup -q %{name}-%{version}

%build
%configure2_5x \
	--enable-shared \
	--with-pic \
	--disable-static

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
%multiarch_binaries %{buildroot}/%{_bindir}/%{name}-config

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

#%files
#%defattr(644,root,root,755)

%files -n %{libname}
%defattr(-,root,root) 
%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
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
%{_mandir}/man8/yazpp-config.8.bz2
   
%define		_modname	xdiff
%define		_status		stable

Summary:	%{_modname} - File differences/patches
Summary(pl):	%{_modname} - Wy¶wietlanie ró¿nic pomiêdzy plikami oraz tworzenie ³atek
Name:		php-pecl-%{_modname}
Version:	1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	2a9f46065c01eaeab0d146f9ad25a5e5
URL:		http://pecl.php.net/package/xdiff/
BuildRequires:	libtool
BuildRequires:	libxdiff-devel
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension creates and applies patches to both text and binary
files.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie potrafi tworzyæ i nak³adaæ ³aty zarówno dla plików
tekstowych jak i binarnych.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README.API,tests}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so

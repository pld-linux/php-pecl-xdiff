%define		_modname	xdiff
%define		_status		beta
Summary:	%{_modname} - file differences/patches
Summary(pl.UTF-8):	%{_modname} - wyświetlanie różnic pomiędzy plikami oraz tworzenie łatek
Name:		php-pecl-%{_modname}
Version:	1.5.1
Release:	3
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	d8c386c98130e724a07b62f5152130e5
Patch0:		%{name}-tsrm.patch
URL:		http://pecl.php.net/package/xdiff/
BuildRequires:	libxdiff-devel >= 0.22
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension creates and applies patches to both text and binary
files.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
To rozszerzenie potrafi tworzyć i nakładać łaty zarówno dla plików
tekstowych jak i binarnych.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
cd %{_modname}-%{version}
%patch0 -p2

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README.API,tests}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so

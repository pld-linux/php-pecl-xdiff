%define		php_name	php%{?php_suffix}
%define		modname	xdiff
%define		status		beta
Summary:	%{modname} - file differences/patches
Summary(pl.UTF-8):	%{modname} - wyświetlanie różnic pomiędzy plikami oraz tworzenie łatek
Name:		%{php_name}-pecl-%{modname}
Version:	1.5.2
Release:	6
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	8b6f93bd700198c52da6e45949f95f3c
Patch0:		php-pecl-%{modname}-tsrm.patch
URL:		http://pecl.php.net/package/xdiff/
BuildRequires:	%{php_name}-devel >= 3:5.0.4
BuildRequires:	libxdiff-devel >= 0.22
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pecl-xdiff < 1.5.2-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension creates and applies patches to both text and binary
files.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
To rozszerzenie potrafi tworzyć i nakładać łaty zarówno dla plików
tekstowych jak i binarnych.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch -P0 -p2

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS README.API tests
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so

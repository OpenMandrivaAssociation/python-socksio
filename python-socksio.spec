Name:		python-socksio
Version:	1.0.0
Release:	2
Summary:	Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5
License:	MIT
Group:		Development/Python
URL:		https://github.com/sethmlarson/socksio
Source0:	https://files.pythonhosted.org/packages/source/s/socksio/socksio-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(flit-core)

%description
Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/socksio
%{py_sitedir}/socksio-*.*-info

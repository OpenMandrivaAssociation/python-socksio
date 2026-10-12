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
BuildRequires:	python%{pyver}dist(flit-core)

%description
Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5.

%prep -a
# flit 4 no longer reads [tool.flit.metadata].
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["flit_core >=3.2"]
build-backend = "flit_core.buildapi"

[project]
name = "socksio"
description = "Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5"
readme = "README.md"
requires-python = ">=3.6"
license = "MIT"
authors = [{name = "Seth Michael Larson", email = "sethmichaellarson@gmail.com"}]
dynamic = ["version"]
classifiers = [
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Internet :: Proxy Servers",
]

[tool.flit.module]
name = "socksio"
EOF

%files
%doc README.md
%license LICENSE
%{py_sitedir}/socksio
%{py_sitedir}/socksio-*.*-info

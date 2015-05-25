%define 	module	pygit2

Summary:	Python bindings for libgit2 library
Name:		python-%{module}
Version:	0.20.3
Release:	2
License:	GPL v2 with linking exception
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pygit2/%{module}-%{version}.tar.gz
# Source0-md5:	1efcc58383fd2e558a8d3cba4dcc4754
URL:		https://pypi.python.org/pypi/pygit2
BuildRequires:	libgit2-devel
BuildRequires:	python-devel
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pygit2 is a set of Python bindings to the libgit2 shared library.

%package -n python3-%{module}
Summary:	Python 3 bindings for libgit2 library
Group:		Libraries/Python
Requires:	libgit2

%description -n python3-%{module}
pygit2 is a set of Python 3 bindings to the libgit2 shared library.

%prep
%setup -q -n %{module}-%{version}

%{__rm} test/test_{credentials,repository}.py

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%check
%{__python} setup.py build -b python test
%{__python3} setup.py build -b python3 test

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install	\
	--optimize=2				\
	--root=$RPM_BUILD_ROOT

%{__python3} setup.py build -b python3 install	\
	--optimize=2				\
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.rst TODO.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/pygit2/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/pygit2-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc COPYING README.rst TODO.txt
%attr(755,root,root) %{py3_sitedir}/*.so
%{py3_sitedir}/%{module}
%{py3_sitedir}/pygit2-*.egg-info


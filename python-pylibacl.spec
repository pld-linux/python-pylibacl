# TODO:
# - build in %build
# - optflags

%define 	module	pylibacl

Summary:	A Python module for manipulating POSIX.1e ACLs
Summary(pl.UTF-8):	Moduł języka Python pozwalający na dostęp do ACL standardu POSIX.1e
Name:		python-%{module}
Version:	0.2.2
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pylibacl/%{module}-%{version}.tar.gz
# Source0-md5:	5628def6afb4b8c37040fc42f7c59eec
URL:		http://pylibacl.sourceforge.net/
BuildRequires:	acl-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for accessing Extended Attributes of the files.

%description -l pl.UTF-8
Moduł języka Python pozwalający na dostęp do rozszerzonych atrybutów
plików.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html BENCHMARK IMPLEMENTATION PLATFORMS README ChangeLog
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.egg-info

%global debug_package %{nil}

Name:           libtree
Version:        1.0
Release:        1%{?dist}
Summary:        Implementation of AVL (Adelson-Velskii and Landis) balanced trees

License:        MIT
URL:            https://piumarta.com/software/tree/
Source0:        %{url}/tree-%{version}.tar.gz

%define common_desc tree.h Implementation of AVL (Adelson-Velskii and Landis) \
balanced trees in the spirit of the BSD queue and list implementations.

%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: libtree-static = %{version}-%{release}

%description devel
%{common_desc}

%prep
%autosetup -n tree-%{version}

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 tree.h %{buildroot}%{_includedir}

%files devel
%{_includedir}/tree.h

%changelog
* Sat Mar 20 2021 Timothée Floure <fnux@fedoraproject.org> - 1.0-1
- Let there be package.

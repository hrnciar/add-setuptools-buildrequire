%global debug_package %{nil}
%global commit 8e1c0a5699c34bc4952e86dc0509070770f2c625

Name:           mum-hash
Version:        0
Release:        1.20210318git%{commit}%{?dist}
Summary:        Fast non-cryptographic hash function

License:        MIT
URL:            https://github.com/vnmakarov/mum-hash
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

%define common_desc MUM hash is a fast non-cryptographic hash function suitable for \
different hash table implementations.

%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: mum-hash-static = %{version}-%{release}

%description devel
%{common_desc}

%prep
%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 mum.h %{buildroot}%{_includedir}
install -p -m 644 mum-prng.h %{buildroot}%{_includedir}
install -p -m 644 mum512.h %{buildroot}%{_includedir}

%files devel
%doc README.md ChangeLog
%{_includedir}/mum*h

%changelog
* Thu Mar 18 2021 Timothée Floure <fnux@fedoraproject.org> - 0-1.20210318git8e1c0a5
- Let there be package.

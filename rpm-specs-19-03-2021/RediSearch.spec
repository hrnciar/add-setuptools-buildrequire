%global module	redisearch
Name:		RediSearch
Version:	1.2.2
Release:	4%{?dist}
Summary:	Full-text search over Redis

%global disable_tests 0

License:	AGPLv3
URL:		https://goodformcode.com/
Source0:	https://github.com/GoodFORM/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# "RediSearch is developed and tested on Linux and Mac OS, on x86_64 CPUs." from docs/index.md
ExclusiveArch:  x86_64

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	python3
BuildRequires:	python3-rmtest >= 1
BuildRequires:	redis-devel
BuildRequires:	redis >= 4
Requires:	redis >= 4
Requires:	redis(modules_abi)%{?_isa} = %{redis_modules_abi}

%description
RediSearch implements a search engine on top of Redis, providing
three main features - full text search, secondary indexing and a
suggestion (auto-completion) engine.

It provides advanced search features like exact phrase matching
and numeric filtering for text queries, that are not possible or
efficient with traditional Redis search approaches.

%prep
%setup -q

%build
make %{?_smp_mflags} LD="cc" LDFLAGS="%{?__global_ldflags}"

%if !%{disable_tests}
%check
make PYTHON="python3" test
%endif

%install
mkdir -p %{buildroot}%{redis_modules_dir}
install -pDm755 src/%{module}.so %{buildroot}%{redis_modules_dir}/%{module}.so

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md docs/*.md docs/*.png docs/img/*.png
%{redis_modules_dir}/%{module}.so

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 1.2.2-2
- Add ExclusiveArch: x86_64

* Sun Mar 29 2020 Nathan Scott <nathans@redhat.com> - 1.2.2-1
- Initial package (BZ #1820391)

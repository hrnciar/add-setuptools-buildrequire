%global forgeurl https://github.com/jreese/znc-push
%global commit  4243934d5bb09ee8f7aa700a1b6bf57b3fcdd6a3
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}
%forgemeta

%global modname push
%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Push notification service module for ZNC

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  libcurl-devel
BuildRequires:  znc-devel
BuildRequires:  zlib-devel

Requires:       znc%{?_isa} = %znc_version

%description
ZNC Push is a module for ZNC that will send notifications to multiple push
notification services, or SMS for any private message or channel highlight
that matches a configurable set of conditions.

%prep
%forgesetup
# fix README permissions
chmod -x README.md

%build
CXXFLAGS="%{optflags} -DUSE_CURL $(pkg-config --libs libcurl) -DPUSHVERSION=%{shortcommit}" \
LDFLAGS="%{__global_ldflags}" \
  znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%license LICENSE
%doc README.md logo.png doc
%{_libdir}/znc/%{modname}.so

%changelog
* Wed Mar 10 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.0.0-2.20210204git4243934
- Fix README permissions

* Thu Feb  4 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.0.0-1.20210204git4243934
- Initial package

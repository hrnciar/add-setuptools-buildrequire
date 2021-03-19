# Generated by go2rpm
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/go-redis/redis
%global goipath         gopkg.in/redis.v2
%global forgeurl        https://github.com/go-redis/redis
Version:                2.3.2

%gometa

%global goaltipaths     github.com/go-redis/redis

%global common_description %{expand:
Type-safe Redis client for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        Type-safe Redis client for Golang

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# test fixes and do not assume use of system redis-server for testing
Patch0:         redis-testing-fixes.patch
# error message has changed
Patch1:         0001-Fix-error-message-in-TestAuth.patch

BuildRequires:  redis
BuildRequires:  golang(gopkg.in/bufio.v1)
BuildRequires:  golang(gopkg.in/check.v1)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1

%install
%gopkginstall

%if %{with check}
%check
# Run a test Redis server rather than assuming the system
# is running one already (see patch0) - non-default port.
redis-cli -p 8126 SHUTDOWN 2>/dev/null || true
redis-server --port 8126 &
sleep 0.2   # time to startup
redis-cli -p 8126 PING || exit 1
%gocheck
redis-cli -p 8126 SHUTDOWN || exit 1
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 01:06:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.3.2-7
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 00:32:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.3.2-2
- Update to new macros

* Fri Mar 22 2019 Nathan Scott <nathans@redhat.com> - 2.3.2-1
- First package for Fedora

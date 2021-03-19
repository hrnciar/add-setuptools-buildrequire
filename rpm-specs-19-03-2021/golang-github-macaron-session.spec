# golang-github-macaron-session.spec
# Generated by go2rpm
%bcond_without check

# https://github.com/go-macaron/session
%global goipath         github.com/go-macaron/session
Version:                1.0.2

%gometa

%global goipathsex      github.com/go-macaron/session/couchbase github.com/go-macaron/session/ledis github.com/go-macaron/session/nodb

%global common_description %{expand:
Middleware session provides session management for Macaron. It can use many
session providers, including memory, file, Redis, Memcache, PostgreSQL, MySQL.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Middleware that provides the session management of Macaron

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# ensure tests use in-memory databases and on non-default ports
Patch0:         0001-Ensure-tests-use-in-memory-databases-and-on-non-defa.patch

BuildRequires:  golang(gitea.com/lunny/nodb)
BuildRequires:  golang(gitea.com/lunny/nodb/config)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/couchbase/go-couchbase)
BuildRequires:  golang(github.com/go-redis/redis/v8)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/siddontang/ledisdb/config)
BuildRequires:  golang(github.com/siddontang/ledisdb/ledis)
BuildRequires:  golang(github.com/unknwon/com)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/macaron.v1)
# perform testing on in-memory databases
BuildRequires:  redis memcached nmap-ncat net-tools procps

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
# stop any pre-existing redis and memcached servers running
printf "shutdown\r\nquit\r\n" | ncat localhost 8131 2>/dev/null || true
redis-cli -p 8130 shutdown 2>/dev/null || true
# start temporary redis and memcached instances for testing
memcached -A --port 8131 &
redis-server --port 8130 &
sleep 0.5   # give these test services some time to startup
echo "-- Server processes"
ps aux | egrep 'redis-server|memcached'
echo "-- Server ports"
netstat -tulnp | egrep '8130|8131'
# run the actual tests
echo "-- Run tests"
%gocheck -t couchbase -t ledis -t nodb
echo "-- Done"
# stop both the newly-created redis and memcached instances
printf "shutdown\r\nquit\r\n" | ncat localhost 8131
redis-cli -p 8130 shutdowm
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 12:32:00 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Wed Jul 29 17:35:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20200729git7d919ce
- Bump to commit 7d919ce6a8d29a256134ca60e9e92da5c76f137f

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 01:20:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190328git0a0a789
- Update to new macros

* Fri May 03 2019 Mark Goodwin <mgoodwin@redhat.com> - 0-0.3.20190328git0a0a789
- Package rebuild for incorrect version in changelog

* Fri May 03 2019 Nathan Scott <nathans@redhat.com> - 0-0.2.20190328git0a0a789
- Package rebuild for correct dependencies

* Thu Mar 28 2019 Nathan Scott <nathans@redhat.com> - 0-0.1.20190328git0a0a789
- First package for Fedora
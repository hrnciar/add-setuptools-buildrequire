# Generated by go2rpm
# Tests need to be set up: https://github.com/jackc/pgx#testing
%bcond_with check

# https://github.com/jackc/pgx
%global goipath         github.com/jackc/pgx
Version:                4.10.1

%gometa

%global goaltipaths     github.com/jackc/pgx/v4

%global common_description %{expand:
Pgx is a pure Go driver and toolkit for PostgreSQL. pgx is different from other
drivers such as pq because, while it can operate as a database/sql compatible
driver, pgx is also usable directly. It offers a native interface similar to
database/sql that offers better performance and more features.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        PostgreSQL driver and toolkit for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jackc/pgconn)
BuildRequires:  golang(github.com/jackc/pgconn/stmtcache)
BuildRequires:  golang(github.com/jackc/pgio)
BuildRequires:  golang(github.com/jackc/pgproto3/v2)
BuildRequires:  golang(github.com/jackc/pgtype)
BuildRequires:  golang(github.com/jackc/puddle)
BuildRequires:  golang(github.com/rs/zerolog)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  golang(gopkg.in/inconshreveable/log15.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 13:08:44 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.10.1-1
- Update to 4.10.1
- Close: rhbz#1882952

* Wed Sep 09 12:38:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.8.1-1
- Update to 4.8.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 21:57:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.3.0-1
- Initial package

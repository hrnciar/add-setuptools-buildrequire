# Generated by go2rpm 1
# Doesn't work within Mock restrictive system
%bcond_with check

# https://github.com/jackc/pgconn
%global goipath         github.com/jackc/pgconn
Version:                1.8.0

%gometa

%global common_description %{expand:
Package pgconn is a low-level PostgreSQL database driver. It operates at nearly
the same level as the C library libpq. It is primarily intended to serve as the
foundation for higher level libraries such as https://github.com/jackc/pgx.
Applications should handle normal queries with a higher level library and only
use pgconn directly when required for low-level access to PostgreSQL
functionality.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Low-level PostgreSQL database driver

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jackc/chunkreader/v2)
BuildRequires:  golang(github.com/jackc/pgio)
BuildRequires:  golang(github.com/jackc/pgpassfile)
BuildRequires:  golang(github.com/jackc/pgproto3/v2)
BuildRequires:  golang(github.com/jackc/pgservicefile)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/text/secure/precis)
BuildRequires:  golang(golang.org/x/xerrors)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 18:02:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Wed Sep 09 12:21:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.4-1
- Initial package

# Generated by go2rpm 1.3
%ifnarch %{arm} %{ix86}
%bcond_without check
%endif

# https://github.com/couchbase/go-couchbase
%global goipath         github.com/couchbase/go-couchbase
%global commit          c04035124b17427663771bd1bdc98f38cad82993

%gometa

%global common_description %{expand:
Couchbase client in Go.}

%global golicenses      LICENSE
%global godocs          examples README.markdown

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Couchbase client in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

# Only in examples
# BuildRequires:  golang(github.com/couchbase/gomemcached)
BuildRequires:  golang(github.com/couchbase/gomemcached/client)
BuildRequires:  golang(github.com/couchbase/goutils/logging)
# Only in examples
# BuildRequires:  golang(github.com/couchbaselabs/go_n1ql)
BuildRequires:  golang(github.com/Pallinder/go-randomdata)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 12:57:08 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210110gitc040351
- Initial package

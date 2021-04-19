%bcond_without check

# https://github.com/haproxytech/client-native
%global goipath         github.com/haproxytech/client-native
Version:                2.2.0

%gometa

%global goaltipaths     %{goipath}/v2

%global common_description %{expand:
Go client for HAProxy configuration and runtime API.}

%global golicenses      LICENSE
%global godocs          README.md README-runtime.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go client for HAProxy configuration and runtime API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/common)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/errors)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/params)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers/filters)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers/http/actions)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers/stats/settings)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers/tcp/actions)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/parsers/tcp/types)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/spoe)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/spoe/types)
BuildRequires:  golang(github.com/haproxytech/config-parser/v3/types)
BuildRequires:  golang(github.com/haproxytech/models/v2)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/pkg/errors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv runtime/README.md README-runtime.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:03:58 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0
- Close: rhbz#1916915

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1914253)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-1
- Update to version 2.2.0-rc1 (Fixes rhbz#1914253)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-1
- Update to version 2.1.0 (Fixes rhbz#1859323)

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Fri May 08 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Update to version 2.0.1

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Upgrade to version 2.0.0

* Wed Apr 15 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.7-1
- Update to version 1.2.7

* Tue Apr 14 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-4
- Add specific versions for haproxytech BuildRequires

* Mon Apr 13 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-3
- Remove runtime/README.md

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-2
- Clean changelog

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.6-1
- Initial package


%bcond_without check

# https://github.com/alibabacloud-go/tea
%global goipath         github.com/alibabacloud-go/tea
Version:                1.1.15

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL.}

%global golicenses      LICENSE
%global godocs          README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/modern-go/reflect2)
BuildRequires:  golang(golang.org/x/net/proxy)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%ifarch armv7hl i686
# Skip 'tea' tests due to 64-bit tests that will fail
%gocheck -d 'tea'
%else
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Wed Jan 27 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.15-1
- Update to version 1.1.15 (Fixes rhbz#1920813)
- Add new golang(github.com/json-iterator/go) and
  golang(github.com/modern-go/reflect2) BuildRequires
- Skip 'tea' tests due to 64-bit tests that will fail

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.14-1
- Update to version 1.1.14 (Fixes rhbz#1917438)

* Wed Jan  6 2021 Brandon Perkins <bperkins@redhat.com> - 1.1.13-1
- Update to version 1.1.13 (Fixes rhbz#1913305)

* Mon Nov 30 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.12-1
- Update to version 1.1.12 (Fixes rhbz#1902686)

* Mon Oct 19 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.11-1
- Update to version 1.1.11 (Fixes rhbz#1889458)

* Tue Sep 08 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.10-1
- Update to version 1.1.10 (Fixes rhbz#1876623)

* Sun Aug 23 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.8-1
- Update to version 1.1.8 (Fixes rhbz#1871444)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-2
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-1
- Update to version 1.1.7 (Fixes rhbz#1811174)
- Enable check stage
- Clean changelog

* Thu Mar 05 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.7-1
- Initial package


# Generated by go2rpm
# Need network access
%bcond_with check

# https://github.com/hashicorp/go-retryablehttp
%global goipath         github.com/hashicorp/go-retryablehttp
Version:                0.6.8

%gometa

%global common_description %{expand:
The Retryablehttp package provides a familiar HTTP client interface with
automatic retries and exponential backoff. It is a thin wrapper over the
standard net/http client library and exposes nearly the same public API. This
makes retryablehttp very easy to drop into existing programs.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Retryable http client in go

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/hashicorp/go-hclog)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 09:05:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.8-1
- Update to 0.6.8
- Close: rhbz#1867266

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 21:34:07 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.6-1
- Update to 0.6.6

* Fri Jan 31 18:22:53 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.4-1
- Update to 0.6.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.4-2
- Add Obsoletes for old name

* Wed Apr 17 16:28:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.4-1
- Release 0.5.4

* Tue Mar 26 17:46:41 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.3-1
- Release 0.5.3 (#1669775)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git6e85be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.git6e85be8
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git6e85be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.git6e85be8
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.20161130git6e85be8
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git6e85be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git6e85be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6e85be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git6e85be8
- First package for Fedora
  resolves: #1410392
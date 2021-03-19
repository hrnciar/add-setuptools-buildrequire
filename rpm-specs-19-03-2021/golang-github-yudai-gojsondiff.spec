# Generated by go2rpm
%bcond_without check

# https://github.com/yudai/gojsondiff
%global goipath         github.com/yudai/gojsondiff
Version:                1.0.0
%global commit          0525c875b75ca60b9e67ddc44496aa16f21066b0

%gometa

%global common_description %{expand:
Package Gojsondiff implements "Diff" that compares two JSON objects and
generates Deltas that describes differences between them. The package also
provides "Patch" that apply Deltas to a JSON object.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Go JSON Diff

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(github.com/yudai/golcs)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 19:03:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2.20190514git0525c87
- Bump to commit 0525c875b75ca60b9e67ddc44496aa16f21066b0

* Fri Mar 15 2019 Nathan Scott <nathans@redhat.com> - 1.0.0-1
- First package for Fedora

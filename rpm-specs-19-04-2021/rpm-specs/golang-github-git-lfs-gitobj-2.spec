# Generated by go2rpm 1
%bcond_without check

# https://github.com/git-lfs/gitobj/v2
%global goipath         github.com/git-lfs/gitobj
Version:                2.0.1

%gometa

%global godevelname %{goname}-2-devel
%global goaltipaths     github.com/git-lfs/gitobj/v2
%global godevelheader %{expand:
Conflicts: %{goname}-devel
}

%global common_description %{expand:
Gitobj reads and writes Git objects.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}-2
Release:        2%{?dist}
Summary:        Gitobj reads and writes Git objects

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version (#1909129)

* Tue Sep 01 16:29:21 EDT 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Initial package

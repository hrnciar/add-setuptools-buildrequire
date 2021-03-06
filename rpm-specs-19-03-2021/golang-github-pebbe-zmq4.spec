# Generated by go2rpm 1
%bcond_without check

# https://github.com/pebbe/zmq4
%global goipath         github.com/pebbe/zmq4
Version:                1.2.5

%gometa

%global godevelheader %{expand:
Requires:       zeromq-devel >= 4.0.1}

%global common_description %{expand:
A Go interface to ZeroMQ version 4.}

%global golicenses      LICENSE.txt
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go interface to ZeroMQ version 4

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  zeromq-devel >= 4.0.1

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
* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.5-1
- Update to latest version (#1930559)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.2-1
- Update to latest version (#1904590)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Fri Feb 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 00:38:35 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.0.0-4
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.0-2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it???s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to tagged version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git5b443b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.20180610git5b443b6
- Add explicit zeromq Req

* Sun Jun 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180610git5b443b6
- First package for Fedora

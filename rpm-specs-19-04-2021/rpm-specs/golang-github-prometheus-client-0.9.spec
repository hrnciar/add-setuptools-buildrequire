# Generated by go2rpm
%bcond_without check

# https://github.com/prometheus/client_golang
%global goipath         github.com/prometheus/client_golang-0.9
%global forgeurl        https://github.com/prometheus/client_golang
Version:                0.9.4

%gometa

%global goname golang-github-prometheus-client-0.9
%global godevelname golang-github-prometheus-client-devel-0.9

%global common_description %{expand:
This is the Go client library for Prometheus. It has two separate parts, one for
instrumenting application code, and one for creating clients that talk to the
Prometheus HTTP API.}

%global golicenses      LICENSE NOTICE
%global godocs          examples CHANGELOG.md CONTRIBUTING.md MAINTAINERS.md README.md README-prometheus.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        7%{?dist}
Summary:        Prometheus instrumentation library for go applications

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/beorn7/perks/quantile)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/prometheus/procfs)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/prometheus/client_golang|github.com/prometheus/client_golang-0.9|' $(find . -iname "*.go" -type f)
cp %{S:1} %{S:2} .
mv prometheus/README.md README-prometheus.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck -t prometheus
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 22:39:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.4-6
- Compat version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-2
- Add Obsoletes for old name

* Sat Jun 22 23:37:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.4-1
- Release 0.9.4

* Thu Apr 18 17:19:27 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.2-1
- Release 0.9.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.5.git180b8fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.9.0-0.4.git180b8fd
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.3.git180b8fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.9.0-0.2.git180b8fd
- Upload glide files

* Tue May 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-0.1.20180526git180b8fd
- Update to 0.9.0 pre snapshot to fix syncthing builds.
- Update to spec 3.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.0-7
- Bump to upstream c5b7fccd204277076155f10851dad72b76a49317
  related: #1214784

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0.7.0-4
- Bump to upstream 449ccefff16c8e2b7229f6be1921ba22f62461fe
  related: #1214784

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 jchaloup <jchaloup@redhat.com> - 0.7.0-1
- Bump to upstream e51041b3fa41cece0dca035740ba6411905be473
  related: #1214784

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0.6.0-3
- Add Godeps.json to doc
  related: #1214784

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.6.0-2
- Update spec file to spec-2.0
- Disabled failing test prometheus
- Disabled failing test model
  resolves: #1214784

* Thu Jul 23 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.6.0-1
- Bump to upstream 36659fa1ad85ee0dd33822b68a192a814c93a57b
  related: #1214784

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-1
- Bump to upstream b0bd7e1be33327b85cb4853e7011156e3cedd657
  related: #1214784

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0.4.0-1
- Bump to upstream 608ec8b69e284600a7ad1b36514a1e6876e22b9f
  resolves: #1214784

* Wed Mar 04 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gite5098ac
- Bump to upstream e5098ac1ff13c7f85b68b120b253dd834ba49682
  related: #1190442

* Thu Feb 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git39e4bc8
- Bump to upstream 39e4bc83f974fb141a9e67c042b26322bacc917b
  related: #1190442

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git52186fc
- First package for Fedora
  resolves: #1190442

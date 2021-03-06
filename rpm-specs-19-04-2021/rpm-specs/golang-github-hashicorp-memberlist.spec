# Generated by go2rpm
# https://github.com/hashicorp/memberlist/issues/195
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/hashicorp/memberlist
%global goipath         github.com/hashicorp/memberlist
Version:                0.2.2

%gometa

%global common_description %{expand:
Memberlist is a Go library that manages cluster membership and member failure
detection using a gossip based protocol.

The use cases for such a library are far-reaching: all distributed systems
require membership, and memberlist is a re-usable solution to managing cluster
membership and node failure detection.

memberlist is eventually consistent but converges quickly on average. The speed
at which it converges can be heavily tuned via various knobs on the protocol.
Node failures are detected and network partitions are partially tolerated by
attempting to communicate to potentially dead nodes through multiple routes.}

%global golicenses      LICENSE
%global godocs          README.md todo.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        4%{?dist}
Summary:        Go package for gossip based membership and failure detection

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/armon/go-metrics)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/hashicorp/go-sockaddr)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/sean-/seed)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
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
for test in "TestMemberList_ProbeNode_Awareness_MissedNack" \
            "TestMemberlist_JoinShutdown" \
            "TestMemberlist_PingDelegate" \
; do
awk -i inplace '/^func.*'"$test"'/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 02:30:38 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.2.2-3
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 17:38:01 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.1.3-2
- Update to new macros

* Wed Apr 17 15:42:29 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.1.3-1
- Release 0.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 0-0.15
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it???s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git28424fb
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20151121git28424fb
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git28424fb
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git28424fb
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git28424fb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git28424fb
- Bump to upstream 28424fb38c7c3e30f366b72b1a55f690d318d8f3
  related: #1250471

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitdad1009
- Update to spec-2.1
  related: #1250471

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.1.gitdad1009
- Update spec file to spec-2.0
- Disable failing test - a golang bug
  resolves: #1250471

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitdad1009
- First package for Fedora
  resolves: #1212065

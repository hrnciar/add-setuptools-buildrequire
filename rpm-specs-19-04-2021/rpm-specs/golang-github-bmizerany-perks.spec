# Generated by go2rpm
%bcond_without check

# https://github.com/bmizerany/perks
%global goipath         github.com/bmizerany/perks
%global commit          d9a9656a3a4b1c2864fdb44db2ef8619772d92aa

%gometa

%global common_description %{expand:
Perks contains the Go package quantile that computes approximate quantiles over
an unbounded data stream within low memory and CPU bounds.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.24%{?dist}
Summary:        Effective Computation of approximate quantiles

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml
Patch0:         add-license.patch
Patch1:         Fix-formatting.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 23:05:33 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.23.20140716gitd9a9656
- There was no FTBFS, probably a random issue during testing.

* Sat Aug 22 22:15:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.22.20140716gitd9a9656
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 20:10:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.18.20140716gitd9a9656
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.16.20140716gitd9a9656
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.20140716gitd9a9656
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20140716gitd9a9656
- Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20140716gitd9a9656
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitd9a9656
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitd9a9656
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitd9a9656
- Update to spec-2.1
  related: #1248668

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitd9a9656
- Update spec file to spec-2.0
  resolves: #1248668

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitd9a9656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitd9a9656
- First package for Fedora
  resolves: #1190431

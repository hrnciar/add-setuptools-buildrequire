# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python          /usr/bin/python3
%else
%global python          /usr/bin/python2
%endif

Name: preproc-rpmspec
Version: 1.2
Release: 2%{?dist}
Summary: Minimalistic tool for rpm spec-file preprocessing
License: GPLv2+
URL: https://pagure.io/preproc-rpmspec.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/preproc-rpmspec.git#170f5b859704dcaf63f9b5f3f047ec439da545e3:
%endif

# Source is created by:
# git clone https://pagure.io/preproc-rpmspec.git
# cd preproc-rpmspec
# git checkout preproc-rpmspec-1.2-1
# ./rpkg spec --sources
Source0: preproc-rpmspec-170f5b85.tar.gz

BuildArch: noarch

%if 0%{?rhel} && 0%{?rhel} < 8
Requires: python2-configparser
%endif

Requires: preproc
Requires: rpkg-macros >= 1.0

%description
Minimalistic tool to perform rpm spec-file preprocessing by using
preproc utilility and rpkg-macros. It can preprocess an rpm
spec file and print the result to stdout or to a file.

%prep
%setup -T -b 0 -q -n preproc-rpmspec

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 preproc-rpmspec %{buildroot}%{_bindir}
sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/preproc-rpmspec

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/preproc-rpmspec

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 clime <clime@fedoraproject.org> 1.2-1
- rewrite into python, add --check-context and --outdir, --no-outdir options

* Thu Oct 08 2020 Michal Novotný <michal.novotny@comprimato.com> 1.1-1
- set lead to empty

* Mon Oct 05 2020 Michal Novotný <michal.novotny@comprimato.com> 1.0-1
- Require rpkg-macros >= 1.0

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.3-1
- no change, just a new tag

* Mon Mar 09 2020 clime <clime@fedoraproject.org> 0.2-1
- update description in spec

* Sun Mar 08 2020 clime <clime@fedoraproject.org> 0.1-1
- odd support for macros that produce files (git_archive/git_pack)
- replace --in-space with --output
- add note about the need to trust the spec files that are being preprocessed
- initial commit

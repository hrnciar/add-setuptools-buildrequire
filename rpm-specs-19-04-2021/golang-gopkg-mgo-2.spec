# Generated by go2rpm
%bcond_without check

# https://github.com/go-mgo/mgo
%global goipath         gopkg.in/mgo.v2
%global forgeurl        https://github.com/go-mgo/mgo
Version:                r2016.08.01
%global commit          a6b53ec6cb22a3699387a57a161566f9402ee85b

%gometa

%global common_description %{expand:
The MongoDB driver for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        MongoDB driver for Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/tomb.v2)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
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
# .: needs network
# txn: needs mongodb
%gocheck -d . -d dbtest -d txn
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - r2016.08.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 18:13:59 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - r2016.08.01-6.20200805gita6b53ec
- Bump to commit a6b53ec6cb22a3699387a57a161566f9402ee85b

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - r2016.08.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - r2016.08.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - r2016.08.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - r2016.08.01-2.20190703git9856a29
- Add Obsoletes for old name

* Mon Jun 03 17:44:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - r2016.08.01-1.20190703git9856a29
- Release r2016.08.01, commit 9856a29383ce1c59f308dd1cf0363a79b5bef6b5

* Thu Feb 07 2019 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.git39b4000
- Remove mongo-db from deps, yet keep the package available in case
  users install the mongo-db from different sources.
  See https://pagure.io/fesco/issue/2078 ticket.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git39b4000
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git39b4000
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Marek Skalický <mskalick@redhat.com> - 0-0.11.git39b4000
- Rebase to version used by mongo-tools

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gite30de8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gite30de8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gite30de8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gite30de8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gite30de8a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gite30de8a
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gite30de8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 jchaloup <jchaloup@redhat.com> - 0-0.3.gite30de8a
- Bump to upstream e30de8ac9ae3b30df7065f766c71f88bba7d4e49
  related: #1232226

* Wed Jan 27 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.git3569c88
- Update spec file to spec-2.1
  related: #1232226

* Mon Jun 15 2015 Marek Skalicky <mskalick@redhat.com> - 0-0.1.git3569c88
- First package for Fedora
  resolves: #1232226
# Generated by go2rpm
%bcond_without check

# https://github.com/tdewolff/parse
%global goipath         github.com/tdewolff/parse
Version:                2.5.15

%gometa

%global goaltipaths     github.com/tdewolff/parse/v2

%global common_description %{expand:
Go parsers for web formats.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go parsers for web formats

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/tdewolff/test) >= 1.0.6
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
* Sat Apr 17 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.15-1
- Update to latest version (#1950146)

* Tue Mar 16 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.14-1
- Update to latest version (#1939319)

* Tue Mar 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.12-1
- Update to latest version (#1933964)

* Mon Feb 22 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.11-1
- Update to latest version (#1930465)

* Wed Feb 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.10-1
- Update to latest version (#1927069)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.9-1
- Update to latest version (#1925846)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 14:48:30 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.8-1
- Update to 2.5.8
- Close: rhbz#1918505

* Sat Dec 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.7-1
- Update to latest version (#1910821)

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.6-1
- Update to latest version (#1901745)

* Fri Oct 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.5-1
- Update to latest version (#1888868)

* Thu Oct 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.4-1
- Update to latest version (#1884203)

* Fri Sep 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.3-2
- rebuilt

* Wed Sep 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.3-1
- Update to latest version (#1882117)

* Sat Sep 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.2-1
- Update to latest version (#1876038)

* Sat Aug 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.1-1
- Update to latest version (#1873760)

* Thu Aug 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.0-1
- Update to latest version (#1872962)

* Mon Aug 24 11:25:45 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.4-3
- Add alternate import path

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.4-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.2-1
- Update to latest version

* Wed Jan 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.1-1
- Update to latest version

* Sat Nov 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version

* Tue Nov 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.13-1
- Update to latest version

* Mon Nov 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.12-1
- Update to latest version

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.11-1
- Update to latest version

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.10-1
- Update to latest version

* Fri Aug 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.9-1
- Update to latest version

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.8-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 22:41:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.3.7-2
- Update to new macros

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.7-1
- Update to latest version

* Mon Apr 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.6-1
- Update to latest version

* Sat Mar 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.5-2
- Use unversioned import path until Go modules are supported in Fedora

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.5-1
- First package for Fedora

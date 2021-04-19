%bcond_without check

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.3.5

%gometa

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Markdown parser written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Thu Apr 15 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.5-1
- Update to latest version (#1949409)

* Sun Apr 11 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.4-1
- Update to latest version (#1948195)

* Sun Mar 21 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.3-1
- Update to latest version (#1941238)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version (#1925924)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version (#1910997)

* Sun Dec 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version (#1907235)

* Sat Aug 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Sun Jul 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.33-1
- Update to latest version

* Sat Jun 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.32-1
- Update to latest version

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.31-1
- Update to latest version

* Thu Apr 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.30-1
- Update to latest version

* Wed Apr 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.29-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.27-1
- Update to latest version

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.26-1
- Update to latest version

* Mon Mar 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.25-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.24-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.23-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.22-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.19-1
- Update to latest version

* Wed Oct 16 06:30:44 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Initial package

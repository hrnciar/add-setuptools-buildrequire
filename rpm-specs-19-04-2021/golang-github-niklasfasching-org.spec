# Generated by go2rpm 1
%bcond_without check

# https://github.com/niklasfasching/go-org
%global goipath         github.com/niklasfasching/go-org
Version:                1.5.0

%gometa

%global common_description %{expand:
Org mode parser with html & pretty printed org rendering.}

%global golicenses      LICENSE
%global godocs          README.org

Name:           %{goname}
Release:        1%{?dist}
Summary:        Org mode parser with html & pretty printed org rendering

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/chroma) >= 0.8.2
BuildRequires:  golang(github.com/alecthomas/chroma/formatters/html)
BuildRequires:  golang(github.com/alecthomas/chroma/lexers)
BuildRequires:  golang(github.com/alecthomas/chroma/styles)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib) >= 1
%endif

%description
%{common_description}

%package -n go-org
Summary:        Org mode parser with html & pretty printed org rendering

%description -n go-org
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/go-org %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n go-org
%license LICENSE
%doc README.org
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Apr 11 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version (#1948341)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version (#1912052)

* Wed Jul 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Sun Jul 05 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Sat Apr 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.9-1
- Update to latest version

* Mon Nov 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.8-1
- Update to latest version

* Sun Oct 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.7-1
- Update to latest version

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.6-1
- Update to latest version

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.5-1
- Update to latest version

* Tue Sep 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.4-1
- Update to latest version

* Sun Aug 18 19:06:06 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-1
- Initial package

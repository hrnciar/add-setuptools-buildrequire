# Generated by go2rpm
%bcond_without check

# https://github.com/dominikh/go-tools
%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                2020.2.1
%global tag             2020.2.1

%gometa

%global common_description %{expand:
honnef.co/go/tools/... is a collection of tools and libraries for working with
Go code, including linters and static analysis, most prominently staticcheck.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Collection of static analysis tools for working with Go code

# Upstream license specification: BSD-3-Clause and MIT
License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/kisielk/gotool)
BuildRequires:  golang(golang.org/x/tools/go/analysis)
BuildRequires:  golang(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/ast/inspector)
BuildRequires:  golang(golang.org/x/tools/go/buildutil)
BuildRequires:  golang(golang.org/x/tools/go/loader)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/go/types/objectpath)
BuildRequires:  golang(golang.org/x/tools/go/types/typeutil)
BuildRequires:  golang(golang.org/x/tools/refactor/importgraph)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/*; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# https://github.com/dominikh/go-tools/issues/687
%gocheck -d unused -d staticcheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 20:27:02 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2020.2.1-1
- Update to 2020.2.1
- Close: rhbz#1918542

* Sat Dec 26 10:18:07 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2020.2-1
- Update to 2020.2
- Close: rhbz#1887385

* Thu Aug 06 14:57:49 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2020.1.5-1
- Update to 2020.1.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 16:57:55 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2019.2.3-1
- Update to 2019.2.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 23:25:11 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2019.2.2-1
- Release 2019.2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 22:58:09 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2019.1.1-2
- Update to new macros

* Sun Mar 17 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2019.1.1-1
- Release 2019.1.1 (#1689449)

* Tue Feb 19 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2019.1-1
- Update to 2019.1
- Fixes #1675047

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 2017.2.2-1
- First package for Fedora

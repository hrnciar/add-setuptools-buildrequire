%global packname statnet.common
%global packver  4.4.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.4.1
Release:          2%{?dist}
Summary:          Common R Scripts and Utilities Used by the Statnet Project Software

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils, R-methods, R-coda, R-parallel, R-tools, R-rle
# Suggests:  R-covr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-coda
BuildRequires:    R-parallel
BuildRequires:    R-tools
BuildRequires:    R-rle

%description
Non-statistical utilities used by the software developed by the Statnet
Project. They may also be of use to others.


%prep
%setup -q -c -n %{packname}

sed -i '/covr/d' %{packname}/DESCRIPTION

# Duplicate of NEWS.
rm %{packname}/NEWS.md


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.4.1-1
- Update to latest version (#1884877)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 4.3.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.2.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.4-1
- Update to latest version

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.2-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 4.0.0-2
- rebuild for R 3.5.0

* Tue Mar 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.0-1
- initial package for Fedora

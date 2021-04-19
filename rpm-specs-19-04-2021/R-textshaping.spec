%global packname textshaping
%global packver  0.3.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Bindings to the HarfBuzz and Fribidi Libraries for Text Shaping

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 1.0.0
# Suggests:  R-covr, R-knitr, R-rmarkdown
# LinkingTo: R-cpp11, R-systemfonts
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 1.0.0
BuildRequires:    R-cpp11-devel
BuildRequires:    R-covr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(fribidi)
BuildRequires:    pkgconfig(harfbuzz)

%description
Provides access to the text shaping functionality in the HarfBuzz library and
the bidirectional algorithm in the Fribidi library. textshaping is a low-level
utility package mainly for graphic devices that expands upon the font tool-set
provided by the systemfonts package.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version (#1937377)

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version (#1927437)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version (#1897163)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-1
- initial package for Fedora

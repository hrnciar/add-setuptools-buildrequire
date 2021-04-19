%global srcname ocrmypdf

Name:           %{srcname}
Version:        12.0.0~b1
Release:        1%{?dist}
Summary:        Add an OCR text layer to scanned PDF files

# Main code: MPL2.0;
# Completion files, hocrtransform.py: MIT;
# _unicodefun.py: BSD;
# Test files: CC-BY-SA and Public Domain
License:        MPL2.0 and MIT and BSD and CC-BY-SA and Public Domain
URL:            https://github.com/jbarlow83/OCRmyPDF
Source0:        %{pypi_source %{srcname} 12.0.0b1}

BuildArch:      noarch

BuildRequires:  ghostscript >= 9.15
BuildRequires:  pngquant >= 2.0.0
BuildRequires:  qpdf >= 8.1.0
BuildRequires:  tesseract >= 4.0.0
BuildRequires:  tesseract-osd
BuildRequires:  tesseract-langpack-deu
#BuildRequires:  unpaper >= 6.1
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.9.1
BuildRequires:  python3dist(coloredlogs) >= 14
BuildRequires:  (python3dist(img2pdf) >= 0.3 with python3dist(img2pdf) < 0.5)
BuildRequires:  (python3dist(pdfminer.six) >= 20191110 with python3dist(pdfminer.six) <= 20201018)
BuildRequires:  python3dist(pikepdf) >= 2.10
BuildRequires:  python3dist(pillow) >= 8.1.2
BuildRequires:  (python3dist(pluggy) >= 0.13 with python3dist(pluggy) < 1)
BuildRequires:  python3dist(pytest) >= 6
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-xdist) >= 2.2
BuildRequires:  python3dist(python-xmp-toolkit) >= 2.0.1
BuildRequires:  python3dist(reportlab) >= 3.5.66
BuildRequires:  python3dist(setuptools) >= 30.3
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(tqdm) >= 4

Requires:       ghostscript >= 9.15
Recommends:     pngquant >= 2.0.0
Requires:       qpdf >= 8.1.0
Requires:       tesseract >= 3.04
#Recommends:     unpaper >= 6.1

%description
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be
searched or copy-pasted.


%package -n %{srcname}-doc
Summary:        ocrmypdf documentation
License:        CC-BY-SA

%description -n %{srcname}-doc
Documentation for ocrmypdf


%prep
%autosetup -n %{srcname}-12.0.0b1 -p1

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# We don't build docs against the installed version, so force the version.
sed -i -e "s/release = get_distribution('ocrmypdf').version/release = '%{version}'/g" docs/conf.py
sed -i -e "s/__version__ = .\+/__version__ = '%{version}'/" src/ocrmypdf/_version.py

# Cleanup shebang and executable bits.
for f in src/%{srcname}/*.py src/%{srcname}/*/*.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
    chmod -x $f
done


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install

# Install completion files.
install -Dpm 0644 misc/completion/ocrmypdf.bash %{buildroot}%{_datadir}/bash-completion/completions/ocrmypdf
install -Dpm 0644 misc/completion/ocrmypdf.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ocrmypdf.fish


%check
%{pytest} -ra -n auto


%files -n %{srcname}
%doc README.md
%license LICENSE
%{_bindir}/ocrmypdf
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-12.0.0b1-py%{python3_version}.egg-info/
%{_datadir}/bash-completion/completions/ocrmypdf
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ocrmypdf.fish

%files -n %{srcname}-doc
%doc html
%license LICENSE


%changelog
* Fri Apr 09 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 12.0.0~b1-1
- Update to latest version (#1947690)

* Sun Mar 21 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.7.3-1
- Update to latest version (#1940814)

* Sat Mar 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.7.1-1
- Update to latest version (#1935602)

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.7.0-1
- Update to latest version (#1933386)

* Mon Feb 15 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.6.2-1
- Update to latest version (#1928669)

* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.6.0-1
- Update to latest version (#1920463)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.5.0-1
- Update to latest version (#1914595)

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.4.5-1
- Update to latest version (#1913459)

* Fri Jan 01 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.4.4-1
- Update to latest version (#1911957)

* Wed Dec 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.4.3-1
- Update to latest version (#1911615)

* Tue Dec 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.4.2-1
- Update to latest version (#1904259)

* Sat Dec 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.4.0-1
- Update to latest version (#1904259)

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.3.3-1
- Update to latest version (#1894119)

* Thu Oct 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.3.1-1
- Update to latest version (#1892199)

* Mon Oct 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.3.0-1
- Update to latest version (#1891263)

* Thu Oct 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.2.1-1
- Update to latest version (#1885990)

* Thu Oct 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.1.2-1
- Update to latest version (#1884208)

* Fri Sep 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.1.1-1
- Update to latest version (#1882640)

* Sat Sep 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.1.0-1
- Update to latest version (#1880187)

* Thu Sep 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.0.2-1
- Update to latest version (#1876854)

* Sat Aug 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 11.0.1-1
- Update to latest version (#1868493)

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 10.3.3-1
- Update to latest version
- Fixes rhbz#1866266

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 10.3.1-1
- Update to latest version
- Fixes rhbz#1860767

* Sat Jul 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 10.3.0-1
- Update to latest version
- Fixes rhbz#1859892

* Mon Jul 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 10.2.0-1
- Update to latest version

* Sun Jun 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.8.2-1
- Update to latest version

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.8.1-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 9.8.0-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.8.0-1
- Update to latest version

* Thu Apr 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.7.2-1
- Update to latest version

* Mon Apr 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.7.1-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.7.0-1
- Update to latest version

* Tue Mar 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.6.1-1
- Update to latest version

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.6.0-1
- Update to latest version

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.5.0-1
- Update to latest version

* Mon Jan 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.4.0-1
- Update to latest version

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.3.0-1
- Update to latest version

* Sat Nov 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.1.1-1
- Update to latest version

* Mon Nov 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.0.5-1
- Update to latest version

* Mon Nov 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.0.4-1
- Update to latest version

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.0.3-2
- Stop running flaky test

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.0.3-1
- Update to latest version

* Sat Aug 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 9.0.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.3.2-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.3.2-1
- Update to latest version

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.3.0-1
- Update to latest version
- Add completion files

* Thu Apr 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.2.4-1
- Update to latest version

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.2.3-1
- Update to latest version

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.2.2-2
- Add explicit sphinx_rtd_theme BuildRequires

* Fri Mar 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.2.2-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.1.0-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 8.0.0-1
- Update to latest version

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.4.0-1
- Update to latest version

* Sun Oct 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.2.1-1
- Update to latest version

* Tue Sep 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.1.0-1
- Update to latest version

* Fri Sep 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.6-1
- Update to latest version

* Sat Aug 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.4-1
- Update to latest version

* Thu Aug 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.3-2
- Remove extraneous shebangs
- Fix summary line
- Remove workaround for reportlab packaging bug

* Wed Aug 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.3-1
- Initial package.

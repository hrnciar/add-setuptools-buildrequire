# These are problematic, sometimes they randomly fail or hang
%bcond_with xvfb_tests

# Does not support python2 at all
%global srcname fslpy

%global desc \
The fslpy project is a FSL programming library written in Python. It is used by \
FSLeyes.

Name:           python-%{srcname}
Version:        3.5.3
Release:        1%{?dist}
Summary:        The FSL Python Library


License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  dcm2niix
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist deprecation}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist nibabel} > 2.2.1
BuildRequires:  %{py3_dist pytest pytest-cov}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wxpython}
BuildRequires:  xorg-x11-server-Xvfb


%description
%{desc}

%{?python_enable_dependency_generator}

%package -n python3-%{srcname}
Summary:        %{summary}

%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{desc}


%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description doc
This package contains documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rfv %{srcname}.egg-info

# For the dep generator to pick up
cat requirements-extra.txt >> requirements.txt

# Remove * from versions, rpm dep generator can't handle it:
# https://bugzilla.redhat.com/show_bug.cgi?id=1758141
# Fixed in F32+, but keeping it here for F31
sed -i -e 's/numpy.*/numpy>=1.0,<2.0/' -e 's/six.*/six>=1.0,<2.0/' -e 's/wxpython.*/wxpython>=4.0,<5.0/' -e '/dataclasses/ d' requirements.txt


# remove unneeded shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env python$/ d' {} 2>/dev/null ';'
# some scripts have the shebang, so we correct these
find . -type f -name "*.py" -exec sed -i 's/#![  ]*\/usr\/bin\/env python$/#!\/usr\/bin\/python3/' {} 2>/dev/null ';'

%build
%py3_build

# Build documentation
PYTHONPATH=.  sphinx-build-3 doc html
# Remove build artefacts
rm -frv html/.buildinfo
rm -frv html/.doctrees

%install
%py3_install

# Remove test packages that are installed in site packages
rm -rfv %{buildroot}/%{python3_sitelib}/tests/

%check
# For F < 33: ppc64le bug with numpy, pillow
# https://bugzilla.redhat.com/show_bug.cgi?id=1738752
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/BEKJIVVK4D73RAV6C26ZBV47S4R7DULX/
%if 0%{?fedora} >= 33

%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fslpy/blob/master/.ci/test_template.sh
xvfb-run pytest-3 tests/test_idle.py
sleep 10
# Sometimes fails, sometimes passes
xvfb-run pytest-3 tests/test_platform.py || exit 0
%endif

# Ignore tests that have already been done
# Ignore immv_imcp because it requires a "nobody" user
# Ignore tests that require downloading data.
# Ignore tests requiring trimesh
# Ignore test using dcm2niix
# Ignore failing test: https://github.com/pauldmccarthy/fslpy/issues/10
pytest-3 tests  -m "not longtest" \
  --ignore=tests/test_idle.py --ignore=tests/test_platform.py \
  --ignore=tests/test_immv_imcp.py --ignore=tests/test_atlases.py \
  --ignore=tests/test_atlases_query.py \
  --ignore=tests/test_scripts/test_atlasq_list_summary.py \
  --ignore=tests/test_scripts/test_atlasq_ohi.py \
  --ignore=tests/test_scripts/test_atlasq_query.py --ignore=tests/test_callfsl.py \
  --ignore=tests/test_mesh.py --ignore=tests/test_dicom.py \
  --ignore=tests/test_parse_data.py \
  --ignore=tests/test_scripts/test_fsl_apply_x5.py
%endif


%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst
%{python3_sitelib}/fsl
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/atlasq
%{_bindir}/atlasquery
%{_bindir}/fsl_apply_x5
%{_bindir}/fsl_ents
%{_bindir}/fsl_convert_x5
%{_bindir}/imcp
%{_bindir}/imglob
%{_bindir}/immv
%{_bindir}/resample_image
%{_bindir}/Text2Vest
%{_bindir}/Vest2Text
%{_bindir}/fsl_abspath
%{_bindir}/imln
%{_bindir}/imrm
%{_bindir}/imtest
%{_bindir}/remove_ext

%files doc
%license LICENSE COPYRIGHT
%doc html

%changelog
* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.5.3-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.4.0-1
- Update to 3.4.0

* Sun Oct 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.3.3-1
- Update to latest patch release

* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.3.0-2
- Disable tests to make it build on F32 ppc

* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.3.0-1
- Update to latest release

* Mon Sep 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.2-3
- Use quotes

* Mon Sep 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.2-2
- Add workaround to fix tests

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.2-1
- Update to new release

* Mon Jul 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.0-4
- Include patch to dump data

* Fri Jul 03 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.0-3
- Remove dataclasses that is part of Python 3.7+
- rhbz#1851358

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.0-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.2.0-1
- Update to 3.2.0

* Fri May 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.1-1
- Update to 3.0.1

* Fri Feb 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.8.1-1
- Update to 2.8.1

* Thu Jan 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.8.0-2
- Temporarily patch requirements to work around dep-generator-bug
- https://bugzilla.redhat.com/show_bug.cgi?id=1758141

* Thu Jan 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.8.0-1
- Update to 2.8.0
- drops rtree=0.8.3 requirement (#1794617)
- enable fixed tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 2.7.0-1
- Update to 2.7.0

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.6.2-1
- Update to 2.6.2

* Mon Sep 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 2.6.1-1
- Update to 2.6.1

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.5.0-2
- Disable failing test on f32

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.5.0-1
- Update to 2.5.0
- Disable failing tests

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 5 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.0-2
- Disable failing test for F29
- https://github.com/pauldmccarthy/fslpy/issues/4
- Update all branches to ensure update path is correct

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.2.0-1
- Update to 2.2.0
- Use dep generator
- Update ignored test locations

* Sun Apr 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-1
- Update to 2.1.0

* Sun Apr 14 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.1-2
- Add BR to build docs correctly

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.1-1
- Update to 2.0.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.12.0-3
- Fix doc build on < F30
- Fix test by requiring higher nibabel

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.12.0-2
- Correct shebangs
- Move Requires to the sub package

* Thu Nov 01 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.12.0-1
- Initial build

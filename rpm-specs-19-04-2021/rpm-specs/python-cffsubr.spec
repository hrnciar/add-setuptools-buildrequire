%global srcname cffsubr

Name:           python-%{srcname}
Version:        0.2.8
Release:        2%{?dist}
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool

License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
# From setup_requires in setup.py:
BuildRequires:  python3dist(setuptools-scm)

%global txbin /usr/bin/tx

BuildRequires:  %{txbin}
BuildRequires:  symlinks

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%generate_buildrequires
%pyproject_buildrequires -x testing

%package -n python3-%{srcname}
Summary:        %{summary}

Requires:       %{txbin}

%description -n python3-%{srcname}
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep
%autosetup -n %{srcname}-%{version}

# Patch out setuptools-git-ls-files dependency
sed -r -i '/setuptools-git-ls-files/d' setup.py pyproject.toml

# Do not build the extension, which is a copy of the “tx” executable from
# adobe-afdko:
sed -r -i 's/(ext_modules=)/# \1/' setup.py

# Remove bundled adobe-afdko:
rm -rf external

%build
%py3_build

%install
%py3_install

# Workaround to prevent a dangling symlink:
install -d "%{buildroot}$(dirname '%{txbin}')"
ln -s '%{txbin}' '%{buildroot}%{txbin}'

# Build a relative symbolic link:
ln -s '%{buildroot}%{txbin}' %{buildroot}/%{python3_sitelib}/%{srcname}/tx
symlinks -c -o %{buildroot}/%{python3_sitelib}/%{srcname}/tx

%check
%if 0%{?fedora} == 33
# Fixing this would require an adobe-afdko update; see
# https://github.com/adobe-type-tools/cffsubr/issues/13.
%global koption -k 'not (TestSubroutinize and test_non_standard_upem_mute_font_matrix_warning)'
%endif
%pytest %{?koption}

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
# This was just a workaround:
%exclude %{txbin}

%changelog
* Mon Mar  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.2.8-2
- New upstream version 0.2.8
- Simplify files list
- Patch out (missing) setuptools-git-ls-files BR; add missing setuptool-scm BR
- Unbundle tx executable from adobe-afdko and switch package to noarch
- Drop obsolete python_provide macro
- Use %%pytest macro to run the tests
- Use generated BR’s

* Mon Feb 15 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 0.2.7-1
- Initial packaging

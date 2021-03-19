%global srcname jose
%global _summary JOSE implementation in Python

Name:           python-%{srcname}
Version:        3.2.0
Release:        5%{?dist}
Summary:        A JOSE implementation in Python

License:        MIT
URL:            https://github.com/mpdavis/%{name}
Source0:        %{pypi_source %{name}}
BuildArch:      noarch

# Upstream support for ecdsa >= 0.16
# https://github.com/mpdavis/python-jose/pull/199
Patch0:         %{name}-3.2.0-pr-199.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# From setup_requires:
BuildRequires:  python3dist(pytest-runner)

# Documentation
BuildRequires:  make
BuildRequires:  doxygen
# From requirements-rtd.txt:
# sphinxcontrib-napoleon==0.3.4; but napoleon is now part of Sphinx proper
BuildRequires:  python3dist(sphinx)

# Fedora packages pycryptodomex, but not pycryptodome (which conflicts with
# pycrypto). Upstream refuses to switch to pycryptodomex for the pycryptodome
# backend (https://github.com/mpdavis/python-jose/issues/26), so we disable the
# corresponding extra because it will fail to install.
#
# We also obsolete the old backend subpackage that required pycryptodomex,
# because it did not do what it claimed to do.
%if 0%{?fedora} == 0 || 0%{?fedora} < 38
Obsoletes:      python3-%{srcname}-pycryptodome < 3.2.0-3
%endif

# Upstream recommends the cryptography backend. We add it as a soft dependency
# so that anyone who does not go out of their way to select a different backend
# gets the best experience.
%if 0%{?fedora} == 32
Recommends:     python3-%{srcname}+cryptography = %{version}-%{release}
%else
Recommends:     python3dist(python-jose[cryptography])
%endif

%global common_description %{expand:
The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web
Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web
Algorithms (JWA) - collectively can be used to encrypt and/or sign content
using a variety of algorithms. While the full set of permutations is extremely
large, and might be daunting to some, it is expected that most applications
will only use a small set of algorithms to meet their needs.

As of 3.1.0, python-jose implements four different cryptographic backends. The
backend must be selected as an extra when installing python-jose. If you do not
select a backend, the native-python backend will be installed.

Unless otherwise noted, all backends support all operations.

Due to complexities with setuptools, the native-python backend is always
installed, even if you select a different backend on install.

  1. cryptography
       * This backend uses pyca/cryptography for all cryptographic operations.
         This is the recommended backend and is selected over all other
         backends if any others are present.
       * Installation: dnf install python3-jose+cryptography
       * Unused dependencies:
           - rsa
           - ecdsa
           - pyasn1

  2. pycryptodome
       * This backend uses pycryptodome for all cryptographic operations.
       * Installation: not available because pycryptodome (which, unlike
                       pycryptodomex, conflicts with pycrypto) is not packaged
       * Unused dependencies:
           - rsa

  3. native-python
       * This backend uses python-rsa and python-ecdsa for all cryptographic
         operations. This backend is always installed but any other backend
         will take precedence if one is installed.
       * Installation: dnf install python3-jose

     Note

     The native-python backend cannot process certificates.

  4. pycrypto
       * This backend uses pycrypto for all cryptographic operations.
       * Installation: dnf install python3-jose+pycrypto
       * Unused dependencies:
           - rsa

     Warning

     The pycrypto project has not been maintained since 2013. This backend is
     maintained for legacy compatibility purposes only. Do not use this backend
     unless you cannot use any of the others.}

%description %{common_description}


%generate_buildrequires
%pyproject_buildrequires -t -x cryptography,pycrypto


%package -n     python3-%{srcname}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides python3-%{srcname}
%endif

%description -n python3-%{srcname} %{common_description}


%package doc
Summary:        Documentation for %{name}

%description doc %{common_description}


# We use the expansion of (on a single line):
#
#   %%python_extras_subpkg -n python3-%%{srcname}
#     -i %%{python3_sitelib}/*.dist-info
#     cryptography pycrypto
#
# macro, but add Provides/Obsoletes for the old backend subpackages.
#
# Even though Fedora 32 does not have
# https://fedoraproject.org/wiki/Changes/PythonExtras, these metapackages will
# still work; they just will not provide python3dist(python-jose[*]), and they
# need manual Requires.


%package -n python3-%{srcname}+cryptography
Summary:        Metapackage for python3-%{srcname}: cryptography extras

Requires:       python3-%{srcname} = %{version}-%{release}
%if 0%{?fedora} == 0 || 0%{?fedora} < 38
Provides:       python3-%{srcname}-cryptography = %{version}-%{release}
Obsoletes:      python3-%{srcname}-cryptography < 3.2.0-3
%endif
%if 0%{?fedora} == 32
Requires:       python3dist(cryptography)
%endif

%description -n python3-%{srcname}+cryptography
This is a metapackage bringing in cryptography extras requires for
python3-%{srcname}.
It contains no code, just makes sure the dependencies are installed.

%files -n python3-%{srcname}+cryptography
%ghost %{python3_sitelib}/*.dist-info


%package -n python3-%{srcname}+pycrypto
Summary: Metapackage for python3-%{srcname}: pycrypto extras

Requires: python3-%{srcname} = %{version}-%{release}
%if 0%{?fedora} == 0 || 0%{?fedora} < 38
Provides:       python3-%{srcname}-pycrypto = %{version}-%{release}
Obsoletes:      python3-%{srcname}-pycrypto < 3.2.0-3
%endif
%if 0%{?fedora} == 32
Requires:       python3dist(pyasn1)
Requires:       python3dist(pycrypto) >= 2.6.0 with python3dist(pycrypto) < 2.7.0
%endif

%description -n python3-%{srcname}+pycrypto
This is a metapackage bringing in pycrypto extras requires for python3-%{srcname}.
It contains no code, just makes sure the dependencies are installed.

%files -n python3-%{srcname}+pycrypto
%ghost %{python3_sitelib}/*.dist-info


%prep
%autosetup -p1

rm -rvf *.egg-info *.dist-info

# Patch out pycryptodome backend extra and tests where required; see note near
# the BR’s
sed -r -i '/^[[:blank:]]*pycryptodome/d' tox.ini requirements.txt

# The napoleon extension is now part of Sphinx proper:
sed -r -i 's/(sphinx)contrib(\.napoleon)/\1.ext\2/g' docs/conf.py


%build
%pyproject_wheel

%make_build -C docs SPHINXOPTS='%{_smp_mflags}' html
rm -vf docs/_build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
echo '>>> Backend: native-python <<<' 1>&2
m='not (cryptography or pycryptodome or pycrypto or backend_compatibility)'
%{pytest} -k "${k}" -m "${m}" tests

echo '>>> Backend: cryptography <<<' 1>&2
m='not (pycryptodome or pycrypto or backend_compatibility)'
%{pytest} -k "${k}" -m "${m}" tests

echo '>>> Backend: pycrypto <<<' 1>&2
m='not (cryptography or pycryptodome or backend_compatibility)'
%{pytest} -k "${k}" -m "${m}" tests

echo '>>> Cross-backend compatibility and coexistence <<<' 1>&2
%{pytest} -k "${k}" tests


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%files doc
%license LICENSE
%doc docs/_build/html


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.2.0-5
- Drop python3dist(setuptools) BR, redundant with %%pyproject_buildrequires

* Fri Mar 05 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.2.0-4
- Backport unreleased ecdsa 0.16 support from upstream. Fixes
  TestECAlgorithm.test_key_too_short test.

* Sat Feb 27 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.2.0-3
- Change “test_key_too_short” skip from patch to pytest option
- Simplify use of name macros
- Switch URL to HTTPS
- Improved summaries and descriptions
- After verifying no dependent packages use them, replace the ad-hoc backend
  metapackages with standard extras metapackages
- Drop obsolete python_provide macro
- Use %%pytest macro and print a message for each backend-specific test
  invocation
- Whitespace changes
- Remove explicit/manual Requires from main package
- Use pyproject-rpm-macros, including generated BR’s
- Fedora packages pycryptodomex, but not pycryptodome (which conflicts with
  pycrypto). Upstream refuses to switch to pycryptodomex for the pycryptodome
  backend (https://github.com/mpdavis/python-jose/issues/26), so we disable the
  corresponding extra because it will fail to install.
- Add a soft dependency on the cryptography backend extra
- Build the HTML documentation in a new -doc subpackage

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 23:59:32 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.2.0-1
- 3.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Chenxiong Qi <qcxhome@gmail.com> - 3.1.0-1
- Initial package.

%global srcname pycryptodomex
%global _description %{expand:PyCryptodome is a self-contained Python package of low-level cryptographic
primitives. It's a fork of PyCrypto. It brings several enhancements with respect
to the last official version of PyCrypto (2.6.1), for instance:

  * Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
  * Accelerated AES on Intel platforms via AES-NI
  * Elliptic curves cryptography (NIST P-256 curve only)
  * Better and more compact API (nonce and iv attributes for ciphers, automatic
    generation of random nonces and IVs, simplified CTR cipher mode, and more)
  * SHA-3 (including SHAKE XOFs) and BLAKE2 hash algorithms
  * Salsa20 and ChaCha20 stream ciphers
  * scrypt and HKDF
  * Deterministic (EC)DSA
  * Password-protected PKCS#8 key containers
  * Shamir's Secret Sharing scheme
  * Random numbers get sourced directly from the OS (and not from a CSPRNG in
    userspace)
  * Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
  * Major clean ups and simplification of the code base

PyCryptodome is not a wrapper to a separate C library like OpenSSL. To the
largest possible extent, algorithms are implemented in pure Python. Only the
pieces that are extremely critical to performance (e.g. block ciphers) are
implemented as C extensions.

Note: all modules are installed under the Cryptodome package to avoid conflicts
with the PyCrypto library.}

Name:           python-%{srcname}
Version:        3.10.1
Release:        1%{?dist}
Summary:        A self-contained cryptographic library for Python

# PyCrypto-based code is public domain, further PyCryptodome contributions are
# BSD
License:        BSD and Public Domain
URL:            http://www.pycryptodome.org/
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Use external libtomcrypt library
Patch0:         %{name}-3.10.1-use_external_libtomcrypt.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtomcrypt-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Needed for documentation
BuildRequires:  python3dist(sphinx)

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# GMP library is dl-opened
Requires:       gmp%{?_isa}
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{_description}


%package -n python3-%{srcname}-selftest
Summary:        PyCryptodome test suite module
Requires:       python3-%{srcname}%{?_isa}
%py_provides python3-%{srcname}-selftest

%description -n python3-%{srcname}-selftest
%{_description}

This package provides the PyCryptodome test suite module (Cryptodome.SelfTest).


%prep
%autosetup -n pycryptodome-%{version} -p0

# Drop bundled libraries
rm -r src/libtom/

# Remove shebang
sed '1{\@^#! /usr/bin/env python@d}' lib/Crypto/SelfTest/__main__.py >lib/Crypto/SelfTest/__main__.py.new && \
touch -r lib/Crypto/SelfTest/__main__.py lib/Crypto/SelfTest/__main__.py.new && \
mv lib/Crypto/SelfTest/__main__.py.new lib/Crypto/SelfTest/__main__.py


%build
touch .separate_namespace
%py3_build

# Build documentation
%make_build -C Doc/ man SPHINXBUILD=sphinx-build


%install
%py3_install


# Install man pages
install -Dpm 0644 Doc/_build/man/pycryptodome.1 $RPM_BUILD_ROOT%{_mandir}/man1/pycryptodome.1


%check
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}/ %{__python3} setup.py test


%files -n python3-%{srcname}
%doc AUTHORS.rst Changelog.rst README.rst
%license LICENSE.rst
%{python3_sitearch}/Cryptodome/
%exclude %{python3_sitearch}/Cryptodome/SelfTest/
%{python3_sitearch}/%{srcname}-*.egg-info/
%{_mandir}/man1/pycryptodome.1.*


%files -n python3-%{srcname}-selftest
%{python3_sitearch}/Cryptodome/SelfTest/


%changelog
* Tue Feb 09 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.8-1
- Update to 3.9.8

* Fri Jun 05 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.7-3
- Drop python2-pycryptodomex (#1785783)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.9.7-2
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.7-1
- Update to 3.9.7

* Mon Feb 17 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.6-2
- Move test suite module to a separate package (RHBZ #1802989)

* Mon Feb 03 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.6-1
- Update to 3.9.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.4-1
- Update to 3.9.4

* Fri Nov 15 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Fri Nov 15 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.2-1
- Update to 3.9.2
- Spec cleanup

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.2-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.8.1-2
- Readd python2-pycryptodomex (#1672052)

* Fri Apr 05 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Fri Mar 29 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Fri Feb 15 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0
- Use the same .spec file for all supported releases of Fedora and EL

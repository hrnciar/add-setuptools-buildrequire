# Generated by rust2rpm 16
%bcond_without check
%global __cargo_skip_build 0

%global crate sequoia-sq

Name:           rust-%{crate}
Version:        0.25.0
Release:        1%{?dist}
Summary:        Command-line frontends for Sequoia

# Upstream license specification: GPL-2.0-or-later
# https://gitlab.com/sequoia-pgp/sequoia/-/issues/708
License:        GPLv2+
URL:            https://crates.io/crates/sequoia-sq
Source:         %{crates_source}
# Initial patched metadata
# * exclude files that are only useful for upstream development
# * prevent manpages from getting installed twice
Patch0:         sequoia-sq-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Command-line frontends for Sequoia.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or MIT
# BSD
# CC0
# GPLv2+
# LGPLv3 or GPLv2 or GPLv3
# LGPLv3+
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
# MIT or zlib or ASL 2.0
# Unlicense or MIT
# zlib or ASL 2.0 or MIT
License:        GPLv2+ and ASL 2.0 and BSD and CC0 and LGPLv3+ and MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/sq
%{_mandir}/man1/sq*

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# remove integration tests (assert-cli is broken during RPM builds)
rm -r tests
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
# install manual pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav man-sq-net-autocrypt/* %{buildroot}/%{_mandir}/man1/

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.25.0-1
- Initial package

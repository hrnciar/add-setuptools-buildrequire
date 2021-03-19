# Generated by rust2rpm 13
%bcond_without check

%global crate assert_cli

Name:           rust-%{crate}
Version:        0.6.3
Release:        3%{?dist}
Summary:        Test CLI Applications

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/assert_cli
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Test CLI Applications.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR BSL-1.0 (1): ryu
# Apache-2.0 OR MIT (23): serde, libc, backtrace, cfg-if, winapi-i686-pc-windows-gnu, gimli, hermit-abi, winapi-x86_64-pc-windows-gnu, itoa, syn, unicode-xid, winapi, lazy_static, rustc-demangle, serde_json, proc-macro2, quote, assert_cli, object, failure, addr2line, failure_derive, environment
# MIT (6): which, docmatic, atty, synstructure, difference, miniz_oxide
# MPL-2.0 (1): colored
# Zlib (1): adler32
License:        MIT and ASL 2.0 and zlib and MPLv2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/assert_fixture
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test -- --   --skip diff::tests::added_first_line_diff \
                    --skip diff::tests::basic_diff \
                    --skip diff::tests::multiline_diff
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 15:01:01 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.3-1
- Initial package
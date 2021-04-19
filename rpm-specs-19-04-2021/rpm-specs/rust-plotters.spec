# Generated by rust2rpm 13
# disable tests for initial bootstrap cycle with criterion 0.3.2+
%bcond_with check
%global debug_package %{nil}

%global crate plotters

Name:           rust-%{crate}
Version:        0.2.15
Release:        2%{?dist}
Summary:        Rust drawing library with a focus on data plotting

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/plotters
Source:         %{crates_source}
# Initial patched metadata
# * drop windows and WASM dependencies
# * bump font-kit from 0.7 to 0.10
# * bump rusttype from 0.8.2 to 0.9
# * drop optional cairo and piston features
# * drop optional cairo-rs and piston_window deps
Patch0:         plotters-fix-metadata.diff
# * code adaptations for rusttype bump
# https://github.com/38/plotters/commit/687db86
Patch1:         687db86.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust drawing library with a focus on data plotting for both WASM and native
applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+area_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+area_series-devel %{_description}

This package contains library source intended for building other packages
which use "area_series" feature of "%{crate}" crate.

%files       -n %{name}+area_series-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bitmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bitmap-devel %{_description}

This package contains library source intended for building other packages
which use "bitmap" feature of "%{crate}" crate.

%files       -n %{name}+bitmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+boxplot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+boxplot-devel %{_description}

This package contains library source intended for building other packages
which use "boxplot" feature of "%{crate}" crate.

%files       -n %{name}+boxplot-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+candlestick-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+candlestick-devel %{_description}

This package contains library source intended for building other packages
which use "candlestick" feature of "%{crate}" crate.

%files       -n %{name}+candlestick-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages
which use "chrono" feature of "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+datetime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+datetime-devel %{_description}

This package contains library source intended for building other packages
which use "datetime" feature of "%{crate}" crate.

%files       -n %{name}+datetime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deprecated_items-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deprecated_items-devel %{_description}

This package contains library source intended for building other packages
which use "deprecated_items" feature of "%{crate}" crate.

%files       -n %{name}+deprecated_items-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+errorbar-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+errorbar-devel %{_description}

This package contains library source intended for building other packages
which use "errorbar" feature of "%{crate}" crate.

%files       -n %{name}+errorbar-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+evcxr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+evcxr-devel %{_description}

This package contains library source intended for building other packages
which use "evcxr" feature of "%{crate}" crate.

%files       -n %{name}+evcxr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+font-kit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+font-kit-devel %{_description}

This package contains library source intended for building other packages
which use "font-kit" feature of "%{crate}" crate.

%files       -n %{name}+font-kit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gif-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gif-devel %{_description}

This package contains library source intended for building other packages
which use "gif" feature of "%{crate}" crate.

%files       -n %{name}+gif-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gif_backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gif_backend-devel %{_description}

This package contains library source intended for building other packages
which use "gif_backend" feature of "%{crate}" crate.

%files       -n %{name}+gif_backend-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+histogram-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+histogram-devel %{_description}

This package contains library source intended for building other packages
which use "histogram" feature of "%{crate}" crate.

%files       -n %{name}+histogram-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+image-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+image-devel %{_description}

This package contains library source intended for building other packages
which use "image" feature of "%{crate}" crate.

%files       -n %{name}+image-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+image_encoder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+image_encoder-devel %{_description}

This package contains library source intended for building other packages
which use "image_encoder" feature of "%{crate}" crate.

%files       -n %{name}+image_encoder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+line_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+line_series-devel %{_description}

This package contains library source intended for building other packages
which use "line_series" feature of "%{crate}" crate.

%files       -n %{name}+line_series-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+palette-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+palette-devel %{_description}

This package contains library source intended for building other packages
which use "palette" feature of "%{crate}" crate.

%files       -n %{name}+palette-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+palette_ext-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+palette_ext-devel %{_description}

This package contains library source intended for building other packages
which use "palette_ext" feature of "%{crate}" crate.

%files       -n %{name}+palette_ext-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+point_series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+point_series-devel %{_description}

This package contains library source intended for building other packages
which use "point_series" feature of "%{crate}" crate.

%files       -n %{name}+point_series-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rusttype-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rusttype-devel %{_description}

This package contains library source intended for building other packages
which use "rusttype" feature of "%{crate}" crate.

%files       -n %{name}+rusttype-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+svg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+svg-devel %{_description}

This package contains library source intended for building other packages
which use "svg" feature of "%{crate}" crate.

%files       -n %{name}+svg-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ttf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ttf-devel %{_description}

This package contains library source intended for building other packages
which use "ttf" feature of "%{crate}" crate.

%files       -n %{name}+ttf-devel
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
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.15-1
- Initial package

# Generated by rust2rpm 13 + a lot of manual work
%bcond_without check
%global __cargo_skip_build 0

Name:           zola
Version:        0.12.2
Release:        3%{?dist}
Summary:        Fast static site generator with everything built-in

# Upstream license specification: MIT
# (MIT or ASL 2.0) and Public Domain
# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or Boost
# BSD
# CC0
# ISC
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
# MIT or BSD
# MIT or zlib or ASL 2.0
# Unlicense or MIT
# zlib
# zlib or ASL 2.0 or MIT
License:        MIT and ASL 2.0 and BSD and CC0 and ISC and MIT and Public Domain and zlib
URL:            https://www.getzola.org/
Source:         https://github.com/getzola/zola/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

# src/cmd/livereload.js
Provides:       bundled(js-livereload-js) = 3.2.4
# components/search/src/elasticlunr.min.js
Provides:       bundled(js-elasticlunr-js) = 0.9.5

%description
%{summary}.

%prep
%autosetup -p1
# https://bugzilla.redhat.com/show_bug.cgi?id=1723064
%if 0%{?__isa_bits} == 32
sed -i -e '/lto/d' Cargo.toml
%endif
# https://github.com/getzola/zola/commit/92282608fead107c998e29a104ceb763a44c2ab8
find -type f -name 'Cargo.toml' -exec sed -i -e '/mockito/s/= "0.27"/= "0.28"/' {} +
# https://github.com/getzola/zola/commit/a903473a87239213e8656aad8d6de075d04ff169
sed -i -e 's/, "rustls-tls"//' components/{link_checker,templates}/Cargo.toml
%cargo_prep

%generate_buildrequires
# HACK
for f in Cargo.toml components/*/Cargo.toml; do
  cd $(dirname $f)
  sed -i.br -r -e '/=\s*\{[^}]+path\s*=/d' Cargo.toml
  %cargo_generate_buildrequires
  mv -f Cargo.toml{.br,}
  cd - >/dev/null
done

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  completions/zola.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  completions/zola.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  completions/_zola

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/zola
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zola.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/zola.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_zola

%changelog
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:34:37 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.2-2
- Rebuild

* Mon Sep 28 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Fri May 08 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Wed Apr 22 2020 Josh Stone <jistone@redhat.com> - 0.10.0-2
- Bump to syntect 4

* Mon Feb 17 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 10:45:44 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Fri Sep 13 19:18:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-5
- Bump ammonia to 3.0.0
- Bump pulldown-cmark to 0.6
- Bump image to 0.22

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 18:29:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-3
- Correct fish completions directory

* Mon Jun 24 13:09:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-2
- Update toml to 0.5
- Bring 32bit packages back, but without LTO

* Sat Jun 22 14:24:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Initial package

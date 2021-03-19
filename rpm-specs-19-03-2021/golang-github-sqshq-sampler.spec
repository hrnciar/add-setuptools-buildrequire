# Generated by go2rpm 1
%bcond_without check

# https://github.com/sqshq/sampler
%global goipath         github.com/sqshq/sampler
Version:                1.1.0

%gometa

%global godevelheader %{expand:
Requires:       pkgconfig(alsa)}

%global common_description %{expand:
Tool for shell commands execution, visualization and alerting. Configured with
a simple YAML file.}

%global golicenses      LICENSE.md
%global godocs          README.md example.yml example-fedora.yml

Name:           %{goname}
Release:        6%{?dist}
Summary:        Tool for shell commands execution, visualization and alerting

License:        GPLv3
# FIXME: Upstream uses unknown SPDX tag GPL-3.0-only!
URL:            %{gourl}
Source0:        %{gosource}
Source1:        example-fedora.yml
# Compatibility with github.com/hajimehoshi/oto 0.6.x (upstreamed)
Patch0:         0001-asset-player.go-Replace-NewPlayer-with-NewContext.patch

BuildRequires:  golang(github.com/gizak/termui/v3)
BuildRequires:  golang(github.com/hajimehoshi/go-mp3)
BuildRequires:  golang(github.com/hajimehoshi/oto)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/lunixbochs/vtclean)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/mbndr/figlet4go)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  pkgconfig(alsa)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/sampler %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0644 -Dp %{SOURCE1}          %{buildroot}%{_docdir}/%{name}/example-fedora.yml

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 00:00:00 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-2
- Remove unnecessary BR
- Remove Exclude s390x arch
- Fix date format in spec

* Fri Dec 27 00:00:00 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Oct 14 00:00:00 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-4
- Exclude s390x arch

* Sat Oct 05 04:49:18 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-3
- Initial package

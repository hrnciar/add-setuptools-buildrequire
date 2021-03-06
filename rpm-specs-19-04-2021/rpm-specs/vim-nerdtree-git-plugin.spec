%global commit      f522a091e2838812d2669c331d7e9c283db6d54d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191024

Name:           vim-nerdtree-git-plugin
Version:        0
Release:        4.%{date}git%{shortcommit}%{?dist}
Summary:        Plugin of NERDTree showing git status

License:        WTFPL
URL:            https://github.com/xuyuanp/nerdtree-git-plugin
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem
Requires:       vim-enhanced
Requires:       vim-nerdtree

%description
A plugin of NERDTree showing git status flags. Works with the LATEST version of
NERDTree.


%prep
%autosetup -n nerdtree-git-plugin-%{commit} -p1


%install
mkdir -p                %{buildroot}%{vimfiles_root}
cp -r nerdtree_plugin   %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md
%{vimfiles_root}/nerdtree_plugin/*
%{_metainfodir}/*.xml


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20191024gitf522a09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20191024gitf522a09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20191024gitf522a09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20191024gitf522a09
- Update to latesti git snapshot
- Add license file

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190613git0501cdf
- Initial package

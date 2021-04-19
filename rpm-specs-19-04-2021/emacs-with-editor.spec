%global pkg with-editor
%global pkgname With-Editor

Name:           emacs-%{pkg}
Version:        3.0.2
Release:        2%{?dist}
Summary:        Use Emacsclient as the editor of child processes
License:        GPLv3+
URL:            https://github.com/magit/with-editor
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make texinfo texinfo-tex
BuildRequires:  emacs-dash >= 2.13
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash >= 2.13

%description
%{pkgname} makes it possible to reliably use the Emacsclient as the editor
of child processes.

%prep
%autosetup -n %{pkg}-%{version}

%build
%make_build

%install
# With-Editor doesn't provide an install target.
install -D -p -m 644 %{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  %{pkg}-autoloads.el %{pkg}.el %{pkg}.elc

%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 3.0.2-1
- Initial packaging

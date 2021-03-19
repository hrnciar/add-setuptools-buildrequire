%global pkg transient
%global pkgname Transient

%global commit 8ad5fb83c458801816fc2f888c43f6baf74b5803
%global commitdate 20210117
%global shortcommit %(c=%{commit}; echo ${c:0:9})

Name:           emacs-%{pkg}
Version:        0.2.0
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Emacs transient key maps
License:        GPLv3+
URL:            https://github.com/magit/transient
Source0:        %{url}/archive/%{commit}/%{pkg}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make texinfo texinfo-tex
Requires:       emacs(bin) >= %{_emacs_version}

%description
%{pkgname} provides transient key maps involving a prefix command, infix
arguments and suffix commands.

%prep
%autosetup -n %{pkg}-%{commit}

%build
%make_build lisp info

%install
# Transient doesn't provide an install target.
install -D -p -m 644 docs/%{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  lisp/%{pkg}-autoloads.el lisp/%{pkg}.el lisp/%{pkg}.elc

%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3.20210117git8ad5fb83c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.2.0-2.20210117git8ad5fb83c
- Update to a recent commit.

* Mon Nov 09 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 0.2.0-1
- Initial packaging

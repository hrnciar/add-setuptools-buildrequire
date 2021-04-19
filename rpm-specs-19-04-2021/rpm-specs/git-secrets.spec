Name:           git-secrets
Version:        1.3.0
Release:        4%{?dist}
Summary:        Prevents committing secrets and credentials into git repos

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}/
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  git-core
BuildRequires:  make

Requires:       git-core


%description
git-secrets scans commits, commit messages, and --no-ff merges to prevent
adding secrets into your git repositories. If a commit, commit message, or any
commit in a --no-ff merge history matches one of your configured prohibited
regular expression patterns, then the commit is rejected.


%prep
%autosetup


%build
%make_build PREFIX=%{_prefix}


%install
%make_install PREFIX=%{_prefix}


%check
make test


%files
%license LICENSE.txt
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 10:00:15 CET 2020 K. de Jong <keesdejong@fedoraproject.org> - 1.3.0-3
- Updated spec file
- Added make build requirement

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Nov 21 2019 K. de Jong <keesdejong@fedoraproject.org> - 1.3.0-1
- Initial package 

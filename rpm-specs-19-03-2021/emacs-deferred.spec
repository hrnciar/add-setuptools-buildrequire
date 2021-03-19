%global pkg deferred

Name:           emacs-%{pkg}
Version:        0.5.1
Release:        2%{?dist}
Summary:        Simple asynchronous functions for Emacs Lisp

License:        GPLv3+
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
deferred.el provides facilities to manage asynchronous tasks.

concurrent.el is a higher level library for asynchronous tasks, based on
deferred.el.
It is inspired by libraries of other environments and concurrent programming
models. It has following facilities: pseud-thread, generator, semaphore,
dataflow variables and event management.


%prep
%autosetup


%build
for i in *.el; do
    %{_emacs_bytecompile} $i
done


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc README.markdown README-concurrent.markdown
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-1
- Initial RPM release

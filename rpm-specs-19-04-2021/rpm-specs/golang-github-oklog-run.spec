# Generated by go2rpm
%bcond_without check

# https://github.com/oklog/run
%global goipath         github.com/oklog/run
Version:                1.1.0

%gometa

%global common_description %{expand:
run.Group is a universal mechanism to manage goroutine lifecycles.

Create a zero-value run.Group, and then add actors to it. Actors are defined as
a pair of functions: an execute function, which should run synchronously; and an
interrupt function, which, when invoked, should cause the execute function to
return. Finally, invoke Run, which concurrently runs all of the actors, waits
until the first actor exits, invokes the interrupt functions, and finally
returns control to the caller only once all actors have returned. This
general-purpose API allows callers to model pretty much any runnable task, and
achieve well-defined lifecycle semantics for the group.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Universal mechanism to manage goroutine lifecycles

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Nathan Scott <nathans@redhat.com> - 1.1.0-1
- Release 1.1.0 (#1788996)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 20:53:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Mon Mar 18 2019 Nathan Scott <nathans@redhat.com> - 1.0.0-1
- First package for Fedora
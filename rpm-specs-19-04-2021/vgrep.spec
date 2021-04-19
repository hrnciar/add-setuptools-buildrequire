# https://github.com/vrothberg/vgrep
%global goipath         github.com/vrothberg/vgrep
Version:                2.5.1

%gometa

%global common_description %{expand:
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.}

%global golicenses      LICENSE
%global godocs          README.md

%bcond_without check

Name:           vgrep
Release:        2%{?dist}
Summary:        User-friendly pager for grep
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/nightlyone/lockfile)
BuildRequires:  golang(github.com/peterh/liner)
BuildRequires:  golang(github.com/sirupsen/logrus)

BuildRequires:  go-md2man

%description
%{common_description}

%gopkg

%prep
%goprep

%build
export LDFLAGS="-X main.version=%{version} "
%gobuild -o %{gobuilddir}/bin/vgrep %{goipath}
go-md2man -in docs/vgrep.1.md -out docs/vgrep.1

%install
%gopkginstall
install -D -p -m 0755 %{gobuilddir}/bin/vgrep %{buildroot}%{_bindir}/vgrep
install -D -p -m 0644 docs/vgrep.1 %{buildroot}%{_mandir}/man1/vgrep.1

%if %{with check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/vgrep
%{_mandir}/man1/vgrep.1*

%gopkgfiles

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 12:50:39 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.1-1
- Update to 2.5.1
- Close: rhbz#1897608

* Sun Nov 01 2020 Carl George <carl@george.computer> - 2.5.0-1
- Latest upstream
- Include man page

* Tue Aug 18 2020 Carl George <carl@george.computer> - 2.4.0-1
- Latest upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Carl George <carl@george.computer> - 2.3.3-1
- Latest upstream

* Wed Jul 01 2020 Carl George <carl@george.computer> - 2.3.1-2
- Embed version into binary

* Mon Jun 29 2020 Carl George <carl@george.computer> - 2.3.1-1
- Initial package

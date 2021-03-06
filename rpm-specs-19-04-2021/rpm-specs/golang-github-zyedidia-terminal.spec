# Generated by go2rpm
%bcond_without check

# https://github.com/zyedidia/terminal
%global goipath         github.com/zyedidia/terminal
%global commit          533c623e241584694ef5438ff56fa66a8b71d8db

%gometa

%global common_description %{expand:
Package Terminal is a vt10x terminal emulation backend, influenced largely by
st, rxvt, xterm, and iTerm as reference. Use it for terminal muxing, a terminal
emulation frontend, or wherever else you need terminal emulation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.12%{?dist}
Summary:        Vt10x terminal emulation backend

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/nsf/termbox-go)
BuildRequires:  golang(github.com/zyedidia/pty)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 17:15:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20190523git533c623
- Bump to commit 533c623e241584694ef5438ff56fa66a8b71d8db

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git1760577
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.6.git1760577
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git1760577
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git1760577
- Replace original "j4k.co/terminal" with the fork

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git1760577
- Replace forked dependency with original one

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180314git1760577
- Update with the new Go packaging

* Fri Jan 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180125git1760577
- Initial package for Fedora

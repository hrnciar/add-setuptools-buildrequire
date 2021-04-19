%global codate 20210414
%global commit 4b7d16dc41fee40989911a8274fd071eccd7fb89
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name:           edid-decode
Version:        0
Release:        7.%{codate}git%{shortcommit}%{?dist}
Summary:        Decode EDID data in human-readable format

License:        MIT
URL:            https://git.linuxtv.org/edid-decode.git/
Source0:        edid-decode-%{shortcommit}.tar.xz
Source1:        edid-decode-snapshot.sh

BuildRequires:  gcc-c++ make

Conflicts:	xorg-x11-utils < 7.5-33

%description
Decodes raw monitor EDID data in human-readable format.


%prep
%setup -q -n %{name}


%build
%set_build_flags
%make_build


%install
%make_install


%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Wed Apr 14 2021 Yanko Kaneti <yaneti@declera.com> - 0-7.2020414git4b7d16dc
- New snapshot.

* Sun Mar 14 2021 Yanko Kaneti <yaneti@declera.com> - 0-7.2020314git083d0480
- New snapshot.

* Sun Feb 28 2021 Yanko Kaneti <yaneti@declera.com> - 0-7.2020228gitf40dfc04
- New snapshot.

* Mon Feb 15 2021 Yanko Kaneti <yaneti@declera.com> - 0-7.2020215gitaf996e63
- New snapshot. New timings options

* Thu Feb 11 2021 Yanko Kaneti <yaneti@declera.com> - 0-6.2020211gitf78149a5
- New snapshot.

* Thu Jan 28 2021 Yanko Kaneti <yaneti@declera.com> - 0-6.2020128git526a72d9
- New snapshot.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20201125git8a370df2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Yanko Kaneti <yaneti@declera.com> - 0-6.20201125git8a370df2
- New snapshot.

* Tue Sep  8 2020 Yanko Kaneti <yaneti@declera.com> - 0-6.20200908git3265be5a
- New snapshot.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20200717git4ee445ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Yanko Kaneti <yaneti@declera.com> - 0-5.20200717git4ee445ea
- New snapshot.

* Mon May 18 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200518git18895047
- New snapshot.

* Thu Mar  5 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200305git68a38bae
- New snapshot. Bugfixes

* Sun Feb 16 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200216git9bdf5552
- New snapshot. Major cleanups

* Tue Feb 11 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200211gitc5b275a6
- New snapshot. Add some more timings formats

* Mon Feb 10 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200210git9f6bb734
- New snapshot. Support Dobly Vision Data Block, CTA Data Blocks in DisplayID

* Mon Feb  3 2020 Yanko Kaneti <yaneti@declera.com> - 0-4.20200203gitc29b9433
- New snapshot. Support  DisplayID 2.0 VESA VSDB

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20200127gita6b199e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Yanko Kaneti <yaneti@declera.com> - 0-3.20200127gita6b199e9
- New snapshot

* Mon Jan 20 2020 Yanko Kaneti <yaneti@declera.com> - 0-3.20200120gitc42616dd
- New snapshot. Adds support for DTCDB and DDDB

* Thu Dec 12 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191212gite719d040
- New snapshot. Add license

* Mon Dec  2 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191202git5dc6e53a
- New snapshot. Switch to C++

* Mon Nov 25 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191125git7bbed3ae
- New snapshot.

* Sat Nov 23 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191123git8108c45f
- New snapshot.

* Thu Nov 21 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191121git8b50301f
- New snapshot.

* Wed Nov 13 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191113gitcc5a7bf9
- New snapshot. Bugfixes.

* Thu Oct 31 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191031git3a6108a7
- New snapshot. Improve DisplayID 1.2/3 parsing

* Fri Oct 18 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191018gitdc8afbf7
- New snapshot. Adds support for HDMI 2.1 Amendment A1 and HDR10+

* Tue Oct  1 2019 Yanko Kaneti <yaneti@declera.com> - 0-3.20191001git7d26052f
- New snapshot

* Thu Sep 26 2019 Yanko Kaneti <yaneti@declera.com> - 0-1.20190926git7696439d
- New snapshot
- Use make_build

* Thu Sep 26 2019 Yanko Kaneti <yaneti@declera.com> - 0-2.20190820git0932deee
- Add Conflicts with xorg-x11-utils < 7.5-33

* Tue Aug 20 2019 Yanko Kaneti <yaneti@declera.com> - 0-1.20190820git0932deee
- Split from xorg-x11-utils

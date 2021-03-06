%global appname pytelegrambotapi
%global richname pyTelegramBotAPI

%global appsum Python Telegram bot API
%global appdesc A simple, but extensible Python implementation for the Telegram Bot API

Name: python-%{appname}
Version: 3.7.7
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv2+
URL: https://github.com/eternnoir/%{richname}
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(requests)
BuildRequires: python3dist(wheel)
BuildRequires: python3dist(six)

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{richname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%license LICENSE
%doc README.md
%{python3_sitelib}/telebot/
%{python3_sitelib}/%{richname}-*.egg-info/

%changelog
* Fri Apr 02 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.7-1
- Updated to version 3.7.7.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.6-1
- Updated to version 3.7.6.

* Fri Jan 08 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.5-1
- Updated to version 3.7.5.

* Sat Nov 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.4-1
- Updated to version 3.7.4.

* Tue Aug 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.3-1
- Updated to version 3.7.3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.2-1
- Updated to version 3.7.2.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.7-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.6.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.7-1
- Updated to version 3.6.7.

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.6.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.6.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.6-1
- Updated to version 3.6.6.

* Sat Aug 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.5-1
- Updated to version 3.6.5.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.4-1
- Updated to version 3.6.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-3
- Fixed build under Python 3.7.

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.7

* Tue May 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-1
- Updated to version 3.6.3.

* Sat Mar 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.2-1
- Updated to version 3.6.2.

* Mon Mar 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.1-1
- Updated to version 3.6.1.

* Fri Mar 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.0-1
- Updated to version 3.6.0.

* Sat Feb 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.2-1
- Updated to version 3.5.2.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.1-1
- Updated to version 3.5.1.

* Wed Aug 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-2
- Small SPEC fixes.

* Tue Aug 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Initial SPEC release.

Name:           trelby
Version:        2.4.2
Release:        1%{?dist}
Summary:        The free, multiplatform, feature-rich screenwriting program

License:        GPLv2 and GPLv3+
URL:            https://github.com/limburgher/trelby
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wxpython4
BuildRequires:  python3-lxml
BuildRequires:  docbook-style-xsl
BuildRequires:  make
Requires:       python3-wxpython4
Requires:       python3-lxml
Requires:       hicolor-icon-theme

%description
Trelby is simple, fast and elegantly laid out to make
screenwriting simple. It is infinitely configurable.

%prep
%setup -q

sed -i "s|src|%{python3_sitelib}/trelby/src|g" bin/trelby

%build
make dist
%{__python3} setup.py build
rm -rf doc/.gitignore

%install
%{__python3} setup.py install --prefix=%{_prefix} \
    --install-lib=%{python3_sitelib}/trelby \
    --install-data=%{_datadir} \
    --skip-build \
    --root $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/trelby/resources
ln -s %{python3_sitelib}/trelby/resources/icon256.png $RPM_BUILD_ROOT%{_datadir}/trelby/resources/icon256.png

desktop-file-validate %{buildroot}/%{_datadir}/applications/trelby.desktop

%check
make test

%files
%license LICENSE
%doc fileformat.txt README.md manual.html
%{_bindir}/*
%{_datadir}/trelby/resources
%{_datadir}/applications/trelby.desktop
%{python3_sitelib}/trelby*
%{_mandir}/man1/trelby.1.gz

%changelog
* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.2-1
- Fix license tag, validate desktop file, move to unittest.mock.

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-2
- Use macro for prefix.

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4.1-1
- 2.4.1

* Mon Feb 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.4-3
- Fix man page, manual, tests, 2.4 final.

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-2
- Fix for title page editing.

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.4-1
- Python3

* Fri Mar 16 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.3-0.dev
- First build.

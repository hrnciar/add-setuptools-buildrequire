# Upstream has not made a new release since 2016, but has made lots of
# improvements in git.
%global srcname iedit
%global commit  0d6d2387188763a88cdf84f749e6f32d5a72bbd6
%global date    20210202
%global forgeurl https://github.com/victorhge/iedit

Name:           emacs-%{srcname}
Version:        0.9.9.9
Release:        1%{?dist}
Summary:        Edit multiple regions simultaneously in Emacs

%forgemeta

License:        GPLv3+
URL:            https://www.emacswiki.org/emacs/Iedit
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  emacs
BuildRequires:  make

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
This package includes Emacs minor modes (iedit-mode and
iedit-rectangle-mode) based on an API library (iedit-lib) and allows you
to alter one occurrence of some text in a buffer (possibly narrowed) or
region, and simultaneously have other occurrences changed in the same
way, with visual feedback as you type.

iedit-mode is a great alternative to built-in replace commands:

- A more intuitive way to alter all the occurrences at once
- Visual feedback
- Fewer keystrokes in most cases
- Optionally preserve case

%prep
%forgesetup

# Fix permissions
chmod 0644 iedit-demo.gif

%build
%make_build

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{srcname}
install -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/%{srcname}

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/%{srcname}/iedit-autoloads.el \
  %{buildroot}%{_emacs_sitestartdir}

%files
%doc README.org iedit-demo.gif
%{_emacs_sitelispdir}/%{srcname}/
%{_emacs_sitestartdir}/iedit-autoloads.el

%changelog
* Wed Mar 10 2021 Jerry James <loganjerry@gmail.com> - 0.9.9.9-1.20210202git0d6d238
- Initial RPM

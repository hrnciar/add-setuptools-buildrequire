%global extdir		caffeine@patapon.info
%global gschemadir	%{_datadir}/glib-2.0/schemas

Name:		gnome-shell-extension-caffeine
Version:	37
Release:	2%{?dist}
Summary:	Disable the screen saver and auto suspend in gnome shell

License:	GPLv2
URL:		https://github.com/eonpatapon/gnome-shell-extension-caffeine
Source0:	https://github.com/eonpatapon/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas

Requires:	gnome-shell-extension-common

%description
This extension allows the user to easily disable the screen saver and auto
suspend in gnome shell via an icon in the top bar. By default, this function
is also enabled if a full screen application is running, and can be configured
to disable gnome shell's night light as well.

%prep
%autosetup

%build
./update-locale.sh
glib-compile-schemas --strict --targetdir=%{extdir}/schemas/ %{extdir}/schemas

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -ar %{extdir} %{buildroot}%{_datadir}/gnome-shell/extensions/%{extdir}
%find_lang %{name} --all-name

# Fedora and EPEL 8 handles post scripts via triggers
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif

%files -f %{name}.lang
%license COPYING
%{_datadir}/gnome-shell/extensions/%{extdir}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 37-1
- Initial package

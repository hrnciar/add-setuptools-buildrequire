Name: sweet-gtk-theme
Summary: Light and dark, colorful GTK+ theme
License: GPLv3

%global git_repo   Sweet
%global git_url    https://github.com/EliverLara/%{git_repo}
%global git_commit a164141483adb83420ec1c0701aa0b0bab65afa2
%global git_date   20201025

%global git_commit_short %(c="%{git_commit}"; echo "${c:0:8}")

Version: 1.10.5
Release: 5.%{git_date}git%{git_commit_short}%{?dist}

URL: https://www.gnome-look.org/p/1253385/
Source0: %{git_url}/archive/%{git_commit}/%{git_repo}-%{git_commit}.tar.gz

BuildArch: noarch

BuildRequires: sassc

Recommends: candy-icon-theme


%description
Sweet is a light and dark, colorful GTK+ theme that can be used with
Gnome Shell, Cinnamon, Metacity, xfwm4, and other window managers.

Sweet works great when used together with the Candy icon theme.


%prep
%setup -q -n %{git_repo}-%{git_commit}

# Remove executable bits from everything that's not a shell/python script
find ./ -type f -executable \
	'!' '(' -name '*.sh' -o -name '*.fish' -o -name '*.py' ')' \
	-exec chmod --verbose a-x '{}' '+'


%build
# Upstream uses Gulp for building, but it is not available in Fedora.
# The Gulpfile takes care of compiling SASS files, but not much else.
# ...so let's just do that ourselves!
for FILE in \
	gtk-3.0/gtk gtk-3.0/gtk-dark \
	gnome-shell/gnome-shell \
	cinnamon/cinnamon cinnamon/cinnamon-dark \
; do
	SCSS_DIR="$(dirname "${FILE}")"
	SCSS_SOURCE="$(basename "${FILE}").scss"
	SCSS_TARGET="${SCSS_SOURCE/scss/css}"
	
	pushd "${SCSS_DIR}"
	sassc --style=compressed "${SCSS_SOURCE}" "${SCSS_TARGET}"
	popd
done


%install
THEME_DIR="%{buildroot}%{_datadir}/themes/Sweet"
install -m 755 -d "${THEME_DIR}"
for FILE in assets cinnamon gnome-shell gtk-2.0 gtk-3.0 metacity-1 xfwm4 index.theme; do
	cp -a "${FILE}" "${THEME_DIR}/${FILE}"
done

# Remove all SCSS source files
# and any executable files that we might have installed by accident
pushd "${THEME_DIR}"
find ./ -name '*.scss' -exec rm --verbose '{}' '+'
find ./ -type f -executable -exec rm --verbose '{}' '+'
popd


%files
%license LICENSE
%{_datadir}/themes/Sweet


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-5.20201025gita1641414
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-4.20201025gita1641414
- Update to latest git snapshot

* Mon Oct 12 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-3.20201004gite3ee1783
- Update to latest git snapshot (now with support for Cinnamon)

* Sat Sep 19 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.5-2.20200913git10aefff0
- Update to latest git snapshot
- Do not re-render the assets during build
- Remove SCSS sources from the final install

* Sun Dec 01 2019 Artur Iwicki <fedora@svgames.pl> - 1.10.5-1.20191118gitb8e8b7d7
- Initial packaging

Name: sweet-gtk-theme
Summary: Light and dark, colorful GTK+ theme
License: GPLv3
URL: https://www.gnome-look.org/p/1253385/

%global git_date_master 20210227
%global git_commit_master 095ba407ca19ae0dd4800aeb733245d27cb8525e

%global git_date_ambar 20210227
%global git_commit_ambar 70fb8ee34145ecfd8a6e3dc6171a395dd5616674

%global git_date_ambar_blue 20210326
%global git_commit_ambar_blue 7931221099b41b931d36807c5ff3fbb3ef39fb25

%global git_date_mars 20210326
%global git_commit_mars eb4782f09e2d59f5db9439c28080c03f06f83d1a

%global git_date_nova 20210402
%global git_commit_nova c59cc1ff37f8f523f101c93e1b8f1f9b6866398b

%global git_date %( \
	( \
		echo '%{git_date_master}'; \
		echo '%{git_date_ambar}'; \
		echo '%{git_date_ambar_blue}'; \
		echo '%{git_date_mars}'; \
		echo '%{git_date_nova}'; \
	) | sort -rn | head -n1)

Version: 2.0
Release: 1.%{git_date}%{?dist}

%global repo_name  Sweet
%global repo_url   https://github.com/EliverLara/%{repo_name}

Source0: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Master-%{git_commit_master}.tar.gz
Source1: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Ambar-%{git_commit_ambar}.tar.gz
Source2: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Ambar-Blue-%{git_commit_ambar_blue}.tar.gz
Source3: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Mars-%{git_commit_mars}.tar.gz
Source4: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Nova-%{git_commit_nova}.tar.gz
Source99: get-sweet-sources.sh

BuildArch: noarch

BuildRequires: sassc

Recommends: candy-icon-theme


%description
Sweet is a light and dark, colorful GTK+ theme that can be used with
Gnome Shell, Cinnamon, Metacity, xfwm4, and other window managers.

Sweet works great when used together with the Candy icon theme.


%prep
%setup -q -c %{repo_name}-%{version} -T -a 0
%setup -q -c %{repo_name}-%{version} -T -D -a 1
%setup -q -c %{repo_name}-%{version} -T -D -a 2
%setup -q -c %{repo_name}-%{version} -T -D -a 3
%setup -q -c %{repo_name}-%{version} -T -D -a 4

# Rename the directories from "repo-commit" to "branch"
mv "%{repo_name}-%{git_commit_master}" master
mv "%{repo_name}-%{git_commit_ambar}" ambar
mv "%{repo_name}-%{git_commit_ambar_blue}" ambar-blue
mv "%{repo_name}-%{git_commit_mars}" mars
mv "%{repo_name}-%{git_commit_nova}" nova

# Remove executable bits from everything that's not a shell/python script
find ./ -type f -executable \
	'!' '(' -name '*.sh' -o -name '*.fish' -o -name '*.py' ')' \
	-exec chmod --verbose a-x '{}' '+'


%build
# Upstream uses Gulp for building, but it is not available in Fedora.
# The Gulpfile takes care of compiling SASS files, but not much else.
# ...so let's just do that ourselves!
for VARIANT in master ambar ambar-blue mars nova; do
	pushd "${VARIANT}"
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
	popd
done


%install
for VARIANT in master ambar ambar-blue mars nova; do
	THEME_DIR="%{buildroot}%{_datadir}/themes/Sweet-${VARIANT}"
	install -m 755 -d "${THEME_DIR}"

	pushd "${VARIANT}"
	for FILE in assets cinnamon gnome-shell gtk-2.0 gtk-3.0 metacity-1 xfwm4 index.theme; do
		cp -a "${FILE}" "${THEME_DIR}/${FILE}"
	done
	popd

	# Remove all SCSS source files
	# and any executable files that we might have installed by accident
	pushd "${THEME_DIR}"
	find ./ -name '*.scss' -exec rm --verbose '{}' '+'
	find ./ -type f -executable -exec rm --verbose '{}' '+'
	popd
done

# Rename "master" to "classic"
mv "%{buildroot}%{_datadir}/themes/Sweet-master" "%{buildroot}%{_datadir}/themes/Sweet-classic"


%files
%license master/LICENSE
%{_datadir}/themes/Sweet-classic
%{_datadir}/themes/Sweet-ambar
%{_datadir}/themes/Sweet-ambar-blue
%{_datadir}/themes/Sweet-mars
%{_datadir}/themes/Sweet-nova


%changelog
* Mon Apr 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0-1.20210402
- Update to v2.0
- Include color variants

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

# This spec file has been automatically updated
Version:        30
Release: 1%{?dist}
#
# Copyright (C) 2017-2020 Red Hat, Inc.
#
# Cockpit is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# Cockpit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Cockpit; If not, see <http://www.gnu.org/licenses/>.
#

Name:           cockpit-podman
Summary:        Cockpit component for Podman containers
License:        LGPLv2+
URL:            https://github.com/cockpit-project/cockpit-podman

Source0:        https://github.com/cockpit-project/cockpit-podman/releases/download/%{version}/cockpit-podman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       cockpit-bridge >= 138
Requires:       podman >= 2.0.4

%description
The Cockpit user interface for Podman containers.

%prep
%setup -q -n cockpit-podman

%build
# Nothing to build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LICENSE.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
* Wed Apr 14 2021 Matej Marusak <mmarusak@redhat.com> - 30-1

- Translation updates
- PatternFly 4 updates
- Fix crash with "Used Images" links

* Fri Feb 19 2021 Martin Pitt <martin@piware.de> - 29-1

- PatternFly 4 updates for a more consistent UI
- Accessibility fixes
- Add FMF tests for sharing tests with up- and downstream

* Thu Feb 11 2021 Matej Marusak <mmarusak@redhat.com> - 28.1-1

- Improve tests to be more robust against unstable Podman API

* Thu Feb 04 2021 Matej Marusak <mmarusak@redhat.com> - 28-1

- Drop cockpit-system dependency
- Correctly show selected option for SELinux labels

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27.1-1

- test: Drop forgotten sit() to make tests work in gating

* Thu Jan 07 2021 Matej Marusak <mmarusak@redhat.com> - 27-1

- images: Indicate that force deletion is in progress
- images: Fix handling of errors on pull
- Use packaged sassc instead of node-sass
- tests: Adjust to new Podman versions and robustify them

* Wed Dec 09 2020 Marius Vollmer <mvollmer@redhat.com> - 26-1
- run: Make hostPort optional
- run: Enable setting up IP address for exposed ports

* Wed Oct 14 2020 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 25-1

- Listen for image build event

* Wed Sep 30 2020 Marius Vollmer <mvollmer@redhat.com> - 24-1

- Use sentence case in the UI

* Wed Sep 02 2020 Martin Pitt <martin@piware.de> - 23-1

- Translation updates

* Wed Aug 19 2020 Marius Vollmer <mvollmer@redhat.com> - 22-1

- Support for pod group deletion

* Wed Aug 05 2020 Matej Marusak <mmarusak@redhat.com> - 21-1

- Support for pod groups
- Support checkpoint and restore
- Registry selection in "download image" dialog
- Selected tag removal during deletion

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Katerina Koukiou <kkoukiou@redhat.com> - 20-1

- Show networking information for containers
- Enable filtering images and containers by owner
- Optionally show intermediate images
- Enable setting up SELinux label when mounting volumes

* Wed Jul 15 2020 Matej Marusak <mmarusak@redhat.com> - 19-1

- Switch to the new Podman REST API
- Improve displaying on small screens

* Mon Jun 15 2020 Matej Marusak <mmarusak@redhat.com> - 18-1

- Bump NPM dependencies to their latest versions
- Stop importing cockpit's deprecated base1/patternfly.css
- Synchronize style with the newest Cockpit

* Thu May 14 2020 Matej Marusak <mmarusak@redhat.com> - 17-1

- Translation updates
- Adjust tests to changed Services page in Cockpit 218

* Wed Apr 29 2020 Martin Pitt <martin@piware.de> - 16-1

- Restyle buttons and dropdowns to be consistent with Cockpit
- Disable button and show a spinner while delete operation is in progress
- Translation updates

* Thu Apr 16 2020 Martin Pitt <martin@piware.de> - 15-3

- Drop obsolete functionality for Fedora Atomic
- Localize dates and times
- Make tests non-destructive, to support Fedora gating

* Wed Mar 04 2020 Martin Pitt <martin@piware.de> - 14-1

- Fix crash on filtering anonymous images
- Translation updates

* Wed Feb 05 2020 sanne raymaekers <sanne.raymaekers@gmail.com> - 13-1

- Show historical logs

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Katerina Koukiou <kkoukiou@redhat.com> - 12-1

- Configure CPU share for system containers

* Wed Nov 27 2019 Martin Pitt <martin@piware.de> - 11-1

- Fix Alert notification in Image Search Modal
- Allow more than a single Error Notification for Container action errors
- Various Alert cleanups
- Translation updates

* Wed Oct 30 2019 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 10-1

- Support for user containers

* Wed Oct 02 2019 Martin Pitt <martin@piware.de> - 9-1

- Minimize CSS in production builds
- Bump NPM dependencies to latest versions

* Wed Sep 04 2019 Martin Pitt <martin@piware.de> - 8-1

- Show list of containers that use given image
- Show placeholder while loading containers and images
- Fix setting memory limit

* Wed Jul 31 2019 Martin Pitt <martin@piware.de> - 7-1

- Fix AppStream ID
- Adjust tests to changed Cockpit Services page

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Martin Pitt <martin@piware.de> - 6-1

- Fix various UI regressions from Cockpit's PatternFly 4 switch
- Add packit configuration (https://packit.dev/)

* Wed Jul 10 2019 Martin Pitt <martin@piware.de> - 5-1

- Add container Terminal

* Wed Jun 26 2019 Katerina Koukiou <kkoukiou@redhat.com> - 4-1

- Fix regression in container commit

* Mon Jun 17 2019 Martin Pitt <martin@piware.de> - 3-1

- Enable Commit button for running containers
- Fix race condition with container deletion
- Stop fetching all containers/images for each container/image event

* Fri May 24 2019 Cockpit Project <cockpituous@gmail.com> - 2-1
- Update to upstream 2 release

* Wed Apr 17 2019 Cockpit Project <cockpituous@gmail.com> - 1-2
- Update to upstream 1 release


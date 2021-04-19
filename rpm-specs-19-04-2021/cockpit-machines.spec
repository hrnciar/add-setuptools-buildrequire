# This spec file has been automatically updated
Version:        243
Release: 1%{?dist}
#
# Copyright (C) 2021 Red Hat, Inc.
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

Name:           cockpit-machines
Summary:        Cockpit user interface for virtual machines
License:        LGPLv2+ and MIT
URL:            https://github.com/cockpit-project/cockpit-machines

Source0:        https://github.com/cockpit-project/cockpit-machines/releases/download/%{version}/cockpit-machines-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires: cockpit-bridge >= 215
%if 0%{?suse_version}
Requires: libvirt-daemon-qemu
%else
Requires: libvirt-daemon-kvm
%endif
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0
# Optional components
Recommends: virt-install
Recommends: libosinfo
Recommends: python3-gobject-base

%description -n cockpit-machines
Cockpit component for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%prep
%setup -q -n cockpit-machines

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

# The changelog is automatically generated and merged
%changelog
* Wed Apr 14 2021 Matej Marusak <mmarusak@redhat.com> - 243-1

- PatternFly 4 updates
- Translation updates
- Correctly manage editing of unknown bus type

* Thu Apr 01 2021 Katerina Koukiou <kkoukiou@redhat.com> - 242.1-1

- Add MIT to the list of licenses in spec file


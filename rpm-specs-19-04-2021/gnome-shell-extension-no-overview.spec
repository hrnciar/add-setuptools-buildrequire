%global extension   no-overview
%global uuid        %{extension}@fthx

Name:           gnome-shell-extension-%{extension}
Version:        4
Release:        1%{?dist}
Summary:        GNOME Shell extension for no overview at start-up
License:        GPLv3
URL:            https://extensions.gnome.org/extension/4099/no-overview/
Source0:        https://extensions.gnome.org/extension-data/no-overviewfthx.v%{version}.shell-extension.zip
Source1:        https://raw.githubusercontent.com/fthx/no-overview/main/LICENSE#/%{extension}-LICENSE
Source2:        https://raw.githubusercontent.com/fthx/no-overview/main/README.md#/%{extension}-README.md
BuildArch:      noarch
Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app


%description
GNOME Shell extension for no overview at start-up. For GNOME Shell 40+.

%prep
%autosetup -cn %{name}-%{version}
cp -p %SOURCE1 LICENSE
cp -p %SOURCE2 README.md

%build
# Nothing to build here

%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -rp *.js metadata.json \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}


%changelog
* Wed Apr 14 2021 Takao Fujiwara <tfujiwar@redhat.com> - 4-1
- Initial integration

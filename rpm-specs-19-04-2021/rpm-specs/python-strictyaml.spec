%global srcname strictyaml

Name:           python-%{srcname}
Version:        1.4.0
%global forgeurl https://github.com/crdoconnor/%{srcname}/
#%%global tag %%{version}
# Upstream failed to tag the 1.4.0 release:
%global commit ae2131a8dab9a341fd30b8334d69a4d319252cd1
%forgemeta
Release:        1%{?dist}
Summary:        Parses and validates a restricted subset of YAML

License:        MIT
URL:            http://hitchdev.com/%{srcname}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# We do not attempt to build the documentation, since it requires an
# idiosyncratic build system (see https://hitchdev.com/) that is hopelessly
# entangled with the idea of downloading dependencies from PyPI. An offline
# build would be nearly impossible.

%global common_description %{expand:
StrictYAML is a type-safe YAML parser that parses and validates a restricted
subset of the YAML specification.

Priorities:

  • Beautiful API
  • Refusing to parse the ugly, hard to read and insecure features of YAML like
    the Norway problem.
  • Strict validation of markup and straightforward type casting.
  • Clear, readable exceptions with code snippets and line numbers.
  • Acting as a near-drop in replacement for pyyaml, ruamel.yaml or poyo.
  • Ability to read in YAML, make changes and write it out again with comments
    preserved.
  • Not speed, currently.}

%description %{common_description}


%generate_buildrequires
%pyproject_buildrequires


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}


%prep
%forgesetup


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


# There are no tests. (If there were, it would be as hard to run them as it is
# to build the documentation.)


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md


%changelog
* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.4.0-1
- Update to 1.4.0
- Start using pyproject-rpm-macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 14:10:19 EST 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.2-1
- Update to 1.3.2

* Tue Jan 12 11:40:57 EST 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.1-1
- Update to 1.3.1

* Sun Jan 10 13:51:32 EST 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-1
- Update to 1.3.0

* Sat Jan  2 16:01:07 EST 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.2.0-1
- Update to version 1.2.0

* Thu Nov 26 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-3
- Remove conditionals for Fedora 32 and older

* Thu Nov 26 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-2
- Remove EPEL conditionals from Fedora spec file

* Tue Nov 24 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.0-1
- Initial package

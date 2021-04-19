# Generated by go2rpm
%bcond_without check

# https://github.com/JamesClonk/vultr
%global goipath         github.com/JamesClonk/vultr
Version:                1.15.0
%global tag             %{version}

%gometa

%global common_description %{expand:
Vultr CLI and API client library.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           vultr
Release:        7%{?dist}
Summary:        Vultr CLI

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jawher/mow.cli)
BuildRequires:  golang(github.com/juju/ratelimit)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
Vultr CLI is a command line tool for using the Vultr API.  It allows you to
create and manage your virtual machines, SSH public keys, snapshots, and
startup scripts on your Vultr account.  You can also use it to directly SSH
into a Vultr virtual machine through the vultr ssh command.

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/vultr %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/vultr

%gopkgfiles

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15.0-3
- Update to latest Go macros

* Tue Jan 22 2019 Carl George <carl@george.computer> - 1.15.0-2
- Expand description

* Sun Jan 06 2019 Carl George <carl@george.computer> - 1.15.0-1
- Initial package

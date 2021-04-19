Name:		secvarctl
Version:	0.1
Release:	1%{?dist}
Summary:	A command line tool for managing Secure Boot Variables on POWER

License:	ASL 2.0
URL:		https://github.com/open-power/secvarctl
Source0:	https://github.com/open-power/secvarctl/archive/v%{version}.tar.gz


BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	mbedtls-devel


%description
secvarctl is a collection of sub-commands for reading, writing
and updating secure variables on POWER's Secure Boot.
The sub-commands are:
	-read , prints info on secure variables
	-write , updates secure variable with new signed authenticated file
	-validate , validates format of given file
	-verify , determines if new variable updates are correctly signed/formatted
	-generate , create relevant files for secure variable management

%prep
%setup -q


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Nov  5 2020 Nick Child <nnac123@linux.vnet.ibm.com> - 0.1-1
- Initial package
- 

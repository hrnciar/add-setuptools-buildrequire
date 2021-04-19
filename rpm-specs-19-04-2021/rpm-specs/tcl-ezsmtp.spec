%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}
%global extname ezsmtp

Name:           tcl-%{extname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Easy SMTP for TCL

License:        TCL and MIT
# the original website for ezsmtp is long gone
URL:            https://web.archive.org/web/20020602055052/http://www.millibits.com/djh/tcl
# archive.org will serve tar.gz as tar, so rename accordingly
Source0:        %{url}/%{extname}%{version}.tar.gz#/%{extname}%{version}.tar

BuildRequires:  tcl

Requires:       tcl(abi) = 8.6
Provides:       %{extname} = %{version}-%{release}

BuildArch:      noarch

%description
Easy SMTP (ezsmtp) is a simple 100%-pure-Tcl cross-platform package for
sending text email, based on original work by Keith Vetter at UC Berkeley.

%prep
%setup -q -n %{extname}%{version}
mkdir -p examples
mv koi8-r-body.txt test_examples.txt postinst.tcl examples/

%build

%install
mkdir -p %{buildroot}%{tcl_sitelib}/ezsmtp
cp -P ezsmtp.tcl %{buildroot}%{tcl_sitelib}/ezsmtp

%files
%license license.txt
%doc README.txt ChangeLog ezsmtp.html
%doc examples
%{tcl_sitelib}/ezsmtp

%changelog
* Fri Apr 16 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.0-1
- Initial package

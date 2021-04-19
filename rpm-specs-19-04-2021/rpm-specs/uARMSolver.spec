Name:		uARMSolver
Version:	0.2.1
Release:	1%{?dist}
Summary:	Universal Association Rule Mining Solver

License:	MIT
URL:		https://github.com/firefly-cpp/uARMSolver
Source0:	https://github.com/firefly-cpp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
	
BuildRequires:	gcc-c++
BuildRequires:	make

%description
uARMSolver allows users to preprocess their data in a transaction database, to 
make discretization of data, to search for association rules and to guide a 
presentation/visualization of the best rules found using external tools. 
Mining the association rules is defined as an optimization and solved using 
the nature-inspired algorithms that can be incorporated easily. Because 
the algorithms normally discover a huge amount of association rules, the 
framework enables a modular inclusion of so-called visual guiders for 
extracting the knowledge hidden in data, and visualize these using 
external tools. 

%prep
%autosetup

%build
%{set_build_flags}
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 ./bin/uARMSolver %{buildroot}/%{_bindir}/%{name}
rm -f %{buildroot}%{_infodir}/dir

%files
%{_bindir}/uARMSolver
%license LICENSE
%doc bin/README.txt

%changelog
* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- New version - 0.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2-1
- Initial version of the package

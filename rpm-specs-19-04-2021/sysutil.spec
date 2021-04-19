# Generated by go2rpm 1
%bcond_without check

# https://github.com/knq/sysutil
%global goipath         github.com/knq/sysutil
%global commit          15668db23d08158adb81783bf9e1617e7ca99c10

%gometa

%global common_description %{expand:
Package sysutil provides cross platform system utilities.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           sysutil
Version:        0
Release:        0.4%{?dist}
Summary:        Provides cross platform system utilities

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200607git8af17bc
- Rename the package

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200406git15668db
- Initial package


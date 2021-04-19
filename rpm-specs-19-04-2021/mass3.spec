# Generated by go2rpm 1
%bcond_without check

# https://github.com/smiegles/mass3
%global goipath         github.com/smiegles/mass3
%global commit          e1d5f1a4284a367f7a8ccef4ce2bd79cd9c75521

%gometa

%global common_description %{expand:
Quickly enumerate through a pre-compiled list of AWS S3 buckets using DNS
instead of HTTP with a list of DNS resolvers and multi-threading.}

%global golicenses      LICENSE
%global godocs          README.md lists/buckets.txt lists/resolvers.txt

Name:           mass3
Version:        0
Release:        0.3%{?dist}
Summary:        Buckets enumerator

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/remeh/sizedwaitgroup)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/mass3 %{goipath}

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
%doc README.md lists/buckets.txt lists/resolvers.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200527gite1d5f1a
- Initial package for Fedora


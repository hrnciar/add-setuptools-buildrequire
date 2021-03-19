# Generated by go2rpm
%bcond_without check

# https://github.com/bifurcation/mint
%global goipath         github.com/bifurcation/mint
%global commit          93c820e81448f1376a058f36684e09b8ad697fe0

%gometa

%global common_description %{expand:
A Minimal TLS 1.3 Implementation in Go.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Minimal TLS 1.3 Implementation in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/net/http2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in bin/mint-client-https bin/mint-server-https bin/mint-server bin/mint-client; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# https://github.com/bifurcation/mint/issues/204
%gocheck -d .
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 13:43:45 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200724git93c820e
- Bump to commit 93c820e81448f1376a058f36684e09b8ad697fe0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 18:53:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702git83ba9bc
- Initial package

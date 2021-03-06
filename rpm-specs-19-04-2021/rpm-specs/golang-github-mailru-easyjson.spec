# Generated by go2rpm
%bcond_without check

# https://github.com/mailru/easyjson
%global goipath         github.com/mailru/easyjson
Version:                0.7.6

%gometa

%global common_description %{expand:
Package Easyjson provides a fast and easy way to marshal/unmarshal Go structs
to/from JSON without the use of reflection. In performance tests, easyjson
outperforms the standard encoding/json package by a factor of 4-5x, and other
JSON encoding packages by a factor of 2-3x.

Easyjson aims to keep generated Go code simple enough so that it can be easily
optimized or fixed. Another goal is to provide users with the ability to
customize the generated code by providing options not available with the
standard encoding/json package, such as generating "snake_case" names or
enabling omitempty behavior by default.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Fast JSON serializer for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/josharian/intern)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in easyjson; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# https://github.com/mailru/easyjson/issues/227
%gocheck -d tests
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 15 00:38:33 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 21:13:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190628git1ea4449
- Initial package

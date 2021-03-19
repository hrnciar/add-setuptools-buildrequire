# Generated by go2rpm
%bcond_without check

# https://github.com/mitchellh/colorstring
%global goipath         github.com/mitchellh/colorstring
%global commit          d06e56a500db4d08c33db0b79461e7c9beafca2d

%gometa

%global common_description %{expand:
Colorstring is a Go library for outputting colored strings to a console using a
simple inline syntax in your string to specify the color to print as.

For example, the string [blue]hello [red]world would output the text "hello
world" in two colors. The API of Colorstring allows for easily disabling colors,
adding aliases, etc.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Go library for colorizing strings for terminal output

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 00:17:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190623gitd06e56a
- Initial package

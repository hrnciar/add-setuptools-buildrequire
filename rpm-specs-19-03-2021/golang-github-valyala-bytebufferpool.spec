# Generated by go2rpm
%bcond_without check

# https://github.com/valyala/bytebufferpool
%global goipath         github.com/valyala/bytebufferpool
Version:                1.0.0

%gometa

%global common_description %{expand:
An implementation of a pool of byte buffers with anti-memory-waste protection.

The pool may waste limited amount of memory due to fragmentation. This amount
equals to the maximum total size of the byte buffers in concurrent use.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Anti-memory-waste byte buffer pool

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 23:42:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package

# Generated by go2rpm
%bcond_without check

%if %{fedora} >= 33
%global llvm_major 11
%else
%global llvm_major 10
%endif

# https://github.com/tinygo-org/go-llvm
%global goipath         tinygo.org/x/go-llvm
%global forgeurl        https://github.com/tinygo-org/go-llvm
%global commit          570e7a6841d9b3ae1c357ac08ff38fe43b55e9c3

%gometa

%global godevelheader %{expand:
Requires:       llvm-devel(major) = %{llvm_major}}

%global common_description %{expand:
This library provides bindings to a system-installed LLVM.}

%global golicenses      LICENSE.txt
%global godocs          README.markdown

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Go bindings to a system-installed LLVM

License:        NCSA
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  gcc-c++
BuildRequires:  llvm-devel(major) = %{llvm_major}
BuildRequires: make

%description
%{common_description}

%gopkg

%prep
%goprep

# Set current LLVM paths.
# Extra checks because of https://bugzilla.redhat.com/show_bug.cgi?id=1871659
if type llvm-config-%{llvm_major}-%{__isa_bits}; then
make config VERSION=%{llvm_major}.0.0 CONFIG=llvm-config-%{llvm_major}-%{__isa_bits} BUILDDIR=%{_prefix}
else
make config VERSION=%{llvm_major}.0.0 CONFIG=llvm-config-%{__isa_bits} BUILDDIR=%{_prefix}
fi

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.15.20201119git570e7a6
- Update to 570e7a6841d9b3ae1c357ac08ff38fe43b55e9c3
- Drop compatibility with EOL Fedora 31

* Sat Sep 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.14.20200919git70c5585
- Switch to llvm11 branch

* Sun Aug 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.13.20200818git345b294
- Simplify LLVM dependency

* Tue Aug 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.12.20200818git345b294
- Update to latest commit

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200419git8d12088
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.10.20200419git8d12088
- Update to latest commit

* Tue Feb 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.9.20200207git1ff21df
- Add support for LLVM 10

* Fri Feb 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.8.20200207git1ff21df
- Update to latest commit

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20190925git95bc4ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.6.20190925git95bc4ff
- Update to latest commit

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190604git0713e35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 01:54:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190604git0713e35
- Update to new macros

* Fri Jun 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20190604git0713e35
- Update to latest commit
- Add gcc-c++ to Requires

* Sat Apr 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.20190427git7707ae5
- Add llvm-devel to Requires

* Thu Apr 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190427git7707ae5
- First package for Fedora

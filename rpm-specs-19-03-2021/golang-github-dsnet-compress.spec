# Generated by go2rpm
%ifnarch ppc64le
%bcond_without check
%endif

# https://github.com/dsnet/compress
%global goipath         github.com/dsnet/compress
Version:                0.0.1

%gometa

%global common_description %{expand:
This package hosts a collection of compression related libraries. The goal of
this project is to provide pure Go implementations for popular compression
algorithms beyond what the Go standard library provides. The goals for these
packages are as follows:
* Maintainable: That the code remains well documented, well tested, readable,
  easy to maintain, and easy to verify that it conforms to the specification
  for the format being implemented.
* Performant: To be able to compress and decompress within at least 80% of the
  rates that the C implementations are able to achieve.
* Flexible: That the code provides low-level and fine granularity control over
  the compression streams similar to what the C APIs would provide.

Of these three, the first objective is often at odds with the other two
objectives and provides interesting challenges. Higher performance can often be
achieved by muddling abstraction layers or using non-intuitive low-level
primitives. Also, more features and functionality, while useful in some
situations, often complicates the API. Thus, this package will attempt to
satisfy all the goals, but will defer to favoring maintainability when the
performance or flexibility benefits are not significant enough.}

%global golicenses      LICENSE.md
%global godocs          doc README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Collection of compression related Go packages

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dsnet/golib/unitconv)
BuildRequires:  golang(github.com/klauspost/compress/flate)
BuildRequires:  golang(github.com/ulikunitz/xz/lzma)
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 18:20:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Release 0.0.1

* Wed Feb 13 2019 Dominik Mierzejewski <dominik@greysector.net> - 0-0.5.gitcc9eb1d
- disable tests on ppc64le temporarily (#1675014)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitcc9eb1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitcc9eb1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.2.20180326gitcc9eb1d
- split docs into a separate subpackage

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180326gitcc9eb1d
- First package for Fedora
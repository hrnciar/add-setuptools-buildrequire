# Generated by go2rpm
%bcond_without check

# https://github.com/influxdata/tdigest
%global goipath         github.com/influxdata/tdigest
Version:                0.0.1

%gometa

%global common_description %{expand:
A new data structure for accurate on-line accumulation of rank-based statistics
such as quantiles and trimmed means. The t-digest algorithm is also very
friendly to parallel programs making it useful in map-reduce and parallel
streaming applications implemented using, say, Apache Spark.

This is an implementation of Ted Dunning's t-digest in Go.

The implementation is based off Derrick Burns' C++ implementation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Implementation of Ted Dunning's t-digest in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(gonum.org/v1/gonum/stat/distuv)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 00:40:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Update to 0.0.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 00:27:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190624gitbf2b5ad
- Initial package
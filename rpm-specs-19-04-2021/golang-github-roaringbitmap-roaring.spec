# Generated by go2rpm
%bcond_without check

# https://github.com/RoaringBitmap/roaring
%global goipath         github.com/RoaringBitmap/roaring
Version:                0.5.5

%gometa

%global goaltipaths     github.com/influxdata/roaring

# Remove in F36:
%global godevelheader %{expand:
Obsoletes:      golang-github-influxdata-roaring-devel < 0.4.12-6
}

%global common_description %{expand:
This is a go version of the Roaring bitmap data structure.

Roaring bitmaps are used by several major systems such as Apache Lucene and
derivative systems such as Solr and Elasticsearch, Metamarkets' Druid,
LinkedIn Pinot, Netflix Atlas, Apache Spark, OpenSearchServer, Cloud Torrent,
Whoosh, Pilosa, Microsoft Visual Studio Team Services (VSTS), and
eBay's Apache Kylin.}

%global golicenses      LICENSE LICENSE-2.0.txt
%global godocs          AUTHORS CONTRIBUTORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go version of the Roaring bitmap data structure

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/glycerine/go-unsnap-stream)
BuildRequires:  golang(github.com/tinylib/msgp/msgp)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/willf/bitset)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 10:54:48 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.5-1
- Update to 0.5.5
- Close: rhbz#1871272

* Sat Aug 01 21:55:01 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 19:38:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.18-1
- Release 0.4.18

* Sun Mar 17 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.17-1
- Release 0.4.17 (#1689418)

* Sun Mar 03 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.16-1
- First package for Fedora
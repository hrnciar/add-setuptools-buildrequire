%global jsname jquery-ui

Name:		js-%{jsname}
Version:	1.12.1
Release:	2%{?dist}
Summary:	jQuery user interface

License:	MIT
URL:		https://jqueryui.com/
#		The upstream source bundles a copy of jshint which has a
#		non-free license and can not be distributed by Fedora.
#		The source included in the srpm has the external/jshint
#		directory removed
Source0:	%{jsname}-%{version}.tar.gz
#		We need to bundle build dependencies since they are no
#		longer available in Fedora. This uses the same
#		technique as the js-jquery package.
Source1:	%{jsname}-%{version}-node-modules.tar.gz
#		Script to create the above sources
Source2:	create-source.sh

BuildArch:	noarch
BuildRequires:	nodejs
BuildRequires:	web-assets-devel
BuildRequires:	yuicompressor
Requires:	js-jquery >= 1.7.0
Requires:	web-assets-filesystem

%description
A curated set of user interface interactions, effects, widgets, and
themes built on top of the jQuery JavaScript Library.

%prep
%setup -q -n %{jsname}-%{version} -a 1

%build
./node_modules/grunt-cli/bin/grunt -v requirejs:js concat:css uglify:main

# Provide a compressed version of the cascading style sheet
yuicompressor -o dist/jquery-ui.min.css dist/jquery-ui.css

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}
install -m 644 -p dist/* %{buildroot}%{_jsdir}/%{jsname}
mkdir -p %{buildroot}%{_jsdir}/%{jsname}/images
install -m 644 -p themes/base/images/* %{buildroot}%{_jsdir}/%{jsname}/images

%files
%{_jsdir}/%{jsname}
%license LICENSE.txt
%doc AUTHORS.txt CONTRIBUTING.md README.md

%changelog
* Sat Mar 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.12.1-2
- Provide a compressed version of the cascading style sheet

* Sat Feb 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.12.1-1
- First packaging for Fedora

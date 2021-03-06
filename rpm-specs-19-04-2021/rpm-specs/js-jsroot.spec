%global jsname jsroot

Name:		js-%{jsname}
Version:	5.9.1
Release:	1%{?dist}
Summary:	JavaScript ROOT - Interactive numerical data analysis graphics

#		Most files are MIT, d3.js is BSD
License:	MIT and BSD
URL:		https://jsroot.gsi.de/
Source0:	https://github.com/root-project/%{jsname}/archive/%{version}/%{jsname}-%{version}.tar.gz
#		Use locally installed mathjax instead of remote installation.
Patch0:		%{name}-mathjax.patch

BuildArch:	noarch
BuildRequires:	web-assets-devel
BuildRequires:	yuicompressor
BuildRequires:	uglify-js
Requires:	web-assets-filesystem
Requires:	js-jquery
Requires:	js-jquery-mousewheel
Requires:	js-jquery-ui
Requires:	js-jquery-ui-touch-punch
Requires:	mathjax

%description
JavaScript ROOT provides interactive ROOT-like graphics in web browsers.
Data can be read and displayed from binary and JSON ROOT files.

%prep
%setup -q -n %{jsname}-%{version}
%patch0 -p1

# Remove pre-minified scripts
rm scripts/*.min.js

# Remove bundled dependencies packaged in Fedora
rm libs/jquery.js
rm libs/jquery-ui.js
rm style/jquery-ui.css
rm -rf style/images

# Remove .gitignore file
rm demo/gulp/.gitignore

%build
for s in scripts/JSRoot*.js scripts/ThreeCSG.js ; do
    yuicompressor ${s} -o ${s%.js}.min.js
done

for s in rawinflate three.extra ; do
    yuicompressor libs/${s}.js -o scripts/${s}.min.js
done

for s in style/JSRoot*.css ; do
    yuicompressor ${s} -o ${s%.css}.min.css
done

uglifyjs libs/d3.js -c negate_iife=false -m --comments /Copyright/ -o scripts/d3.min.js

uglifyjs libs/dat.gui.js -c -m -o scripts/dat.gui.min.js

uglifyjs libs/three.js -c -m -b beautify=false,preamble="'// threejs.org/license'" -o scripts/three.min.js

%install
mkdir -p %{buildroot}%{_jsdir}/%{jsname}/scripts
install -m 644 -p scripts/*.js %{buildroot}%{_jsdir}/%{jsname}/scripts

ln -s %{_jsdir}/jquery/latest/jquery.min.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts
ln -s %{_jsdir}/jquery.mousewheel.min.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts
ln -s %{_jsdir}/jquery-ui/jquery-ui.min.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts
ln -s %{_jsdir}/jquery-ui-touch-punch/jquery.ui.touch-punch.min.js \
   %{buildroot}%{_jsdir}/%{jsname}/scripts
ln -s %{_jsdir}/mathjax \
   %{buildroot}%{_jsdir}/%{jsname}/scripts

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/libs
install -m 644 -p libs/*.js %{buildroot}%{_jsdir}/%{jsname}/libs
rm %{buildroot}%{_jsdir}/%{jsname}/libs/three.extra_head.js
rm %{buildroot}%{_jsdir}/%{jsname}/libs/three.svg_renderer_header.js
rm %{buildroot}%{_jsdir}/%{jsname}/libs/three.svg_renderer_footer.js

ln -s %{_jsdir}/jquery/latest/jquery.js \
   %{buildroot}%{_jsdir}/%{jsname}/libs
ln -s %{_jsdir}/jquery.mousewheel.js \
   %{buildroot}%{_jsdir}/%{jsname}/libs
ln -s %{_jsdir}/jquery-ui/jquery-ui.js \
   %{buildroot}%{_jsdir}/%{jsname}/libs
ln -s %{_jsdir}/jquery-ui-touch-punch/jquery.ui.touch-punch.js \
   %{buildroot}%{_jsdir}/%{jsname}/libs

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/style
install -m 644 -p style/*.css %{buildroot}%{_jsdir}/%{jsname}/style

ln -s %{_jsdir}/jquery-ui/jquery-ui.css \
   %{buildroot}%{_jsdir}/%{jsname}/style
ln -s %{_jsdir}/jquery-ui/images \
   %{buildroot}%{_jsdir}/%{jsname}/style

# No minified stylesheet in js-jquery-ui package - symlink non-minified version
ln -s jquery-ui.css %{buildroot}%{_jsdir}/%{jsname}/style/jquery-ui.min.css

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/files
install -m 644 -p files/* %{buildroot}%{_jsdir}/%{jsname}/files

mkdir -p %{buildroot}%{_jsdir}/%{jsname}/img
install -m 644 -p img/* %{buildroot}%{_jsdir}/%{jsname}/img

mkdir -p %{buildroot}%{_pkgdocdir}
ln -s %{_jsdir}/%{jsname}/scripts %{buildroot}%{_pkgdocdir}
ln -s %{_jsdir}/%{jsname}/style %{buildroot}%{_pkgdocdir}
ln -s %{_jsdir}/%{jsname}/files %{buildroot}%{_pkgdocdir}
ln -s %{_jsdir}/%{jsname}/img %{buildroot}%{_pkgdocdir}

%files
%{_jsdir}/%{jsname}
%license LICENSE scripts/*.LICENSE
%doc %{_pkgdocdir}
%doc changes.md demo docs/* index.htm readme.md

%changelog
* Thu Mar 11 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.9.1-1
- Update to version 5.9.1
- Change Requires to new js-jquery-ui package (also for EPEL 8)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-5
- Compatibility with uglifyjs v3 (no --preamble option)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-3
- Do not use closure-compiler for Fedora 33+ - it is orphaned and
  uninstallable with broken deps.

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-2
- No longer bundle js-jquery, js-jquery-mousewheel and
  js-jquery-ui-touch-punch for EPEL 8.
- Still bundle js-jquery-ui which is not available in EPEL 8.

* Mon Mar 23 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.8.0-1
- Update to version 5.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.2-1
- Update to version 5.7.2
- Bundle jquery and its dependants in EPEL 8 - not available

* Wed Aug 14 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.1-1
- Update to version 5.7.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.7.0-1
- Update to version 5.7.0

* Fri Mar 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.4-1
- Update to version 5.6.4

* Fri Feb 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.3-1
- Update to version 5.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.1-1
- Update to version 5.6.1

* Mon Nov 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.6.0-1
- Update to version 5.6.0

* Thu Aug 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.5.1-1
- Update to version 5.5.1

* Fri Jul 20 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.5.0-1
- Update to version 5.5.0
- Change dependency to js-jquery since js-jquery2 is orphaned

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-2
- Adapt symlinks to updated jquery-ui package

* Wed May 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.2-1
- Update to version 5.4.2

* Wed Apr 11 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.1-1
- Update to version 5.4.1

* Sat Feb 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.4.0-1
- Update to version 5.4.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.5-1
- Update to version 5.3.5

* Wed Jan 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.4-2
- Make Summary more informative
- Add files directory needed by root-net-http

* Mon Dec 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.3.4-1
- Initial packaging for Fedora

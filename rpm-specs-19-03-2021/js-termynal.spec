%global srcname termynal

%global commit 9b301892db6f8d403abfce7adf65888dffed72ea
%global forgeurl https://github.com/ines/%{srcname}/
%forgemeta

Name:           js-%{srcname}
Summary:        Lightweight and modern terminal animations using async/await
Version:        0.0.1
Release:        2%{?dist}

URL:            %{forgeurl}
Source0:        %{forgesource}
License:        MIT

BuildArch:      noarch

BuildRequires:  web-assets-devel
BuildRequires:  golang-github-evanw-esbuild

Requires:       web-assets-filesystem

%description
Typing animations are nothing new and Termynal isn’t particularly
revolutionary. The author wrote it because they needed a modern and lightweight
version with minimal JavaScript and without messy, nested setTimeout calls.
Most of the existing libraries rely on JavaScript for both the rendering,
styling and animation, or even require jQuery. This is inconvenient, especially
if you’re using the animation as part of your software’s documentation. If a
user has JavaScript disabled, they will only see a blank window.

Termynal uses async and await, which is now supported pretty much across all
major browsers. Termynal lets you write all input and output in plain HTML, and
all styling in plain CSS. Non-JS users will still see the complete code, just
no animation. The width and height of the terminal window is read off the
original container. This means you won’t have to worry about sizing or layout
reflows. Termynal also comes with a flexible HTML API, so you can use it
without having to write a single line of JavaScript yourself.


%prep
%forgeautosetup
# Remove pre-minified JavaScript per Fedora guidelines
rm -f *.min.*


%build
esbuild \
    --platform=browser \
    --sourcemap \
    --minify \
    --out-extension:.js=.min.js \
    --outdir=%{_vpath_builddir} \
    %{srcname}.js


%install
install -t '%{buildroot}%{_jsdir}/%{srcname}' -m 0644 -p -D \
    %{srcname}.* %{_vpath_builddir}/%{srcname}.*


# There are no tests.


%files
%license LICENSE
%doc README.md
%doc example*.html

%{_jsdir}/%{srcname}


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.1-2
- Remove stray find command

* Fri Mar 05 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.0.1-1
- Initial package

# Build HTML docs from markdown using pandoc?
%bcond_without html_docs

Name:           gn
# Upstream uses the number of commits in the git history as the version number.
# See gn --version, which outputs something like “1874 (2b683eff)”. The commit
# position and short commit hash in this string come from “git describe HEAD
# --match initial-commit”; see build/gen.py. This means that a complete git
# checkout is required to establish the version number; the information is not
# in the tarball! This is terribly inconvenient. See
# https://bugs.chromium.org/p/gn/issues/detail?id=3.
#
# As a result, it is necessary to use our custom update-version script,
# supplying the new full commit hash as the sole argument or providing no
# arguments to select the latest commit. This will:
#  1. Clone the git repository from the Internet (a substantial download)
#  2. Run build/gen.py to generate last_commit_position.h, the header with
#     version information, and copy it into the same directory as the script
#  3. Modify the commit and access macros and the Version field in this spec
#     file.
#  4. Download the source tarball (spectool -g)
#  5. Update the sources (fedpkg new-sources %%{commit}.tar.gz)
#  6. Stage all changes in git
%global commit dba01723a441c358d843a575cb7720d54ddcdf92
%global access 20210410
%global shortcommit %(echo %{commit} | cut -b -8)
Version:        1897
Release:        1.%{access}git%{shortcommit}%{?dist}
Summary:        Meta-build system that generates build files for Ninja

# BSD except for src/base/third_party/icu/, which is (Unicode and MIT); note
# that the “ICU License” is MIT,
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_style_.28ICU_Variant.29
#
# Note that src/util/test/gn_test.cc, which is licensed ASL 2.0, does not
# contribute to the installed RPM, only to the gn_unittests executable; you may
# verify this with:
#   gdb -ex 'set pagination off' -ex 'info sources' gn | grep -F gn_test.cc
License:        BSD and Unicode and MIT
URL:            https://%{name}.googlesource.com/%{name}
Source0:        %{url}/+archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
# Generated using script update-version:
Source1:        last_commit_position.h
Source2:        update-version

# Clean up compiler warnings on gcc/g++:
Patch0:         https://src.fedoraproject.org/rpms/chromium/raw/ce30313f5e4af121140c037bf026453355534f24/f/chromium-84.0.4147.105-gn-gcc-cleanup.patch

# The python3_pkgversion macro is required for EPEL; see
# https://fedoraproject.org/wiki/PackagingDrafts:Python3EPEL. On Fedora (and
# EPEL8) it simply expands to “3”.
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  /usr/bin/pathfix.py

%if %{with html_docs}
BuildRequires:  pandoc
BuildRequires:  parallel
%endif
BuildRequires:  help2man

Requires:       vim-filesystem
Requires:       python%{python3_pkgversion}
Provides:       vim-%{name} = %{version}-%{release}

BuildRequires:  emacs
Requires:       emacs-filesystem >= %{_emacs_version}
Provides:       emacs-%{name} = %{version}-%{release}


%description
GN is a meta-build system that generates build files for Ninja.


%package doc
Summary:        Documentation for GN
BuildArch:      noarch

%description doc
The %{name}-doc package contains detailed documentation for GN.


%prep
%autosetup -c -n %{name}-%{commit} -p3

# Use pre-generated last_commit_position.h.
mkdir -p ./out
cp -vp '%{SOURCE1}' ./out

# Copy and rename vim extensions readme for use in the main documentation
# directory.
cp -vp misc/vim/README.md README-vim.md

# Fix shebangs in examples and such.
%py3_shebang_fix .
# On EPEL7, we would have to work around the missing py3_shebang_fix macro, but
# the package would not build anyway because it requires C++17 support.


%build
# We need to set CC and CXX explicitly before Fedora 33, including on the EPELs.
CC='gcc'; export CC
CXX='g++'; export CXX
AR='gcc-ar'; export AR
%set_build_flags
# Both --use-icf and --use-lto add compiler flags that only work with clang++,
# not with g++. We do get LTO on Fedora anyway, since we respect the
# distribution’s build flags.
%{__python3} build/gen.py \
    --no-last-commit-position \
    --no-strip \
    --no-static-libstdc++
ninja -C out -v

%if %{with html_docs}
# There is a script, misc/help_as_html.py, that generates some HTML help, but
# pandoc does a better job and we can cover more Markdown sources.
find . -type f -name '*.md' | parallel -v pandoc -o '{.}.html' '{}'
%endif

help2man \
    --name='%{summary}' \
    --version-string="%{name} $(./out/%{name} --version)" \
    --no-info \
    ./out/%{name} |
  # Clean up a couple of stray binary bytes in the help output
  tr -d '\302\240' |
  # Format the entries within the sections as tagged paragraphs, and italicise
  # [placeholders in square brackets].
  sed -r -e 's/(^[[:alnum:]_]+:)/.TP\n.B \1\n/' \
      -e 's/\[([^]]+)\]/\\fI[\1]\\fR/g' > out/%{name}.1


%install
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p out/%{name}

install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -vrp misc/vim/* '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete
%py_byte_compile %{__python3} '%{buildroot}%{_datadir}/vim/vimfiles/%{name}-format.py'

install -d '%{buildroot}%{_emacs_sitestartdir}'
install -t '%{buildroot}%{_emacs_sitestartdir}' -p -m 0644 misc/emacs/*.el

install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p out/%{name}.1


%check
out/gn_unittests

# Verify consistency of the version header with the spec file
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION_NUM[[:blank:]]+'\
'%{version}[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION[[:blank:]]+'\
'"%{version} \(%{shortcommit}\)"[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null


%files
%license LICENSE
%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1*

%{_datadir}/vim/vimfiles/%{name}-format.py
%{_datadir}/vim/vimfiles/autoload/%{name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{name}filetype.vim
%{_datadir}/vim/vimfiles/ftplugin/%{name}.vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%{_emacs_sitestartdir}/%{name}-mode.el


%files doc
%license LICENSE
%doc AUTHORS
%doc OWNERS
%doc README*.md
%if %{with html_docs}
%doc README*.html
%endif
%doc docs
%doc examples
%doc infra
%doc tools


%changelog
* Sat Apr 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1897-1.20210410gitdba01723
- Update to version 1897

* Tue Apr 06 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1896-1.20210406gita95c8a3c
- Update to version 1896
- Do not use %%exclude for unpackaged files (RPM 4.17 compatibility)

* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1894-4.20210329gitb2e3d862
- Update to version 1894

* Wed Mar 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1893-3.20210314git64b3b940
- Stop installing xemacs plugins
  (https://fedoraproject.org/wiki/Changes/Deprecate_xemacs)

* Wed Mar 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1893-2.20210314git64b3b940
- Improved source URL based on package review feedback

* Mon Mar  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1893-1.20210314git64b3b940
- Update to version 1893

* Mon Mar  1 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1891-1.20210127gitdfcbc6fe
- Update to version 1891

* Sun Jan  3 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1884-1.20210127git94bda7cc
- Update to version 1884

* Sun Jan  3 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1876-1.20210103git0d67e272
- Update to version 1876

* Sat Dec 19 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 1875-1.20201219git4e260f1d
- Initial spec file

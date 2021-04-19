Name:           jo
Summary:        Small utility to create JSON objects
Version:        1.4
Release:        2%{?dist}

URL:            https://github.com/jpmens/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# The entire source is GPLv2+, except json.c and json.h, which are MIT, and
# base64.c and base64.h, which are Public Domain.
License:        GPLv2+ and MIT and Public Domain

BuildRequires:  gcc

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

# Currently, rebuilding jo.md and jo.1 from jo.pandoc does not work for us:
#
#   /usr/bin/pandoc -s -w man+simple_tables -o jo.1 jo.pandoc
#   [WARNING] Could not deduce format from file extension .pandoc
#     Defaulting to markdown
#   The extension simple_tables is not supported for man
#
# We are not required to rebuild these, so for now we just use the ones from
# the source tarball without rebuilding them; we therefore do not BR pandoc.

BuildRequires:  pkgconfig(bash-completion)
# Yes, this is pkgconf on Fedora, but still pkg-config on EPEL7.
BuildRequires:  /usr/bin/pkg-config
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot %(dirname %{bashcompdir} 2>/dev/null)

# Upstream URL: http://ccodearchive.net/info/json.html
# Upstream VCS: https://github.com/rustyrussell/ccan/tree/master/ccan/json
#
# This is a copylib and not designed to be built as a separate library. See
# https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides; even under
# the old guidelines, in which bundled libraries required FPC exemptions, a
# variety of similar CCAN modules had exemptions as copylibs.
#
# Inspection of https://github.com/rustyrussell/ccan/tree/master/ccan/json
# shows the bundled code is consistent with version 0.1 (as declared in a
# comment in https://github.com/rustyrussell/ccan/blob/master/ccan/json/_info),
# but has been forked with various small modifications in json.c.
Provides:       bundled(ccan-json) = 0.1

# The public-domain base64 implementation looks like a copylib, but I could not
# find the upstream from which it was copied, so I am not treating it as a
# bundled dependency.

%description
This is jo, a small utility to create JSON objects

  $ jo -p name=jo n=17 parser=false
  {
      "name": "jo",
      "n": 17,
      "parser": false
  }

or arrays

  $ seq 1 10 | jo -a
  [1,2,3,4,5,6,7,8,9,10]


%prep
%autosetup


%build
autoreconf -fiv
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
# NEWS not included because it is empty
%doc press.md
%doc README.md
%doc %{name}.md

%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1*

# Note that it is standard in Fedora for packages providing shell completions
# to co-own the completions directory in lieu of having a runtime dependency on
# the relevant shell completions package.
%{bashcompdir}


%changelog
* Thu Mar 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.4-2
- Improved source URL (better tarball name)

* Fri Feb 05 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.4-1
- Initial package

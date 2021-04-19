# Generated by go2rpm 1
%bcond_without check

# https://github.com/storj/common
%global goipath         storj.io/common
%global forgeurl        https://github.com/storj/common
%global commit          07a5dc68dc1cf48965c6d5df6c99eddd02bbaf30

%gometa

%global common_description %{expand:
Storj common packages.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Storj common packages

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/btcsuite/btcutil/base58)
BuildRequires:  golang(github.com/calebcase/tmpfile)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/spacemonkeygo/monkit/v3)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/zeebo/admission/v3)
BuildRequires:  golang(github.com/zeebo/admission/v3/admmonkit)
BuildRequires:  golang(github.com/zeebo/admission/v3/admproto)
BuildRequires:  golang(github.com/zeebo/errs)
BuildRequires:  golang(golang.org/x/crypto/argon2)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(storj.io/drpc)
BuildRequires:  golang(storj.io/drpc/drpcconn)
BuildRequires:  golang(storj.io/drpc/drpcctx)
BuildRequires:  golang(storj.io/drpc/drpcerr)
BuildRequires:  golang(storj.io/drpc/drpcmanager)
BuildRequires:  golang(storj.io/drpc/drpcmetadata)
BuildRequires:  golang(storj.io/drpc/drpcstream)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(go.uber.org/zap/zaptest)
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
# rpc: needs network
%gocheck -d rpc -d ranger/httpranger
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 22:55:00 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20210113git07a5dc6
- Bump to commit 07a5dc68dc1cf48965c6d5df6c99eddd02bbaf30

* Fri Sep 18 09:13:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200918git79b66a3
- Initial package

# Generated by go2rpm
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/grpc-ecosystem/grpc-gateway
%global goipath         github.com/grpc-ecosystem/grpc-gateway
Version:                1.16.0

%gometa

%global common_description %{expand:
The grpc-gateway is a plugin of the Google protocol buffers compiler protoc.
It reads protobuf service definitions and generates a reverse-proxy server
which translates a RESTful JSON API into gRPC. This server is generated
according to the google.api.http annotations in your service definitions.}

%global golicenses      LICENSE.txt
%global godocs          docs examples CHANGELOG.md CONTRIBUTING.md README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        GRPC to JSON proxy generator

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/antihax/optional)                                          
BuildRequires:  golang(github.com/ghodss/yaml)                                               
BuildRequires:  golang(github.com/golang/glog)                                               
BuildRequires:  golang(github.com/golang/protobuf/descriptor)                                
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)                                    
BuildRequires:  golang(github.com/golang/protobuf/proto)                                     
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)                  
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/plugin)                      
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/rogpeppe/fastuuid)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/httpbody)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires:  golang(google.golang.org/grpc) 
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/connectivity)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%build
for cmd in protoc-gen-swagger protoc-gen-grpc-gateway; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -d runtime
%endif

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 07:51:13 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.0-1
- Update to 1.16.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 21:33:16 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.14.6-1
- Update to 1.14.6

* Tue Feb 11 16:42:41 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.5-3
- Add Obsoletes for old name

* Sat Apr 27 14:05:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.5-2
- Update to new macros

* Thu Apr 11 15:53:36 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.5-1
- Release 1.8.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.0-0.13
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.11.git8cc3a55
- Upload glide files

* Thu Mar 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.10.git8cc3a55
- Bump to 8cc3a55af3bcf171a1c23a90c4df9cf591706104
  related: #1405682

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.9.git18d1596
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.git18d1596
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.7.git18d1596
- Bump to upstream 18d159699f2e83fc5bb9ef2f79465ca3f3122676
  related: #1405682

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.git84398b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.git84398b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.4.git84398b9
- Bump to upstream 84398b94e188ee336f307779b57b3aa91af7063c
  related: #1405682

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.gitf52d055
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.2.gitf52d055
- Polish the spec file
  resolves: #1405682

* Tue Aug 02 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.1.gitf52d055
- First package for Fedora
  resolves: #1362419

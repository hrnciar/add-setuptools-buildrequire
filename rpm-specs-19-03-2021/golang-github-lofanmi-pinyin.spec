# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/Lofanmi/pinyin-golang
%global goipath         github.com/Lofanmi/pinyin-golang
Version:                1.0

%gometa

%global common_description %{expand:
This package provides tools and Golang library to convert Chinese characters
to Pinyin.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Tools and Golang library to convert Chinese characters to Pinyin

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in demo; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Mar 05 23:29:22 CST 2021 Robin Lee <cheeselee@fedoraproject.org> - 1.0-1
- Initial package

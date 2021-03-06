Name:           awscli
Version:        1.19.53
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS

License:        ASL 2.0 and MIT
URL:            https://aws.amazon.com/cli/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     groff
Requires:       python3-docutils
Requires:       python3-colorama
Requires:       python3-s3transfer
Requires:       python3-rsa

%{?python_provide:%python_provide python3-%{name}}

%description
This package provides a unified
command line interface to Amazon Web Services.

%prep
%autosetup -n %{name}-%{version} -p 1
rm -vr %{name}.egg-info
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +

# https://github.com/aws/aws-cli/issues/4837
sed -i "/,<0.16/d" setup.cfg
sed -i "/,<0.16/d" setup.py

# https://bugzilla.redhat.com/show_bug.cgi?id=1854288
sed -i s/4.5.0/4.7/g setup.py
sed -i s/4.5.0/4.7/g setup.cfg

# https://github.com/aws/aws-cli/issues/5795
sed -i s/\<0.4.4/\<=0.4.4/g setup.py
sed -i s/\<0.4.4/\<=0.4.4/g setup.cfg

# https://github.com/aws/aws-cli/issues/5893
sed -i s/\<5.4/\<=5.4.1/g setup.py
sed -i s/\<5.4/\<=5.4.1/g setup.cfg

%build
%py3_build

%install
%py3_install
rm -vf %{buildroot}%{_bindir}/{aws_bash_completer,aws_zsh_completer.sh,aws.cmd}
install -Dpm0644 bin/aws_bash_completer \
  %{buildroot}%{_datadir}/bash-completion/completions/aws
install -Dpm0644 bin/aws_zsh_completer.sh \
  %{buildroot}%{_datadir}/zsh/site-functions/_awscli

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/aws
%{_bindir}/aws_completer
%{python3_sitelib}/awscli/
%{python3_sitelib}/%{name}-*.egg-info/
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/aws
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_awscli

%changelog
* Thu Apr 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.53-1
- 1.19.53

* Thu Apr 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.52-1
- 1.19.52

* Tue Apr 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.51-1
- 1.19.51

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.50-1
- 1.19.50

* Fri Apr 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.49-1
- 1.19.49

* Fri Apr 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.48-1
- 1.19.48

* Wed Apr 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.47-1
- 1.19.47

* Wed Apr 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.46-1
- 1.19.46

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.45-1
- 1.19.45

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.44-1
- 1.19.44

* Thu Apr 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.43-1
- 1.19.43

* Thu Apr 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.42-1
- 1.19.42

* Wed Mar 31 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.41-1
- 1.19.41

* Tue Mar 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.40-1
- 1.19.40

* Mon Mar 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.39-1
- 1.19.39

* Fri Mar 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.37-1
- 1.19.37

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.36-1
- 1.19.36

* Wed Mar 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.35-1
- 1.19.35

* Tue Mar 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.34-1
- 1.19.34

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.33-1
- 1.19.33

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.31-1
- 1.19.31

* Thu Mar 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.30-1
- 1.19.30

* Wed Mar 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.29-1
- 1.19.29

* Tue Mar 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.28-1
- 1.19.28

* Mon Mar 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.27-1
- 1.19.27

* Fri Mar 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.26-1
- 1.19.26

* Thu Mar 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.25-1
- 1.19.25

* Wed Mar 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.24-1
- 1.19.24

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.23-1
- 1.19.23

* Mon Mar 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.22-1
- 1.19.22

* Fri Mar 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.21-1
- 1.19.21

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.20-1
- 1.19.20

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.19-1
- 1.19.19

* Tue Mar 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.18-1
- 1.19.18

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.17-1
- 1.19.17

* Fri Feb 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.16-1
- 1.19.16

* Thu Feb 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.15-1
- 1.19.15

* Wed Feb 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.14-1
- 1.19.14

* Tue Feb 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.13-1
- 1.19.13

* Sat Feb 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.12-1
- 1.19.12

* Fri Feb 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.11-1
- 1.19.11

* Thu Feb 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.10-1
- 1.19.10

* Wed Feb 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.9-1
- 1.19.9

* Tue Feb 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.8-1
- 1.19.8

* Fri Feb 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.6-1
- 1.19.6

* Wed Feb 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.5-1
- 1.19.5

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.4-1
- 1.19.4

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.3-1
- 1.19.3

* Fri Feb 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.2-1
- 1.19.2

* Wed Feb 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.19.0-1
- 1.19.0

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.223-1
- 1.18.223

* Fri Jan 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.222-1
- 1.18.222

* Thu Jan 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.221-1
- 1.18.221

* Wed Jan 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.220-1
- 1.18.220

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.219-2
- Allow pyyaml 5.4.1

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.219-1
- 1.18.219

* Fri Jan 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.218-1
- 1.18.218

* Wed Jan 20 08:21:22 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.217-1
- 1.18.217

* Tue Jan 19 08:29:18 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.216-1
- 1.18.216

* Fri Jan 15 10:51:14 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.215-1
- 1.18.215

* Thu Jan 14 08:20:40 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.214-1
- 1.18.214

* Wed Jan 13 08:36:50 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.213-1
- 1.18.213

* Tue Jan 12 08:20:23 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.212-1
- 1.18.212

* Fri Jan  8 10:53:32 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.211-1
- 1.18.211

* Thu Jan  7 08:34:02 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.210-1
- 1.18.210

* Wed Jan  6 08:16:13 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.209-1
- 1.18.209

* Tue Jan  5 08:40:03 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.208-1
- 1.18.208

* Mon Jan  4 08:34:11 CST 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.18.207-1
- 1.18.207

* Wed Dec 30 16:22:02 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.206-1
- 1.18.206

* Wed Dec 30 08:36:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.205-1
- 1.18.205

* Tue Dec 29 09:15:36 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.204-1
- 1.18.204

* Thu Dec 24 08:37:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.203-1
- 1.18.203

* Wed Dec 23 08:41:55 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.202-1
- 1.18.202

* Tue Dec 22 08:30:57 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.201-1
- 1.18.201

* Fri Dec 18 16:34:01 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.200-1
- 1.18.200

* Fri Dec 18 08:28:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.199-1
- 1.18.199

* Thu Dec 17 08:17:07 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.198-1
- 1.18.198

* Wed Dec 16 08:26:32 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.197-1
- 1.18.197

* Tue Dec 15 08:32:12 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.196-1
- 1.18.196

* Mon Dec 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.195-1
- 1.18.195

* Mon Dec 14 09:20:56 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.194-1
- 1.18.194

* Fri Dec 11 08:14:11 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.193-1
- 1.18.193

* Wed Dec 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.192-1
- 1.18.192

* Tue Dec 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.191-2
- Allow colorama <=0.4.4

* Tue Dec  8 08:24:48 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.191-1
- 1.18.191

* Mon Dec  7 08:27:50 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.190-1
- 1.18.190

* Fri Dec  4 10:08:13 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.189-1
- 1.18.189

* Wed Dec  2 08:26:56 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.188-1
- 1.18.188

* Tue Dec  1 11:53:09 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.186-1
- 1.18.186

* Mon Nov 30 09:21:27 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.185-1
- 1.18.185

* Tue Nov 24 08:26:14 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.184-1
- 1.18.184

* Mon Nov 23 08:27:23 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.183-1
- 1.18.183

* Fri Nov 20 08:15:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.182-1
- 1.18.182

* Thu Nov 19 08:28:00 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.181-1
- 1.18.181

* Wed Nov 18 08:23:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.180-1
- 1.18.180

* Tue Nov 17 09:17:04 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.179-1
- 1.18.179

* Mon Nov 16 08:36:23 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.178-1
- 1.18.178

* Thu Nov 12 15:47:49 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.177-1
- 1.18.177

* Thu Nov 12 10:27:24 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.176-1
- 1.18.176

* Wed Nov 11 09:23:32 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.175-1
- 1.18.175

* Mon Nov  9 14:13:32 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.174-1
- 1.18.174

* Mon Nov  9 09:44:28 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.173-1
- 1.18.173

* Fri Nov  6 08:26:00 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.172-1
- 1.18.172

* Thu Nov  5 15:00:16 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.171-1
- 1.18.171

* Tue Nov  3 08:31:47 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.170-1
- 1.18.170

* Mon Nov  2 09:27:24 CST 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.169-1
- 1.18.169

* Fri Oct 30 08:14:20 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.168-1
- 1.18.168

* Thu Oct 29 08:11:54 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.167-1
- 1.18.167

* Wed Oct 28 09:48:46 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.166-1
- 1.18.166

* Tue Oct 27 09:39:33 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.165-1
- 1.18.165

* Fri Oct 23 16:47:54 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.164-1
- 1.18.164

* Fri Oct 23 08:14:24 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.163-1
- 1.18.163

* Thu Oct 22 08:30:03 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.162-1
- 1.18.162

* Tue Oct 20 21:07:12 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.161-1
- 1.18.161

* Tue Oct 20 08:11:09 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.160-1
- 1.18.160

* Fri Oct 16 14:55:55 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.159-1
- 1.18.159

* Fri Oct 16 08:10:29 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.158-1
- 1.18.158

* Sat Oct 10 16:04:43 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.157-1
- 1.18.157

* Thu Oct  8 14:32:19 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.156-1
- 1.18.156

* Thu Oct  8 09:01:18 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.155-1
- 1.18.155

* Wed Oct  7 08:57:36 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.154-1
- 1.18.154

* Fri Oct  2 15:35:45 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.152-1
- 1.18.152

* Fri Oct  2 08:20:50 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.151-1
- 1.18.151

* Thu Oct  1 08:17:51 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.150-1
- 1.18.150

* Wed Sep 30 09:04:28 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.149-1
- 1.18.149

* Tue Sep 29 09:15:18 CDT 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.148-1
- 1.18.148

* Mon Sep 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.147-1
- 1.18.147

* Fri Sep 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.146-1
- 1.18.146

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.145-1
- 1.18.145

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.144-1
- 1.18.144

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.143-1
- 1.18.143

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.142-1
- 1.18.142

* Fri Sep 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.141-1
- 1.18.141

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.140-1
- 1.18.140

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.139-1
- 1.18.139

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.138-1
- 1.18.138

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.137-1
- 1.18.137

* Fri Sep 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.136-1
- 1.18.136

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.135-1
- 1.18.135

* Wed Sep 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.134-1
- 1.18.134

* Tue Sep 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.133-1
- 1.18.133

* Fri Sep 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.132-1
- 1.18.132

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.131-1
- 1.18.131

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.130-1
- 1.18.130

* Tue Sep 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.129-1
- 1.18.129

* Mon Aug 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.128-1
- 1.18.128

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.127-1
- 1.18.127

* Thu Aug 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.126-1
- 1.18.126

* Tue Aug 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.125-1
- 1.18.125

* Fri Aug 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.124-1
- 1.18.124

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.123-1
- 1.18.123

* Wed Aug 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.122-1
- 1.18.122

* Tue Aug 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.121-1
- 1.18.121

* Mon Aug 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.120-1
- 1.18.120

* Fri Aug 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.119-1
- 1.18.119

* Thu Aug 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.118-1
- 1.18.118

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.117-1
- 1.18.117

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.116-1
- 1.18.116

* Mon Aug 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.115-1
- 1.18.115

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.114-1
- 1.18.114

* Thu Aug 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.113-1
- 1.18.113

* Wed Aug 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.112-1
- 1.18.112

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.111-1
- 1.18.111

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.110-1
- 1.18.110

* Fri Jul 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.109-1
- 1.18.109

* Thu Jul 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.108-1
- 1.18.108

* Wed Jul 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.107-1
- 1.18.107

* Tue Jul 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.106-1
- 1.18.106

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.105-1
- 1.18.105

* Fri Jul 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.104-1
- 1.18.104

* Thu Jul 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.103-1
- 1.18.103

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.102-1
- 1.18.102

* Tue Jul 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.101-1
- 1.18.101

* Mon Jul 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.100-1
- 1.18.100

* Fri Jul 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.99-1
- 1.18.99

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.98-1
- 1.18.98

* Mon Jul 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.97-2
- Re-fix rsa requires.

* Fri Jul 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.97-1
- 1.18.97

* Thu Jul 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.96-1
- 1.18.96

* Wed Jul 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.95-2
- Work around rsa requires.

* Wed Jul 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.95-1
- 1.18.95

* Tue Jul 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.94-1
- 1.18.94

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.93-1
- 1.18.93

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.92-1
- 1.18.92

* Wed Jul 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.91-1
- 1.18.91

* Tue Jun 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.90-1
- 1.18.90

* Sat Jun 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.89-1
- 1.18.89

* Fri Jun 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.88-1
- 1.18.88

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.87-1
- 1.18.87

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.86-1
- 1.18.86

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.85-1
- 1.18.85

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.84-1
- 1.18.84

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.83-1
- 1.18.83

* Thu Jun 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.82-1
- 1.18.82

* Wed Jun 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.81-1
- 1.18.81

* Tue Jun 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.80-1
- 1.18.80

* Sat Jun 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.79-1
- 1.18.79

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.78-1
- 1.18.78

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.77-1
- 1.18.77

* Sat Jun 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.74-1
- 1.18.74

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.73-1
- 1.18.73

* Thu Jun 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.72-1
- 1.18.72

* Tue Jun 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.70-1
- 1.18.70

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.69-1
- 1.18.69

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.18.66-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.66-1
- 1.18.66

* Thu May 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.65-1
- 1.18.65

* Wed May 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.64-1
- 1.18.64

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.61-1
- 1.18.61

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.60-1
- 1.18.60

* Thu May 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.59-1
- 1.18.59

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.58-1
- 1.18.58

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.57-1
- 1.18.57

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.56-1
- 1.18.56

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.55-1
- 1.18.55

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.54-1
- 1.18.54

* Wed May 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.53-1
- 1.18.53

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.52-2
- Patch for docutils version issue.

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.52-1
- 1.18.52

* Sat May 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.51-1
- 1.18.51

* Fri May 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.50-1
- 1.18.50

* Thu Apr 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.49-1
- 1.18.49

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.48-1
- 1.18.48

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.47-1
- 1.18.47

* Sat Apr 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.46-1
- 1.18.46

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.45-1
- 1.18.45

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.44-1
- 1.18.44

* Wed Apr 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.43-1
- 1.18.43

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.42-1
- 1.18.42

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.41-1
- 1.18.41

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.40-1
- 1.18.40

* Thu Apr 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.39-1
- 1.18.39

* Wed Apr 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.38-1
- 1.18.38

* Tue Apr 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.37-1
- 1.18.37

* Mon Apr 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.36-1
- 1.18.36

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.35-1
- 1.18.35

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.34-1
- 1.18.34

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.33-1
- 1.18.33

* Mon Mar 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.32-1
- 1.18.32

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.31-1
- 1.18.31

* Fri Mar 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.30-1
- 1.18.30

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.29-1
- 1.18.29

* Wed Mar 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.28-1
- 1.18.28

* Tue Mar 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.27-1
- 1.18.27

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.26-1
- 1.18.26

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.25-1
- 1.18.25

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.24-1
- 1.8.24

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.23-1
- 1.8.23

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.22-1
- 1.18.22

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.21-1
- 1.18.21

* Fri Mar 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.20-1
- 1.18.20

* Thu Mar 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.19-1
- 1.18.19

* Wed Mar 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.18-1
- 1.18.18

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.17-1
- 1.18.17

* Sun Mar 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.16-1
- 1.18.16

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.15-1
- 1.18.15

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.14-1
- 1.18.14

* Wed Mar 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.13-1
- 1.18.13

* Tue Mar 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.12-1
- 1.18.12

* Fri Feb 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.18.9-1
- 1.18.9

* Thu Feb 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.18.8-1
- Update to 1.18.8

* Fri Feb 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.12-1
- Update to 1.17.12

* Wed Jan 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.9-1
- Update to 1.17.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.309-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 David Duncan <davdunc@amazon.com> - 1.16.266-1
- Merge changes from 1.16.266 release.

* Mon Oct 21 2019 James Hogarth <james.hogarth@gmail.com> - 1.16.263-2
- Fix changelog syntax
- Remove unused patchfile

* Sat Oct 19 2019 David Duncan <davdunc@amazon.com> - 1.16.263-1
- Merge changes from 1.16.263 release.

* Thu Oct 10 2019 David Duncan <davdunc@amazon.com> - 1.16.253-2
- Merge changes from 1.16.253 release.
- Remove relax-dependencies patch requirement. 

* Fri Oct 04 2019 David Duncan <davdunc@amazon.com> - 1.16.253-1
- Merge changes from 1.16.253 release.

* Thu Oct 03 2019 David Duncan <davdunc@amazon.com> - 1.16.252-1
- Merge changes from 1.16.252 release.

* Thu Oct 03 2019 David Duncan <davdunc@amazon.com> - 1.16.251-1
- Merge changes from 1.16.251 release.

* Tue Oct 01 2019 David Duncan <davdunc@amazon.com> - 1.16.250-1
- Merge changes from 1.16.250 release.

* Mon Sep 30 2019 David Duncan <davdunc@amazon.com> - 1.16.249-1
- Merge changes from 1.16.249 release.

* Sat Sep 28 2019 David Duncan <davdunc@amazon.com> - 1.16.248-1
- Merge changes from 1.16.248 release.

* Thu Sep 26 2019 David Duncan <davdunc@amazon.com> - 1.16.247-1
- Merge changes from 1.16.247 release.

* Wed Sep 25 2019 David Duncan <davdunc@amazon.com> - 1.16.246-1
- Merge changes from 1.16.246 release.

* Sun Sep 22 2019 David Duncan <davdunc@amazon.com> - 1.16.243-1
- Merge changes from 1.16.243 release.

* Thu Sep 19 2019 David Duncan <davdunc@amazon.com - 1.16.241-1
- Update to 1.16.241
 
* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.235-2
- Rebuild with correct patch.

* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.235-1
- Update to 1.16.235.

* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-3
- Rebuild for new python-botocore 1.12.225

* Wed Aug 21 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-2
- Re-add mistakenly dropped patch.

* Wed Aug 21 2019 Kevin Fenzi <kevin@scrye.com> - 1.16.222-1
- Update to 1.16.222

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.16.198-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.198-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 David Duncan <davdunc@amazon.com> - 1.16.198-1
- Update to 1.16.198
- Add updates and fixes

* Tue May 28 2019 David Duncan <davdunc@amazon.com> - 1.16.167-1
- Update to 1.16.167
- Add updates and fixes

* Wed Apr 24 2019 David Duncan <davdunc@amazon.com> - 1.16.145-1
- Adding support for ap-east-1 

* Thu Mar 21 2019 David Duncan <davdunc@amazon.com> - 1.16.129-1
- Bumping version to 1.16.129

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.111-1
- Update to 1.16.111

* Mon Feb 11 2019 David Duncan <davdunc@amazon.com> - 1.16.101
- api-change:ecs: Update ecs command to latest version
- api-change:discovery: Update discovery command to latest version
- api-change:dlm: Update dlm command to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.16.85-2
- Enable python dependency generator

* Mon Nov 19 2018 David Duncan <davdunc@amazon.com> - 1.16.57-1
- Update to 1.16.57. Fixes bug #1613078

* Tue Nov 06 2018 Carl George <carl@george.computer> - 1.16.28-3
- Add patch0 to relax dependencies

* Wed Oct 17 2018 Justin W. Flory <jflory7@fedoraproject.org> - 1.16.28-2
- Add groff dependency, fix 'aws help' issue in stock install

* Sun Oct 07 2018 David Duncan <davdunc@amazon.com> - 1.16.28
- Update to 1.16.28

* Sun Sep 02 2018 David Duncan <davdunc@amazon.com> - 1.15.72-1
- Update to 1.15.72. Updates bug #1613078

* Sun Aug 05 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.71-1
- Update to 1.15.71. Fixes bug #1612393

* Fri Aug 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.70-1
- Update to 1.15.70. Fixes bug #1611853

* Wed Aug 01 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.69-1
- Update to 1.15.69. Fixes bug #1610059

* Fri Jul 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.66-1
- Update to 1.15.66. Fixes bug #1609074

* Thu Jul 26 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.65-1
- Update to 1.15.65. Fixes bug #1608097

* Sun Jul 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.63-1
- Update to 1.15.63. Fixes bug #1606924

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.62-1
- Update to 1.15.62. Fixes bug #1602972

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.60-1
- Update to 1.15.60. Fixes bug #1602176

* Sun Jul 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.59-1
- Update to 1.15.59. Fixes bug #1599467

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.53-1
- Update to 1.15.53. Fixes bug #1598936

* Thu Jul 05 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.52-1
- Update to 1.15.52. Fixes bug #1598597

* Wed Jul 04 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.51-2
- Update to 1.15.51. Fixes bug #1596663

* Mon Jul 02 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.15.48-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.48-1
- Update to 1.14.48. Fixes bug #1596420

* Thu Jun 28 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.47-1
- Update to 1.14.47. Fixes bug #1595469

* Sat Jun 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.45-1
- Update to 1.14.45. Fixes bug #1594465

* Fri Jun 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.44-1
- Update to 1.14.44. Fixes bug #1594038

* Fri Jun 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.43-1
- Update to 1.14.43. Fixes bug #1594038
- Fix python-botocore version to match new python-botocore.

* Wed Jun 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.42-1
- Update to 1.14.42. Fixes bug #1593483

* Wed Jun 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.41-1
- Update to 1.15.41. Fixes bug #1593040

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.15.40-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.40-1
- Update to 1.15.40. Fixes bug #1591986

* Fri Jun 15 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.39-1
- Update to 1.15.39. Fixes bug #1591048

* Tue Jun 12 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.37-1
- Update to 1.15.37. Fixes bug #1590039

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.35-1
- Update to 1.15.35. Fixes bug #1588851

* Wed Jun 06 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.33-1
- Update to 1.15.33. Fixes bug #1586055

* Sun Jun 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.31-1
- Update to 1.15.31. Fixes bug #1583867

* Sun May 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.28-1
- Update to 1.15.28. Fixes bug #1580992

* Fri May 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.24-1
- Update to 1.15.24. Fixes bug #1579995

* Fri May 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.23-1
- Update to 1.15.23. Fixes bug #1579573

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.22-1
- Update to 1.15.22. Fixes bug #1579086

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.21-1
- Update to 1.15.21. Fixes bug #1578162

* Fri May 11 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.19-1
- Update to 1.15.19. Fixes bug #1574745

* Wed May 02 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.12-1
- Update to 1.15.12. Fixes bug #1574052

* Fri Apr 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.10-1
- Update to 1.15.10. Fixes bug #1572396

* Thu Apr 26 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.9-1
- Update to 1.15.9. Fixes bug #1571002

* Mon Apr 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.6-1
- Update to 1.15.6. Fixes bug #1570216

* Fri Apr 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.5-1
- Update to 1.15.5. Fixes bug #1569974

* Sat Apr 14 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.4-1
- Update to 1.15.4. Fixes bug #1565379

* Sat Apr 07 2018 Kevin Fenzi <kevin@scrye.com>  - 1.15.2-1
- Update to 1.15.2. Fixes bug #1563195

* Sat Mar 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.68-1
- Update to 1.4.68. Fixes bug #1561240

* Tue Mar 27 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.64-1
- Update to 1.4.64. Fixes bug #1560762

* Sun Mar 25 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.63-1
- Update to 1.4.63. Fixes bug #1559367

* Fri Mar 23 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.62-1
- Update to 1.4.62. Fixes bug #1559367

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.60-1
- Update to 1.4.60. Fixes bug #1559193

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.59-1
- Update to 1.4.59. Fixes bug #1558758

* Sat Mar 17 2018 Kevin Fenzi <kevin@scrye.com>  - 1.14.58-1
- Update to 1.4.58. Fixes bug #1555085

* Tue Mar 13 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.55-1
- Update to 1.4.55. Fixes bug #1555085

* Tue Mar 13 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.54-1
- Update to 1.14.54. Fixes bug #1554552

* Thu Mar 08 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.53-1
- Update to 1.14.53. Fixes bug 1552345

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.50-2
- Update for new python-botocore.

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.50-1
- Update to 1.14.50. Fixes bug #1550746

* Thu Mar 01 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.49-1
- Update to 1.14.49. Fixes bug #1549549

* Sat Feb 24 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.46-1
- Update to 1.14.46. Fixes bug #1546901

* Sat Feb 17 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.41-1
- Update to 1.14.41. Fixes bug #1546437

* Fri Feb 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.40-1
- Update to 1.14.40. Fixes bug #1544045

* Thu Feb 08 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.34-1
- Update to 1.14.34. Fixes bug #1543659

* Wed Feb 07 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.33-1
- Update to 1.14.33. Fixes bug #1542468

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.32-2
- Fix python-botocore version requirement.

* Wed Jan 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.14.32-1
- Update to 1.14.32. Fixes bug #1481464

* Sun Aug 13 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.133-1
- Update to 1.11.133

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.109-2
- Forgot to update

* Wed Jun 21 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.109-1
- Update to 1.11.109

* Tue May 23 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.90-1
- Update to 1.11.90

* Wed Mar 15 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.63-1
- Update to 1.11.63

* Sat Feb 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.55-1
- Update to 1.11.55

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.40-1
- Update to 1.11.40

* Wed Dec 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.34-2
- Update to 1.11.34

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.11.28-3
- Rebuild for Python 3.6

* Tue Dec 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.28-2
- Add PyYAML dependency

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.28-1
- Update to 1.11.28

* Sat Dec 03 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.24-1
- Update to 1.11.24

* Thu Nov 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.21-1
- Update to 1.11.21

* Mon Oct 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.12-1
- Update to 1.11.12

* Sun Oct 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Wed Sep 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.67-1
- Update to 1.10.67

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.62-1
- Update to 1.10.62

* Wed Aug 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.59-1
- Update to current upstream version

* Fri Aug 05 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.53-1
- Update to current upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.45-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.45-1
- Update to current upstream version

* Wed Jun 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.36-1
- Update to current upstream version

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.34-1
- Update to current upstream version

* Wed Feb 24 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.7-1
- Update to current upstream version

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.6-2
- Fix broken dependency

* Fri Feb 19 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.6-1
- Update to current upstream version

* Wed Feb 17 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.5-1
- Update to current upstream version

* Fri Feb 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.4-1
- Update to current upstream version

* Wed Feb 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.3-1
- Update to current upstream version

* Tue Feb 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.2-1
- Update to current upstream version

* Tue Feb 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.1-1
- Update to current upstream version

* Fri Jan 22 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.0-1
- Update to current upstream version

* Wed Jan 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.21-1
- Update to current upstream version
- Don't fix documentation permissions any more (pull request merged)

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.920-1
- Update to current upstream version

* Fri Jan 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.19-1
- Update to current upstream version
- Don't substitue the text of bin/aws_bash_completer anymore (pull request merged)
- Don't remove the shabang from awscli/paramfile.py anymore (pull request merged)

* Wed Jan 13 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.18-1
- Update to current upstream version
- Fix completion for bash
- Remove bcdoc dependency that is not used anymore

* Sun Jan 10 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.17-1
- Update to current upstream version
- Lock the botocore dependency version

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.16-1
- Update to current upstream version
- Add dir /usr/share/zsh
- Add dir /usr/share/zsh/site-functions
- Add MIT license (topictags.py is MIT licensed)
- Move dependency from python-devel to python2-devel
- Add Recommends lines for zsh and bsah-completion for Fedora
- Remove BuildReuires: bash-completion
- Remove the macros py2_build and py2_install to prefer the extended form
- Force non-executable bit for documentation
- Remove shabang from awscli/paramfile.py
- Fix bash completion
- Fix zsh completion
- Remove aws.cmd

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.15-1
- Initial package.

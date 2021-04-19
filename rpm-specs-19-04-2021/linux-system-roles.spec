%if 0%{?rhel} && ! 0%{?epel}
%bcond_with ansible
%else
%bcond_without ansible
%endif

%if 0%{?rhel}
Name: rhel-system-roles
%else
Name: linux-system-roles
%endif
Url: https://github.com/linux-system-roles/
Summary: Set of interfaces for unified system management
Version: 1.0.1
Release: 1%{?dist}

#Group: Development/Libraries
License: GPLv3+ and MIT and BSD
%global installbase %{_datadir}/linux-system-roles
%global _pkglicensedir %{_licensedir}/%{name}
%global rolealtprefix linux-system-roles.
%global roleprefix %{name}.
%global roleinstprefix %{nil}
%global rolealtrelpath ../../linux-system-roles/
%if 0%{?rhel}
%global roleinstprefix %{roleprefix}
%global installbase %{_datadir}/ansible/roles
%global rolealtrelpath %{nil}
%endif

%if 0%{?rhel}
%global collection_namespace redhat
%global collection_name rhel_system_roles
%else
%global collection_namespace fedora
%global collection_name linux_system_roles
%endif
%global subrole_prefix "private_${role}_subrole_"

%global collection_version %{version}

# Helper macros originally from macros.ansible by Igor Raits <ignatenkobrain>
# Not available on RHEL, so we must define those macros locally here without using ansible-galaxy

# Not used (yet). Could be made to point to AH in RHEL - but what about CentOS Stream?
#%%{!?ansible_collection_url:%%define ansible_collection_url() https://galaxy.ansible.com/%%{collection_namespace}/%%{collection_name}}

%{!?ansible_collection_files:%define ansible_collection_files %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/}

%if %{with ansible}
BuildRequires: ansible >= 2.9.10
%endif

%if %{undefined ansible_collection_build}
%if %{without ansible}
# Empty command. We don't have ansible-galaxy.
%define ansible_collection_build() :
%else
%define ansible_collection_build() ansible-galaxy collection build
%endif
%endif

%if %{undefined ansible_collection_install}
%if %{without ansible}
# Simply copy everything instead of galaxy-installing the built artifact.
%define ansible_collection_install() mkdir -p %{buildroot}%{ansible_collection_files}; cp -a . %{buildroot}%{ansible_collection_files}/%{collection_name}/
%else
%define ansible_collection_install() ansible-galaxy collection install -n -p %{buildroot}%{_datadir}/ansible/collections %{collection_namespace}-%{collection_name}-%{version}.tar.gz
%endif
%endif

# For each role, call either defcommit() or deftag(). The other macros
# (%%id and %%shortid) can be then used in the same way in both cases.
# This way  the rest of the spec file des not need to know whether we are
# dealing with a tag or a commit.
%global archiveext tar.gz
# list of role names
%global rolenames %nil
# list of assignments that can be used to populate a bash associative array variable
%global rolestodir %nil
%define getarchivedir() %(p=%{basename:%{S:%{1}}}; echo ${p%%.%{archiveext}})

%define defcommit() %{expand:%%global ref%{1} %{2}
%%global shortcommit%{1} %%(c=%%{ref%{1}}; echo ${c:0:7})
%%global extractdir%{1} %%{expand:%%getarchivedir %{1}}
%%{!?repo%{1}:%%global repo%{1} %%{rolename%{1}}}
%%global archiveurl%{1} %%{?forgeorg%{1}}%%{!?forgeorg%{1}:%%{url}}%%{repo%{1}}/archive/%%{ref%{1}}/%%{repo%{1}}-%%{ref%{1}}.tar.gz
%%global rolenames %%{?rolenames} %%{rolename%{1}}
%%global roletodir%{1} [%{rolename%{1}}]="%{extractdir%{1}}"
%%global rolestodir %%{?rolestodir} %{roletodir%{1}}
}

%define deftag() %{expand:%%global ref%{1} %{2}
%%global extractdir%{1} %%{expand:%%getarchivedir %{1}}
%%{!?repo%{1}:%%global repo%{1} %%{rolename%{1}}}
%%global archiveurl%{1} %%{?forgeorg%{1}}%%{!?forgeorg%{1}:%%{url}}%%{repo%{1}}/archive/%%{ref%{1}}/%%{repo%{1}}-%%{ref%{1}}.tar.gz
%%global rolenames %%{?rolenames} %%{rolename%{1}}
%%global roletodir%{1} [%{rolename%{1}}]="%{extractdir%{1}}"
%%global rolestodir %%{?rolestodir} %%{roletodir%{1}}
}

#%%defcommit 1 43eec5668425d295dce3801216c19b1916df1f9b
%global rolename1 postfix
%deftag 1 0.1

#%%defcommit 2 6cd1ec8fdebdb92a789b14e5a44fe77f0a3d8ecd
%global rolename2 selinux
%deftag 2 1.1.1

%defcommit 3 924650d0cd4117f73a7f0413ab745a8632bc5cec
%global rolename3 timesync
#%%deftag 3 1.0.0

%defcommit 4 77596fdd976c6160d6152c200a5432c609725a14
%global rolename4 kdump
#%%deftag 4 1.0.0

%defcommit 5 bda206d45c87ee8c1a5284de84f5acf5e629de97
%global rolename5 network
#%%deftag 5 1.0.0

%defcommit 6 485de47b0dc0787aea077ba448ecb954f53e40c4
%global rolename6 storage
#%%deftag 6 1.2.2

%defcommit 7 e81b2650108727f38b1c856699aad26af0f44a46
%global rolename7 metrics
#%%deftag 7 0.1.0

#%%defcommit 8 cfa70b6b5910b3198aba2679f8fc36aad45ca45a
%global rolename8 tlog
%deftag 8 1.1.0

%defcommit 9 4c81fd1380712ab0641b6837f092dd9caeeae0a6
%global rolename9 kernel_settings
#%%deftag 9 1.0.1

%defcommit 10 07e08107e7ccba5822f8a7aaec1a2ff0a221bede
%global rolename10 logging
#%%deftag 10 0.2.0

%defcommit 11 4dfc5e2aca74cb82f2a50eec7e975a2b78ad9678
%global rolename11 nbde_server
#%%deftag 11 1.0.1

%defcommit 12 19f06159582550c8463f7d8492669e26fbdf760b
%global rolename12 nbde_client
#%%deftag 12 1.0.1

%defcommit 13 0376ceece57882ade8ffaf431b7866aae3e7fed1
%global rolename13 certificate
#%%deftag 13 1.0.1

%defcommit 14 2e2941c5545571fc8bc494099bdf970f498b9d38
%global rolename14 crypto_policies

%global forgeorg15 https://github.com/willshersystems/
%global repo15 ansible-sshd
%global rolename15 sshd
%defcommit 15 e1de59b3c54e9d48a010eeca73755df339c7e628

%defcommit 16 21adc637511db86b5ba279a70a7301ef3a170669
%global rolename16 ssh

%defcommit 17 779bb78559de58bb5a1f25a4b92039c373ef59a4
%global rolename17 ha_cluster

%global mainid 8f069305caa0a142c2c6ac14bd4d331282a1c079
Source: %{url}auto-maintenance/archive/%{mainid}/auto-maintenance-%{mainid}.tar.gz
Source1: %{archiveurl1}
Source2: %{archiveurl2}
Source3: %{archiveurl3}
Source4: %{archiveurl4}
Source5: %{archiveurl5}
Source6: %{archiveurl6}
Source7: %{archiveurl7}
Source8: %{archiveurl8}
Source9: %{archiveurl9}
Source10: %{archiveurl10}
Source11: %{archiveurl11}
Source12: %{archiveurl12}
Source13: %{archiveurl13}
Source14: %{archiveurl14}
Source15: %{archiveurl15}
Source16: %{archiveurl16}
Source17: %{archiveurl17}

# Script to convert the collection README to Automation Hub.
# Not used on Fedora.
Source998: collection_readme.sh

Patch11: rhel-system-roles-postfix-pr5.diff
Patch12: postfix-meta-el8.diff

Patch21: selinux-tier1-tags.diff
Patch22: selinux-bz-1926947-no-variable-named-present.diff
Patch23: selinux-ansible-test-issues.diff

Patch31: timesync-tier1-tags.diff
Patch32: timesync-ansible-test-issues.diff

Patch41: rhel-system-roles-kdump-pr22.diff
Patch42: kdump-tier1-tags.diff
Patch43: kdump-meta-el8.diff
Patch44: kdump-fix-newline.diff

Patch51: network-epel-minimal.diff
# Not suitable for upstream, since the files need to be executable there
Patch52: network-permissions.diff
Patch53: network-tier1-tags.diff
Patch55: network-disable-bondtests.diff
Patch56: network-pr353.diff
Patch57: network-ansible-test.diff

Patch62: storage-partition-name.diff
Patch63: storage-no-disks-existing.diff
Patch64: storage-trim-volume-size.diff
Patch65: storage-ansible-test.diff

Patch71: metrics-mssql-x86.diff

Patch151: sshd-example.diff
Patch152: sshd-work-on-ansible28-jinja27.diff

BuildArch: noarch

# These are needed for md2html.sh to build the documentation
BuildRequires: asciidoc
BuildRequires: pandoc
BuildRequires: highlight
BuildRequires: python3
BuildRequires: python3-six
BuildRequires: python3dist(ruamel.yaml)

Requires: python3-jmespath

Obsoletes: rhel-system-roles-techpreview < 1.0-3

%if %{undefined __ansible_provides}
Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{collection_version}
%endif
# be compatible with the usual Fedora Provides:
Provides: ansible-collection-%{collection_namespace}-%{collection_name} = %{version}-%{release}

# We need to put %%description within the if block to avoid empty
# lines showing up.
%if 0%{?rhel}
%description
Collection of Ansible roles and modules that provide a stable and
consistent configuration interface for managing multiple versions
of Red Hat Enterprise Linux.
%else
%description
Collection of Ansible roles and modules that provide a stable and
consistent configuration interface for managing multiple versions
of Fedora, Red Hat Enterprise Linux & CentOS.
%endif

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -n %{getarchivedir 0}

declare -A ROLESTODIR=(%{rolestodir})
for rolename in %{rolenames}; do
    mv "${ROLESTODIR[${rolename}]}" ${rolename}
done

cd %{rolename1}
%patch11 -p1
%patch12 -p1
cd ..
cd %{rolename2}
%patch21 -p1
%patch22 -p1
%patch23 -p1
cd ..
cd %{rolename3}
%patch31 -p1
%patch32 -p1
cd ..
cd %{rolename4}
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
cd ..
cd %{rolename5}
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
cd ..
cd %{rolename6}
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
cd ..
cd %{rolename7}
%patch71 -p1
cd ..
cd %{rolename15}
%patch151 -p1
%patch152 -p1
sed -r -i -e "s/ansible-sshd/linux-system-roles.sshd/" tests/*.yml examples/*.yml README.md
cd ..

# Replacing "linux-system-roles.rolename" with "rhel-system-roles.rolename" in each role
%if "%{roleprefix}" != "linux-system-roles."
for rolename in %{rolenames}; do
    find $rolename -type f -exec \
         sed "s/linux-system-roles[.]${rolename}\\>/%{roleprefix}${rolename}/g" -i {} \;
done
%endif

# Removing symlinks in tests/roles
for rolename in %{rolenames}; do
    if [ -d ${rolename}/tests/roles ]; then
        find ${rolename}/tests/roles -type l -exec rm {} \;
        if [ -d ${rolename}/tests/roles/linux-system-roles.${rolename} ]; then
            rm -r ${rolename}/tests/roles/linux-system-roles.${rolename}
        fi
    fi
done
rm %{rolename5}/tests/modules
rm %{rolename5}/tests/module_utils
rm %{rolename5}/tests/playbooks/roles

# transform ambiguous #!/usr/bin/env python shebangs to python3 to stop brp-mangle-shebangs complaining
find -type f -executable -name '*.py' -exec \
     sed -i -r -e '1s@^(#! */usr/bin/env python)(\s|$)@#\13\2@' '{}' +

%build
sh md2html.sh \
%{rolename1}/README.md \
%{rolename2}/README.md \
%{rolename3}/README.md \
%{rolename4}/README.md \
%{rolename5}/README.md \
%{rolename6}/README.md \
%{rolename7}/README.md \
%{rolename8}/README.md \
%{rolename9}/README.md \
%{rolename10}/README.md \
%{rolename11}/README.md \
%{rolename12}/README.md \
%{rolename13}/README.md \
%{rolename14}/README.md \
%{rolename15}/README.md \
%{rolename16}/README.md \
%{rolename17}/README.md

mkdir .collections
%if 0%{?rhel}
# Convert the upstream collection readme to the downstream one
%{SOURCE998} lsr_role2collection/collection_readme.md
%endif
./galaxy_transform.py "%{collection_namespace}" "%{collection_name}" "%{collection_version}" "Red Hat Enterprise Linux System Roles Ansible Collection" > galaxy.yml.tmp
mv galaxy.yml.tmp galaxy.yml

for role in %{rolenames}; do
    python3 lsr_role2collection.py --role "$role" --src-path "$role" \
        --src-owner %{name} --subrole-prefix %{subrole_prefix} --dest-path .collections \
        --readme lsr_role2collection/collection_readme.md \
        --namespace %{collection_namespace} --collection %{collection_name}
done

rm -f .collections/ansible_collections/%{collection_namespace}/%{collection_name}/tests/sanity/ignore-2.9.txt
# Merge .sanity-ansible-ignore-2.9-ROLENAME.txt into tests/sanity/ignore-2.9.txt
mkdir -p .collections/ansible_collections/%{collection_namespace}/%{collection_name}/tests/sanity
for role in %{rolenames}; do
    if [ -f .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.sanity-ansible-ignore-2.9-"$role".txt ];
    then
      cat .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.sanity-ansible-ignore-2.9-"$role".txt \
        >> .collections/ansible_collections/%{collection_namespace}/%{collection_name}/tests/sanity/ignore-2.9.txt
      rm -f .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.sanity-ansible-ignore-*-"$role".txt
    fi
done

# removing dot files/dirs
rm -r .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.[A-Za-z]*

cp -p galaxy.yml lsr_role2collection/.ansible-lint \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}

# converting README.md to README.html
sh md2html.sh -l \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename1}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename2}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename3}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename4}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename5}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename6}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename7}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename8}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename9}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename10}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename11}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename12}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename13}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename14}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename15}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename16}/README.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{rolename17}/README.md

cd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_build

%install
mkdir -p $RPM_BUILD_ROOT%{installbase}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles

cp -pR %{rolename1}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename1}
cp -pR %{rolename2}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename2}
cp -pR %{rolename3}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename3}
cp -pR %{rolename4}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename4}
cp -pR %{rolename5}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename5}
cp -pR %{rolename6}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename6}
cp -pR %{rolename7}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename7}
cp -pR %{rolename8}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename8}
cp -pR %{rolename9}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename9}
cp -pR %{rolename10}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename10}
cp -pR %{rolename11}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename11}
cp -pR %{rolename12}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename12}
cp -pR %{rolename13}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename13}
cp -pR %{rolename14}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename14}
cp -pR %{rolename15}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename15}
cp -pR %{rolename16}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename16}
cp -pR %{rolename17}      $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}%{rolename17}

%if 0%{?rolealtprefix:1}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename1}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename1}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename2}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename2}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename3}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename3}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename4}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename4}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename5}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename5}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename6}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename6}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename7}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename7}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename8}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename8}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename9}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename9}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename10}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename10}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename11}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename11}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename12}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename12}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename13}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename13}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename14}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename14}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename15}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename15}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename16}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename16}
ln -s    %{rolealtrelpath}%{roleinstprefix}%{rolename17}   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{rolealtprefix}%{rolename17}
%endif

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/kdump
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/postfix
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/selinux
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/timesync
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/network
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/storage
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/metrics
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/tlog
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/kernel_settings
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/logging
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/nbde_server
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/nbde_client
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/certificate
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/crypto_policies
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/sshd
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/ssh
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/ha_cluster
mkdir -p $RPM_BUILD_ROOT%{_pkglicensedir}

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kdump/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kdump/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/kdump
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kdump/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/kdump.COPYING

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}postfix/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}postfix/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/postfix
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}postfix/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/postfix.COPYING

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}selinux/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}selinux/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/selinux
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}selinux/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/selinux.COPYING
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}selinux/selinux-playbook.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/selinux/example-selinux-playbook.yml

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}timesync/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}timesync/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/timesync
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}timesync/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/timesync.COPYING
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}timesync/examples/multiple-ntp-servers.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/timesync/example-timesync-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}timesync/examples/single-pool.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/timesync/example-timesync-pool-playbook.yml

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/network.LICENSE
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/bond_with_vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-bond_with_vlan-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/bridge_with_vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-bridge_with_vlan-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/eth_simple_auto.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth_simple_auto-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/eth_with_vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth_with_vlan-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/infiniband.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-infiniband-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/macvlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-macvlan-playbook.yml
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/remove_profile.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-remove_profile-playbook.yml
rm $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/remove_profile.yml
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/down_profile.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-down_profile-playbook.yml
rm $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/down_profile.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/inventory \
   $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-inventory
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/ethtool_features.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-ethtool_features-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/ethtool_features_default.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-ethtool_features_default-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/bond_simple.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-bond_simple-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/eth_with_802_1x.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth_with_802_1x-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/wireless_wpa_psk.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-wireless_wpa_psk-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/remove+down_profile.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-remove+down_profile-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/dummy_simple.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-dummy_simple-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/ethtool_coalesce.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-ethtool_coalesce-playbook.yml
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/team_simple.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-team_simple-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/eth_dns_support.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth_dns_support-playbook.yml

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}storage/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}storage/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/storage
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}storage/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/storage.LICENSE

rm $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}*/semaphore
rm -r $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}*/molecule

rm -r $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}*/.[A-Za-z]*
rm $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}*/tests/.git*

rm $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples/roles
rmdir $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}network/examples

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}metrics/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}metrics/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/metrics
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}metrics/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/metrics.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}tlog/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}tlog/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/tlog
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}tlog/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/tlog.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kernel_settings/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kernel_settings/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/kernel_settings
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kernel_settings/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/kernel_settings.LICENSE
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}kernel_settings/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/kernel_settings.COPYING

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}logging/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}logging/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/logging
cp -p  $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}logging/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/logging.LICENSE
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}logging/COPYING \
    $RPM_BUILD_ROOT%{_pkglicensedir}/logging.COPYING

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_server/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_server/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/nbde_server
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_server/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/nbde_server.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_client/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_client/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/nbde_client
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}nbde_client/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/nbde_client.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}certificate/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}certificate/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/certificate
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}certificate/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/certificate.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}crypto_policies/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}crypto_policies/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/crypto_policies
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}crypto_policies/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/crypto_policies.LICENSE

cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}sshd/README.md \
    $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}sshd/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/sshd
cp -p $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}sshd/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/sshd.LICENSE
# referenced in the configuring-openssh-servers-using-the-sshd-system-role documentation module
# must be updated if changing the file path
mv $RPM_BUILD_ROOT%{installbase}/%{roleinstprefix}sshd/examples/example-root-login.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/sshd/example-root-login-playbook.yml
rmdir $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}sshd/examples

cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ssh/README.md \
    $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ssh/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/ssh
cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ssh/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/ssh.LICENSE

cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ha_cluster/README.md \
    $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ha_cluster/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/ha_cluster
cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ha_cluster/LICENSE \
    $RPM_BUILD_ROOT%{_pkglicensedir}/ha_cluster.LICENSE
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ha_cluster/examples/simple.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/ha_cluster/example-simple-playbook.yml
rmdir $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ha_cluster/examples

cd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_install

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/collection
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/collection/roles

cp -p %{buildroot}%{ansible_collection_files}%{collection_name}/README.md \
    %{buildroot}%{ansible_collection_files}%{collection_name}/README.html \
    $RPM_BUILD_ROOT%{_pkgdocdir}/collection

for rolename in %{rolenames}; do
  if [ -f %{buildroot}%{ansible_collection_files}%{collection_name}/roles/${rolename}/README.md ]; then
    mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/collection/roles/${rolename}
    cp -p %{buildroot}%{ansible_collection_files}%{collection_name}/roles/${rolename}/README.md \
        %{buildroot}%{ansible_collection_files}%{collection_name}/roles/${rolename}/README.html \
        $RPM_BUILD_ROOT%{_pkgdocdir}/collection/roles/${rolename}
  fi
done


%files
%if %{without ansible}
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/roles
%endif
%if "%{installbase}" != "%{_datadir}/ansible/roles"
%dir %{installbase}
%endif
%if 0%{?rolealtprefix:1}
%{_datadir}/ansible/roles/%{rolealtprefix}kdump
%{_datadir}/ansible/roles/%{rolealtprefix}postfix
%{_datadir}/ansible/roles/%{rolealtprefix}selinux
%{_datadir}/ansible/roles/%{rolealtprefix}timesync
%{_datadir}/ansible/roles/%{rolealtprefix}network
%{_datadir}/ansible/roles/%{rolealtprefix}storage
%{_datadir}/ansible/roles/%{rolealtprefix}metrics
%{_datadir}/ansible/roles/%{rolealtprefix}tlog
%{_datadir}/ansible/roles/%{rolealtprefix}kernel_settings
%{_datadir}/ansible/roles/%{rolealtprefix}logging
%{_datadir}/ansible/roles/%{rolealtprefix}nbde_server
%{_datadir}/ansible/roles/%{rolealtprefix}nbde_client
%{_datadir}/ansible/roles/%{rolealtprefix}certificate
%{_datadir}/ansible/roles/%{rolealtprefix}crypto_policies
%{_datadir}/ansible/roles/%{rolealtprefix}sshd
%{_datadir}/ansible/roles/%{rolealtprefix}ssh
%{_datadir}/ansible/roles/%{rolealtprefix}ha_cluster
%endif
%{installbase}/%{roleinstprefix}kdump
%{installbase}/%{roleinstprefix}postfix
%{installbase}/%{roleinstprefix}selinux
%{installbase}/%{roleinstprefix}timesync
%{installbase}/%{roleinstprefix}network
%{installbase}/%{roleinstprefix}storage
%{installbase}/%{roleinstprefix}metrics
%{installbase}/%{roleinstprefix}tlog
%{installbase}/%{roleinstprefix}kernel_settings
%{installbase}/%{roleinstprefix}logging
%{installbase}/%{roleinstprefix}nbde_server
%{installbase}/%{roleinstprefix}nbde_client
%{installbase}/%{roleinstprefix}certificate
%{installbase}/%{roleinstprefix}crypto_policies
%{installbase}/%{roleinstprefix}sshd
%{installbase}/%{roleinstprefix}ssh
%{installbase}/%{roleinstprefix}ha_cluster
%{_pkgdocdir}/*/example-*-playbook.yml
%{_pkgdocdir}/network/example-inventory
%{_pkgdocdir}/*/README.md
%{_pkgdocdir}/*/README.html
%{_pkgdocdir}/collection/roles/*/README.md
%{_pkgdocdir}/collection/roles/*/README.html
%doc %{installbase}/%{roleinstprefix}*/README.md
%doc %{installbase}/%{roleinstprefix}*/README.html
%doc %{ansible_collection_files}/%{collection_name}/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/kdump/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/postfix/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/selinux/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/timesync/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/network/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/storage/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/metrics/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/tlog/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/kernel_settings/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/logging/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/nbde_server/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/nbde_client/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/certificate/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/crypto_policies/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/sshd/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/ssh/README.md
%doc %{ansible_collection_files}/%{collection_name}/roles/ha_cluster/README.md
# can't use a glob for .md files, only for .html. .md files include READMEs
# for private subroles, and we don;t want to tag those as docs.
%doc %{ansible_collection_files}/%{collection_name}/README.html
%doc %{ansible_collection_files}/%{collection_name}/roles/*/README.html

%license %{_pkglicensedir}/*
%license %{installbase}/%{roleinstprefix}kdump/COPYING
%license %{installbase}/%{roleinstprefix}postfix/COPYING
%license %{installbase}/%{roleinstprefix}selinux/COPYING
%license %{installbase}/%{roleinstprefix}timesync/COPYING
%license %{installbase}/%{roleinstprefix}network/LICENSE
%license %{installbase}/%{roleinstprefix}storage/LICENSE
%license %{installbase}/%{roleinstprefix}metrics/LICENSE
%license %{installbase}/%{roleinstprefix}tlog/LICENSE
%license %{installbase}/%{roleinstprefix}kernel_settings/LICENSE
%license %{installbase}/%{roleinstprefix}kernel_settings/COPYING
%license %{installbase}/%{roleinstprefix}logging/LICENSE
%license %{installbase}/%{roleinstprefix}logging/COPYING
%license %{installbase}/%{roleinstprefix}nbde_server/LICENSE
%license %{installbase}/%{roleinstprefix}nbde_client/LICENSE
%license %{installbase}/%{roleinstprefix}certificate/LICENSE
%license %{installbase}/%{roleinstprefix}crypto_policies/LICENSE
%license %{installbase}/%{roleinstprefix}sshd/LICENSE
%license %{installbase}/%{roleinstprefix}ssh/LICENSE
%license %{installbase}/%{roleinstprefix}ha_cluster/LICENSE

%{ansible_collection_files}

%changelog
* Tue Apr  6 2021 Pavel Cahyna <pcahyna@redhat.com> - 1.0.1-1
- Sync with RHEL version 1.0.1-1.el8
  Fix description field in galaxy.yml
  Remove "Technology Preview" from Collection README
  Merging individual ignore file and add it to the package
  Add a note to each module Doc to indicate it is private
  Add patches for network and storage role ansible-test fixes
  Simplify doc tags in %%files, corrects a forgotten doc tag for ha_cluster
  Suppress one ansible-lint warning in ha_cluster
  Add patch for the inclusive language leftover on network-role README.md

* Mon Feb 22 2021 Pavel Cahyna <pcahyna@redhat.com> - 1.0.0-16
- Sync with RHEL version 1.0.0-31
  Rebase certificate role to pick up a test fix
  Rebase logging role to fix default private key path,
  upstream PR #218
  Update collection doc transformation to match a modified text
  and include the Tech Preview note again (for RHEL)

* Fri Feb 19 2021 Pavel Cahyna <pcahyna@redhat.com> - 1.0.0-15
- Sync with RHEL version 1.0.0-29
  Added roles: ssh, ha_cluster
  Updated roles: certificate, kernel_settings, nbde_client,
  logging, network
  Improvements to collection build and metadata
- Two further improvements from RHEL:
  Corrected merge botch in files list - make ssh README a docfile
  Dynamically update galaxy.yml with our metadata even on Fedora,
  we can't rely on correct version number in auto-maintenance

* Tue Feb  9 2021 Pavel Cahyna <pcahyna@redhat.com> - 1.0.0-14
- Synchronize with RHEL, new roles added:
  storage, metrics, tlog, kernel_settings, logging, nbde_server,
  nbde_client, certificate, crypto_policies, sshd, and the
  fedora.linux_system_roles collection.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Till Maas <opensource@till.name> - 1.0-8
- Install roles at /usr/share/linux-system-roles, use symlinks in
  /usr/share/ansible/roles/ to allow using alternatives

* Wed Nov 14 2018 Mike DePaulo <mikedep333@gmail.com> - 1.0-7
- spec file improvement: Remove unnecessary %%doc for files under _pkgdocdor
- Install license files under /usr/share/licenses instead of /usr/share/doc

* Tue Nov 06 2018 Mike DePaulo <mikedep333@gmail.com> - 1.0-7
- Fix rpm build for added example timesync example playbooks
- Misc spec file comments fixes
- Fix rpmlint error by escaping a previous changelog entry with a macro
- Comply with Fedora guidelines by always using "cp -p" in %%install
- Update %%description to be different for Fedora.

* Wed Oct 24 2018 Pavel Cahyna <pcahyna@redhat.com> - 1.0-7
- Update to latest versions of selinux, kdump and timesync.
- Update to the latest revision of postfix, fixes README markup
- Add Obsoletes for the -techpreview subpackage introduced mistakenly in 1.0-1
- spec file improvement: Unify the source macros with deftag() and defcommit()

* Tue Oct 23 2018 Till Maas <opensource@till.name> - 1.0-6
- Update Network system role to latest commit to include Fedora 29 fixes
- Update example timesync example playbooks
- Add comments about upstream status

* Tue Aug 14 2018 Pavel Cahyna <pcahyna@redhat.com> - 1.0-4
- Format the READMEs as html, by vdolezal, with changes to use highlight
  (source-highlight does not understand YAML)

* Thu Aug  9 2018 Pavel Cahyna <pcahyna@redhat.com> - 1.0-3
- Rebase the network role to the last revision (d866422).
  Many improvements to tests, introduces autodetection of the current provider
  and defaults to using profile name as interface name.
- Rebase the selinux, timesync and kdump roles to their 1.0rc1 versions.
  Many changes to the role interfaces to make them more consistent
  and conforming to Ansible best practices.
- Update the description.

* Fri May 11 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-4
- Fix complaints about /usr/bin/python during RPM build by making the affected scripts non-exec
- Fix merge botch

* Mon Mar 19 2018 Troy Dawson <tdawson@redhat.com> - 0.6-3.1
- Use -a (after cd) instead of -b (before cd) in %%setup

* Wed Mar 14 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-3
- Minor corrections of the previous change by Till Maas.

* Fri Mar  9 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-2
- Document network role options: static routes, ethernet, dns
  Upstream PR#36, bz1550128, documents bz1487747 and bz1478576

* Tue Jan 30 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-1
- Drop hard dependency on ansible (#1525655), patch from Yaakov Selkowitz
- Update the network role to version 0.4, solves bz#1487747, bz#1478576

* Tue Dec 19 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-3
- kdump: fix the wrong conditional for ssh checking and improve test (PR#10)

* Tue Nov 07 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-2
- kdump: add ssh support. upstream PR#9, rhbz1478707

* Tue Oct 03 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-1
- SELinux: fix policy reload when SELinux is disabled on CentOS/RHEL 6
  (bz#1493574)
- network: update to b856c7481bf5274d419f71fb62029ea0044b3ec1 :
  makes the network role idempotent (bz#1476053) and fixes manual
  network provider selection (bz#1485074).

* Mon Aug 28 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.4-1
- network: update to b9b6f0a7969e400d8d6ba0ac97f69593aa1e8fa5:
  ensure that state:absent followed by state:up works (bz#1478910), and change
  the example IP adresses to the IANA-assigned ones.
- SELinux: fix the case when SELinux is disabled (bz#1479546).

* Tue Aug 8 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.3-2
- We can't change directories to symlinks (rpm bug #447156) so keep the old
  names and create the new names as symlinks.

* Tue Aug 8 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.3-1
- Change the prefix to linux-system-roles., keeping compatibility
  symlinks.
- Update the network role to dace7654feb7b5629ded0734c598e087c2713265:
  adds InfiniBand support and other fixes.
- Drop a patch included upstream.

* Mon Jun 26 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.2-2
- Leave a copy of README and COPYING in every role's directory, as suggested by T. Bowling.
- Move the network example inventory to the documentation directory together.
  with the example playbooks and delete the now empty "examples" directory.
- Use proper reserved (by RFC 7042) MAC addresses in the network examples.

* Tue Jun 6 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.2-1
- Update the networking role to version 0.2 (#1459203)
- Version every role and the package separately. They live in separate repos
  and upstream release tags are not coordinated.

* Mon May 22 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.1-2
- Prefix the roles in examples and documentation with rhel-system-roles.

* Thu May 18 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.1-1
- Update to 0.1 (first upstream release).
- Remove the tuned role, it is not ready yet.
- Move the example playbooks to /usr/share/doc/rhel-system-roles/$SUBSYSTEM
  directly to get rid of an extra directory.
- Depend on ansible.

* Thu May 4 2017  Pavel Cahyna <pcahyna@redhat.com> - 0-0.1.20170504
- Initial release.
- kdump r. fe8bb81966b60fa8979f3816a12b0c7120d71140
- postfix r. 43eec5668425d295dce3801216c19b1916df1f9b
- selinux r. 1e4a21f929455e5e76dda0b12867abaa63795ae7
- timesync r. 33a1a8c349de10d6281ed83d4c791e9177d7a141
- tuned r. 2e8bb068b9815bc84287e9b6dc6177295ffdf38b
- network r. 03ff040df78a14409a0d89eba1235b8f3e50a750


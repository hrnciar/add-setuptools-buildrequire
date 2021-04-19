Name:           gnatcoll-db
Epoch:          2
Version:        21.0.0
Release:        2%{?dist}
Summary:        The GNAT Components Collection – database packages
Summary(sv):    GNAT Components Collection – databaspaket

License:        GPLv3+ with exceptions and GPLv3+
# The subpackages have different licenses. This is the aggregation of those.

URL:            https://github.com/AdaCore/gnatcoll-db
Source:         https://github.com/AdaCore/gnatcoll-db/archive/v%{version}/%{name}-%{version}.tar.gz

# This patch makes gnatcoll_db2ada run dborm.py in python3, and also corrects
# the location of dborm.py:
Patch:          gnatcoll-db-2018-dborm_python3.patch

BuildRequires:  gcc-gnat gprbuild fedora-gnat-project-common sed
BuildRequires:  gnatcoll-core-devel = %{epoch}:%{version}
BuildRequires:  gnatcoll-bindings-devel = %{epoch}:%{version}
# Although upstream doesn't explicitly say so, I guess it's best to keep all
# the parts of Gnatcoll on the same version number.
BuildRequires:  sqlite-devel libpq-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}
# GPRinstall fails on s390x and gnatcoll-db can't wait for that bug to be fixed.
# probably https://bugzilla.redhat.com/show_bug.cgi?id=1905708
ExcludeArch:    s390x

%global common_description_en \
This is the database module of the GNAT Components Collection.

%global common_description_sv \
Detta är databasmodulen i GNAT Components Collection.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package -n gnatcoll-sql
Summary:        The GNAT Components Collection – SQL component
Summary(sv):    GNAT Components Collection – SQL-komponenten
License:        GPLv3+ with exceptions

%description -n gnatcoll-sql
This is the SQL component of the GNAT Components Collection. It provides an
object-oriented, high-level interface to SQL queries.

%description -n gnatcoll-sql -l sv
Detta är SQL-komponenten i GNAT Components Collection. Den tillhandahåller ett
objektorienterat högnivågränssnitt mot SQL-frågor.


%package -n gnatcoll-sqlite
Summary:        The GNAT Components Collection – SQLite support
Summary(sv):    GNAT Components Collection – stöd för SQLite
License:        GPLv3+ with exceptions

%description -n gnatcoll-sqlite
This component provides support for SQLite to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-sqlite -l sv
Den här komponenten tillhandahåller stöd för SQLite till SQL-komponenten i
GNAT Components Collection.


%package -n gnatcoll-postgres
Summary:        The GNAT Components Collection – PostgreSQL support
Summary(sv):    GNAT Components Collection – stöd för PostgreSQL
License:        GPLv3+ with exceptions
# Gnatcoll.SQL.Postgres.Gnade is GPLv2+ with exceptions. The other source files
# are GPLv3+ with exceptions. These combine into GPLv3+ with exceptions on the
# binary code.

%description -n gnatcoll-postgres
This component provides support for PostgreSQL to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-postgres -l sv
Den här komponenten tillhandahåller stöd för PostgreSQL till SQL-komponenten i
GNAT Components Collection.


%package -n gnatcoll-xref
Summary:        The GNAT Components Collection – cross-referencing
Summary(sv):    GNAT Components Collection – korshänvisning
License:        GPLv3+
# gnatcoll-xref.ads, gnatcoll-xref.adb and gnatinspect.adb do not grant the
# GCC Runtime Library Exception.
Provides:       gnatinspect = %{epoch}:%{version}-%{release}

%description -n gnatcoll-xref
This is the Xref component of the GNAT Components Collection. It provides
support for parsing the .ali and .gli files that are generated by GNAT and GCC.
In particular, those files contain information that can be used to do cross-
references for entities (going from references to their declaration for
instance).

This package also contains Gnatinspect, a command-line tool for building and
querying a database of cross-reference information.

%description -n gnatcoll-xref -l sv
Detta är komponenten Xref i GNAT Components Collection. Den analyserar .ali-
och .gli-filerna som GNAT och GCC producerar. I de filerna finns uppgifter som
kan användas till korshänvisning (till exempel att hitta en deklaration utifrån
en referens).

Det här paketet innehåller också Gnatinspect, ett kommandoradsverktyg för att
bygga och söka i en databas över korshänvisningar.


%package devel
Summary:        Development files for the GNAT Components Collection – database packages
Summary(sv):    Filer för programmering med GNAT Components Collection – databaspaket
Provides:       gnatcoll_db2ada = %{epoch}:%{version}-%{release}
Provides:       gnatcoll_all2ada = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-postgres%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-xref%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel

%description devel %{common_description_en}

The gnatcoll-db-devel package contains source code and linking information for
developing applications that use the GNAT Components Collection database
packages.

This package also contains the tool gnatcoll_db2ada, which generates an Ada
package from a description of a database schema.

%description devel -l sv %{common_description_sv}

Paketet gnatcoll-db-devel innehåller källkod och länkningsinformation som
behövs för att utveckla program som använder GNAT Components Collections
databaspaket.

Det här paketet innehåller också verktyget gnatcoll_db2ada som genererar ett
adapaket från en beskrivning av en databasstruktur.


%prep
%autosetup -p0


%build
export GNATCOLL_VERSION=%{version}
export BUILD=PROD
export LIBRARY_TYPE=relocatable
export GNATCOLL_SQLITE=external

# Most of these components depend on each other and need to be built in
# dependency order. Install the built libraries to a staging directory where
# the later build jobs can find them.
mkdir stage  # without --parents to avoid clobbering any existing directory
%global GPRbuild_args %{GPRbuild_optflags} -aP stage%{_GNAT_project_dir}
for subdir in sql sqlite postgres xref ; do
    component=gnatcoll_${subdir}
    gprbuild -P ${subdir}/${component}.gpr %{GPRbuild_args}
    gprinstall -P ${subdir}/${component}.gpr \
               -aP stage%{_GNAT_project_dir} \
               --prefix=${PWD}/stage%{_prefix} \
               --lib-subdir=${PWD}/stage%{_libdir} \
               --ali-subdir=${PWD}/stage%{_libdir}/${component} \
               --no-lib-link -m --create-missing-dirs
    ln --symbolic --force lib${component}.so.%{version} \
       stage%{_libdir}/lib${component}.so
done
# There are four variants of gnatcoll_db2ada that differ in their database
# support. Build the one that supports the most databases.
for GPR in gnatinspect/gnatinspect.gpr gnatcoll_db2ada/gnatcoll_all2ada.gpr ; do
    gprbuild -P ${GPR} %{GPRbuild_args} -cargs -fPIE
    # -fPIE is added for the hardening.
done


%install
# The libraries have already been staged, so just move them to the "buildroot"
# staging directory.
mv stage/* --target-directory=%{buildroot}

# Stage the executable files.
mkdir --parents %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/gnatcoll
cp gnatinspect/obj/gnatinspect gnatcoll_db2ada/obj/gnatcoll_all2ada \
   --target-directory=%{buildroot}%{_bindir}
cp --preserve=timestamps gnatcoll_db2ada/dborm.py \
   --target-directory=%{buildroot}%{_libexecdir}/gnatcoll

# Preserving the command name "gnatcoll_db2ada" seems like a good idea.
ln --symbolic gnatcoll_all2ada %{buildroot}%{_bindir}/gnatcoll_db2ada

# Make the generated usage project files architecture-independent.
for GPR in %{buildroot}%{_GNAT_project_dir}/*.gpr ; do
    component=`basename --suffix=.gpr ${GPR}`
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'${component}'";|i' \
        ${GPR}
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Delete the package Linker, which contains linker parameters that a
    #    shared library normally doesn't need, and can contain architecture-
    #    specific pathnames.
    # 4: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 5: Replace the value of Library_Dir with Directories.Libdir.
    # 6: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

# GPRinstall's manifest files are architecture-specific because they contain
# what seems to be checksums of architecture-specific files, so they must not
# be under _datadir. Their function is poorly documented, but they seem to be
# used when GPRinstall uninstalls packages. The manifest files are therefore
# irrelevant in this RPM package, so delete them.
rm --recursive --force %{buildroot}%{_GNAT_project_dir}/manifests

# This readme file may be of some value to developers:
mkdir --parents %{buildroot}%{_docdir}/gnatcoll/xref
cp --preserve=timestamps xref/README.md \
   --target-directory=%{buildroot}%{_docdir}/gnatcoll/xref

# Install the license in a directory named after the source package.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 COPYING.RUNTIME \
   --target-directory=%{buildroot}%{_licensedir}/%{name}


%check
%{_rpmconfigdir}/check-rpaths


%files -n gnatcoll-sql
%{_libdir}/libgnatcoll_sql.so.*
%license %{_licensedir}/%{name}
# All the other subpackages depend on gnatcoll-sql, so only this one needs to
# contain the license files.

%files -n gnatcoll-sqlite
%{_libdir}/libgnatcoll_sqlite.so.*

%files -n gnatcoll-postgres
%{_libdir}/libgnatcoll_postgres.so.*

%files -n gnatcoll-xref
%{_libdir}/libgnatcoll_xref.so.*
%{_bindir}/gnatinspect

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gnatcoll*
%{_GNAT_project_dir}/*
%{_bindir}/gnatcoll_*2ada
%{_libexecdir}/gnatcoll
%{_docdir}/gnatcoll


%changelog
* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-2
- Corrected the license of gnatcoll-xref.

* Mon Feb 08 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-1
- Upgraded to version 21.0.0.
- s390x is excluded until GPRinstall can be fixed.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-3
- Added versions to Provides tags.
- Tagged the license file as such.

* Wed Apr 03 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-2
- Added more macro usage and more comments.
- Removed unnecessary duplicates of the license file.

* Sun Mar 24 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-1
- new package

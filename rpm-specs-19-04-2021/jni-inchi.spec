%global debver 1

Name:           jni-inchi
Version:        0.8
Release:        1%{?dist}
Summary:        International Chemical Identifiers for Java

License:        LGPLv3+
URL:            http://jni-inchi.sourceforge.net/
Source0:        https://github.com/SureChEMBL/jni-inchi/archive/v%{version}-%{debver}-deb/%{name}-%{version}.tar.gz
# Generate JNI headers with "javac -h" instead of javah.  Do not use jnati,
# which we do not have in Fedora, to load the native library.
Patch0:         %{name}-native.patch
# Fix warnings about unsafe or unchecked operations
Patch1:         %{name}-unsafe.patch
# Adapt to changes in inchi 1.06
Patch2:         %{name}-inchi106.patch
# Fix javadoc problems
Patch3:         %{name}-javadoc.patch

BuildRequires:  gcc
BuildRequires:  inchi-devel
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)

%description
JNI-InChI enables Java software to generate IUPAC's International
Chemical Identifiers (InChIs) by making Java Native Interface (JNI) calls
to the InChI C library developed by IUPAC.  All of the features from the
InChI library are supported:

- Standard and Non-Standard InChI generation from structures with 3D, 2D,
  or no coordinates
- Structure generation (without coordinates) from InChI
- InChIKey generation
- Check InChI / InChIKey
- InChI-to-InChI conversion
- AuxInfo to InChI input
- Access to the full range of options supported by InChI
- Full support for InChI's handling of stereochemistry

JNI-InChI is a library intended for use by developers of other projects.
It does not enable users to generate InChIs from molecule file formats
such as .mol, .cml, .mol2, or SMILES strings.  If you want to do any of
these, you should take a look at the Chemistry Development Kit (CDK) or
JUMBO, both of which include InChI generation powered by JNI-InChI.  If,
however, you are a software developer and you want want to generate the
InChI for a molecule that you already hold in memory, JNI-InChI is what
you need.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{version}-%{debver}-deb -p1

# Remove prebuilt artifacts
rm -fr src/main/resources

# Remove bundled inchi library
rm -fr src/main/native/inchi-1.03

# Remove a test class that uses a very old log4j interface
rm src/main/java/net/sf/jniinchi/Main.java

# Set the library path
sed -i 's,@LIBDIR@,%{_libdir},' \
    src/main/java/net/sf/jniinchi/JniInchiWrapper.java

# Set the build flags
sed -e 's|@CFLAGS@|%{build_cflags}|' \
    -e 's|@LDFLAGS@|%{build_ldflags}|' \
    -i src/main/native/Makefile

# Fix end of line encoding
sed -i.orig 's/\r//' README
touch -r README.orig README
rm README.orig

# Not needed for an RPM build
%pom_remove_plugin :maven-javadoc-plugin

%build
mkdir -p target/native
export LD_LIBRARY_PATH=$PWD/target/native
%mvn_build

%install
%mvn_install

# Install the shared object
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -p target/native/*.so %{buildroot}%{_libdir}/%{name}

%files -f .mfiles
%doc README README.surechembl.txt
%license LICENSE-GPL.txt LICENSE-LGPL.txt NOTICE.txt
%{_libdir}/%{name}/

%changelog
* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 0.8-1
- Initial RPM

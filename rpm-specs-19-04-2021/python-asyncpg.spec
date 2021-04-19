%global srcname asyncpg

Name:           python-%{srcname}
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.22.0
Release:        4%{?dist}

License:        ASL 2.0
URL:            https://github.com/MagicStack/%{srcname}
Source0:        %{pypi_source}
# Temporary workaround; see https://github.com/MagicStack/asyncpg/pull/708.
Source1:        https://raw.githubusercontent.com/MagicStack/%{srcname}/v%{version}/docs/Makefile
Source2:        https://raw.githubusercontent.com/MagicStack/%{srcname}/v%{version}/docs/_static/theme_overrides.css

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python3-docs

BuildRequires:  make

# For tests:
#
# For pg_config binary
BuildRequires:  libpq-devel
# For pg_ctl binary
BuildRequires:  postgresql-server
# For citext extension
BuildRequires:  postgresql-contrib
# Replace python3dist(sphinxcontrib-asyncio), which is not working properly
# (Error in "py:comethod directive: unknown option: "async".):
BuildRequires:  python3dist(sphinxcontrib-trio)

# Note that asyncpg/pgproto comes from a git submodule referencing a separate
# project, https://github.com/MagicStack/py-pgproto. However, we do not treat
# it as a bundled dependency because it contains only sources; it has no build
# system and is not designed for separate installation; and it is managed as a
# part of the asyncpg package, as evidenced by the comment “This module is part
# of asyncpg” in the file headers.

%global common_description %{expand:
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL
server binary protocol for use with Python’s asyncio framework. You can read
more about asyncpg in an introductory blog post
http://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/.}

%description %{common_description}


%generate_buildrequires
# Note dev extra includes doc and test extras
%pyproject_buildrequires -x dev


%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       python3-docs


%description -n python3-%{srcname} %{common_description}


%package doc
Summary:        Documentation for %{name}

BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rvf %{srcname}.egg-info

# Remove pre-generated C sources from Cython to ensure they are re-generated
# and not used in the build. Note that recordobj.c is not a generated source,
# and must not be removed!
find %{srcname} -type f -name '*.c' ! -name 'recordobj.c' -print -delete

# Loosen pinned versions in setup.py
sed -r -i 's/~=/>=/g' setup.py

cp -p '%{SOURCE1}' docs/
mkdir -p docs/_static
cp -p '%{SOURCE2}' docs/_static/

# Use local inventory in intersphinx mapping.
#
# Do not put the source directory at the front of the path, as this keeps us
# from using our own PYTHONPATH setting to allow importing the compiled
# extension modules.
#
# Replace python3dist(sphinxcontrib-asyncio), which is not working properly:
# (Error in "py:comethod directive: unknown option: "async".):
sed -r -i \
    -e 's|https://docs.python.org/3|/%{_docdir}/python3-docs/html|' \
    -e 's|(sys\.path\.)insert\(0,[[:blank:]]*|\1append\(|' \
    -e 's|(sphinxcontrib)\.asyncio|\1_trio|' \
    docs/conf.py


%build
%set_build_flags
%pyproject_wheel

(
  # Temporary local installation so we can import the Cython extension module
  # to build documentation:
  PYTEMP="${PWD}/%{_vpath_builddir}/pytemp"
  export PYTHONPATH="${PYTEMP}"

  %{__python3} -m pip install --target="${PYTEMP}" \
      --no-deps --use-pep517 --no-build-isolation \
      --disable-pip-version-check --no-clean --progress-bar off --verbose \
      %{_pyproject_wheeldir}/*.whl

  %make_build -C docs html SPHINXBUILD='sphinx-build' SPHINXOPTS='%{?_smp_mflags}'
  rm -vf docs/_build/html/.buildinfo docs/_build/html/.nojekyll

  rm -rf "${PYTEMP}"
)


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# It is not clear why the tests always import asyncpg as ../asyncpg/__init__.py
# even if we set PYTHONPATH to the installed sitearch directory. This
# workaround is ugly, but there is nothing actually wrong with it, as the
# install is already done by the time the check section runs:
rm -rf %{srcname}
ln -s %{buildroot}%{python3_sitearch}/%{srcname}/

# Do not run flake8 code style tests (which may fail)
k='not TestFlake8'

%pytest -k "${k}"


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

# The Cython implementation files (.pyx) and Cython-generated C sources (.c)
# are included in the installed package. These are definitely not needed.

%exclude %{python3_sitearch}/%{srcname}/*/*.pyx
%exclude %{python3_sitearch}/%{srcname}/*/*/*.pyx
%exclude %{python3_sitearch}/%{srcname}/*/*.c
%exclude %{python3_sitearch}/%{srcname}/*/*/*.c

# The C header files (.h) and Cython definition and include files (.pxd and
# .pxi) would be needed to compile Cython extension code using the internal
# APIs of the package. The upstream documentation does not indicate that this
# is an intended use, so we do not ship them. If we did, we would need to put
# them in a new subpackage called python3-%%{srcname}-devel.
%exclude %{python3_sitearch}/%{srcname}/*/*.pxd
%exclude %{python3_sitearch}/%{srcname}/*/*/*.pxd
%exclude %{python3_sitearch}/%{srcname}/*/*.pxi
%exclude %{python3_sitearch}/%{srcname}/*/*.h
%exclude %{python3_sitearch}/%{srcname}/*/*/*.h


%files doc
%license LICENSE
%doc README.rst
%doc docs/_build/html


%changelog
* Tue Mar 30 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.0-4
- Use pyproject-rpm-macros for build and install, too
- More complete documentation build

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.0-3
- Remove setuptools BR, redundant with %%pyproject_buildrequires

* Wed Mar 03 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.0-2
- Fix intersphinx inventory path

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.0-1
- Initial package

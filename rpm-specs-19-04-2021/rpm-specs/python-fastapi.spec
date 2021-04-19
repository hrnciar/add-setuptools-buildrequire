%global srcname fastapi

# The following dependencies must be packaged to build the HTML documentation:
#   - python3dist(markdown-include)
#   - python3dist(mkdocs-markdown-extradata-plugin)
%bcond_with html_docs

%global sum_en  FastAPI framework
%global sum_es  FastAPI framework
# Missing translation (localized docs present, but untranslated)
# Summary(fr):    FastAPI framework
# Missing translation (localized docs present, but untranslated)
# Summary(it):    FastAPI framework
# Translation present, but the title was not translated
%global sum_ja  FastAPI framework
%global sum_ka  FastAPI 프레임워크
%global sum_pt  Framework FastAPI
# Missing translation (localized docs present, but untranslated)
# %%global sum_ru  FastAPI framework
# Missing translation (localized docs present, but untranslated)
# %%global sum_sq  FastAPI framework
# Missing translation (localized docs present, but untranslated)
# %%global sum_tr  FastAPI framework
# Missing translation (localized docs present, but untranslated)
# %%global sum_uk  FastAPI framework
%global sum_zh  FastAPI 框架

Name:           python-%{srcname}
Version:        0.63.0
Release:        7%{?dist}
Summary:        %{sum_en}

License:        MIT
URL:            https://github.com/tiangolo/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

# Fix compatibility with starlette 0.14.x
# (https://github.com/tiangolo/fastapi/issues/2342,
# https://github.com/tiangolo/fastapi/issues/2493):
#
# https://github.com/tiangolo/fastapi/pull/2335/
Patch0:         %{srcname}-0.63.0-pr-2335.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Documentation
BuildRequires:  js-termynal
BuildRequires:  web-assets-devel
# For converting absolute symlinks in the buildroot to relative ones
BuildRequires:  symlinks

Summary(en):    %{sum_en}
Summary(es):    %{sum_es}
# Summary(fr):    %%{sum_fr}
# Summary(it):    %%{sum_it}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pt):    %{sum_pt}
# Summary(ru):    %%{sum_ru}
# Summary(sq):    %%{sum_sq}
# Summary(tr):    %%{sum_tr}
# Summary(uk):    %%{sum_uk}
Summary(zh):    %{sum_zh}

%global common_description_en %{expand:
FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python 3.6+ based on standard Python type hints.

The key features are:

  • Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette
    and Pydantic). One of the fastest Python frameworks available.

  • Fast to code: Increase the speed to develop features by about 200% to 300%.*
  • Fewer bugs: Reduce about 40% of human (developer) induced errors.*
  • Intuitive: Great editor support. Completion everywhere. Less time
    debugging.
  • Easy: Designed to be easy to use and learn. Less time reading docs.
  • Short: Minimize code duplication. Multiple features from each parameter
    declaration. Fewer bugs.
  • Robust: Get production-ready code. With automatic interactive
    documentation.
  • Standards-based: Based on (and fully compatible with) the open standards
    for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

* estimation based on tests on an internal development team, building production
  applications.}
%global common_description_es %{expand:
FastAPI es un web framework moderno y rápido (de alto rendimiento) para
construir APIs con Python 3.6+ basado en las anotaciones de tipos estándar de
Python.

Sus características principales son:

  • Rapidez: Alto rendimiento, a la par con NodeJS y Go (gracias a
    Starlette y Pydantic). Uno de los frameworks de Python más rápidos.

  • Rápido de programar: Incrementa la velocidad de desarrollo entre 200% y
    300%.*
  • Menos errores: Reduce los errores humanos (de programador) aproximadamente
    un 40%.*
  • Intuitivo: Gran soporte en los editores con auto completado en todas
    partes. Gasta menos tiempo debugging.
  • Fácil: Está diseñado para ser fácil de usar y aprender. Gastando menos
    tiempo leyendo documentación.
  • Corto: Minimiza la duplicación de código. Múltiples funcionalidades con
    cada declaración de parámetros. Menos errores.
  • Robusto: Crea código listo para producción con documentación automática
    interactiva.
  • Basado en estándares: Basado y totalmente compatible con los estándares
    abiertos para APIs: OpenAPI (conocido previamente como Swagger) y JSON
    Schema.

* Esta estimación está basada en pruebas con un equipo de desarrollo interno
  contruyendo aplicaciones listas para producción.}
#%%global common_description_fr %%{expand:…}
#%%global common_description_it %%{expand:…}
%global common_description_ja %{expand:
FastAPI は、Pythonの標準である型ヒントに基づいてPython 3.6 以降でAPI
を構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワークです。

主な特徴:

  - 高速: NodeJS や Go 並みのとても高いパフォーマンス (Starlette と Pydantic
    のおかげです)。最も高速な Python フレームワークの一つです。

  - 高速なコーディング: 開発速度を約 200%~300%向上させます。 *
  - 少ないバグ: 開発者起因のヒューマンエラーを約 40％削減します。 *
  - 直感的: 素晴らしいエディタのサポートや オートコンプリート。
    デバッグ時間を削減します。
  - 簡単: 簡単に利用、習得できるようにデザインされています。
    ドキュメントを読む時間を削減します。
  - 短い: コードの重複を最小限にしています。
    各パラメータからの複数の機能。少ないバグ。
  - 堅牢性:
    自動対話ドキュメントを使用して、本番環境で使用できるコードを取得します。
  - Standards-based: API
    のオープンスタンダードに基づいており、完全に互換性があります: OpenAPI
    (以前は Swagger として知られていました) や JSON スキーマ.

* 本番アプリケーションを構築している開発チームのテストによる見積もり。}
%global common_description_ko %{expand:
FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한
Python3.6+의 API를 빌드하기 위한 웹 프레임워크입니다.

주요 특징으로:

  • 빠름: (Starlette과 Pydantic 덕분에) NodeJS 및 Go와 대등할 정도로 매우 높은
    성능. 사용 가능한 가장 빠른 파이썬 프레임워크 중 하나.

  • 빠른 코드 작성: 약 200%에서 300%까지 기능 개발 속도 증가.*
  • 적은 버그: 사람(개발자)에 의한 에러 약 40% 감소.*
  • 직관적: 훌륭한 편집기 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.
  • 쉬움: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
  • 짧음: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
  • 견고함: 준비된 프로덕션 용 코드를 얻으세요. 자동 대화형 문서와 함께.
  • 표준 기반: API에 대한 (완전히 호환되는) 개방형 표준 기반: OpenAPI (이전에
    Swagger로 알려졌던) 및 JSON 스키마.

* 내부 개발팀의 프로덕션 애플리케이션을 빌드한 테스트에 근거한 측정}
%global common_description_pt %{expand:
FastAPI é um moderno e rápido (alta performance) framework web para construção
de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

Os recursos chave são:

  • Rápido: alta performance, equivalente a NodeJS e Go (graças ao Starlette e
    Pydantic). Um dos frameworks mais rápidos disponíveis.
  • Rápido para codar: Aumenta a velocidade para desenvolver recursos entre
    200% a 300%.*
  • Poucos bugs: Reduz cerca de 40% de erros induzidos por humanos
    (desenvolvedores).*
  • Intuitivo: Grande suporte a IDEs. Auto-Complete em todos os lugares. Menos
    tempo debugando.
  • Fácil: Projetado para ser fácil de aprender e usar. Menos tempo lendo
    documentação.
  • Enxuto: Minimize duplicação de código. Múltiplos recursos para cada
    declaração de parâmetro. Menos bugs.
  • Robusto: Tenha código pronto para produção. E com documentação interativa
    automática.
  • Baseado em padrões: Baseado em (e totalmente compatível com) os padrões
    abertos para APIs: OpenAPI (anteriormente conhecido como Swagger) e JSON
    Schema.

* estimativas baseadas em testes realizados com equipe interna de
  desenvolvimento, construindo aplicações em produção.}
#%%global common_description_ru %%{expand:…}
#%%global common_description_sq %%{expand:…}
#%%global common_description_tr %%{expand:…}
#%%global common_description_uk %%{expand:…}
%global common_description_zh %{expand:
FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+
并基于标准的 Python 类型提示。

关键特性:

  • 快速：可与 NodeJS 和 Go 比肩的极高性能（归功于 Starlette 和 Pydantic）。
    最快的 Python web 框架之一。
  • 高效编码：提高功能开发速度约 200％ 至 300％。*
  • 更少 bug：减少约 40％ 的人为（开发者）导致错误。*
  • 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
  • 简单：设计的易于使用和学习，阅读文档的时间更短。
  • 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
  • 健壮：生产可用级别的代码。还有自动生成的交互式文档。
  • 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger)
    和 JSON Schema。

* 根据对某个构建线上应用的内部开发团队所进行的测试估算得出。}

%description %{common_description_en}

%description -l en %{common_description_en}
%description -l es %{common_description_es}
#%%description -l fr %%{common_description_fr}
#%%description -l it %%{common_description_it}
%description -l ja %{common_description_ja}
%description -l ko %{common_description_ko}
%description -l pt %{common_description_pt}
#%%description -l ru %%{common_description_ru}
#%%description -l sq %%{common_description_sq}
#%%description -l tr %%{common_description_tr}
#%%description -l uk %%{common_description_uk}
%description -l zh %{common_description_zh}


%generate_buildrequires
# Tests under tests/test_tutorial may require dependencies that are only in the
# dev extra.
%pyproject_buildrequires -x all,test,dev%{?with_html_docs:,doc}


%pyproject_extras_subpkg -n python3-%{srcname} all


%package -n     python3-%{srcname}
Summary:        %{sum_en}

Summary(en):    %{sum_en}
Summary(es):    %%{sum_es}
# Summary(fr):    %%{sum_fr}
# Summary(it):    %%{sum_it}
Summary(ja):    %{sum_ja}
Summary(ko):    %{sum_ko}
Summary(pt):    %{sum_pt}
# Summary(ru):    %%{sum_ru}
# Summary(sq):    %%{sum_sq}
# Summary(tr):    %%{sum_tr}
# Summary(uk):    %%{sum_uk}
Summary(zh):    %{sum_zh}

%description -n python3-%{srcname} %{common_description_en}

%description -n python3-%{srcname} -l en %{common_description_en}
%description -n python3-%{srcname} -l es %{common_description_es}
#%%description -n python3-%%{srcname} -l fr %%{common_description_fr}
#%%description -n python3-%%{srcname} -l it %%{common_description_it}
%description -n python3-%{srcname} -l ja %{common_description_ja}
%description -n python3-%{srcname} -l ko %{common_description_ko}
%description -n python3-%{srcname} -l pt %{common_description_pt}
#%%description -n python3-%%{srcname} -l ru %%{common_description_ru}
#%%description -n python3-%%{srcname} -l sq %%{common_description_sq}
#%%description -n python3-%%{srcname} -l tr %%{common_description_tr}
#%%description -n python3-%%{srcname} -l uk %%{common_description_uk}
%description -n python3-%{srcname} -l zh %{common_description_zh}


%package doc
Summary:        Documentation for %{name}

Requires:       js-termynal

%description doc %{common_description_en}

%description doc -l en %{common_description_en}
%description doc -l es %{common_description_es}
#%%description doc -l fr %%{common_description_fr}
#%%description doc -l it %%{common_description_it}
%description doc -l ja %{common_description_ja}
%description doc -l ko %{common_description_ko}
%description doc -l pt %{common_description_pt}
#%%description doc -l ru %%{common_description_ru}
#%%description doc -l sq %%{common_description_sq}
#%%description doc -l tr %%{common_description_tr}
#%%description doc -l uk %%{common_description_uk}
%description doc -l zh %{common_description_zh}


%prep
%autosetup -n %{srcname}-%{version} -p1

# Comment out all dependencies on orjson (for ORJSONResponse); it cannot be
# packaged in Fedora until it builds with the stable Rust toolchain instead of
# the nightly one. Note that this removes it from the “all” extra metapackage.
#
# Loosen all dependencies that are pinned to exact versions. We have to try to
# work with what is packaged.
#
# Comment out test dependencies that are only for linting/formatting/analysis,
# and will not be used.
#
# Comment out the databases[sqlite] test dependency because it is not yet
# packaged for Fedora.
#
# Do not require async backport libraries where they are not needed
# (https://github.com/tiangolo/fastapi/pull/2902).
#
# Selectively loosen dependencies that are perhaps arbitrarily pinned to
# certain version ranges: first, those for which we choose to allow newer
# versions, and second, those for which we choose to allow older and newer
# versions. This could have unwanted consequences, but such is the nature of
# packaging.
#
# Allow aiofiles 0.6.x: https://github.com/tiangolo/fastapi/pull/3075
#
# Replace passlib[bcrypt] with passlib and bcrypt separately, until
# https://bugzilla.redhat.com/show_bug.cgi?id=1936021 is fixed (F35 and later).
sed -r -i \
    -e 's/("orjson\b.*",)/# \1/' \
    -e 's/==/>=/g' \
    -e 's/("(mypy|black|flake8|isort|autoflake)\b.*",)/# \1/' \
    -e 's/("(databases\[sqlite\]).*",)/# \1/' \
    -e 's/("async_(exit_stack|generator)[^"]*)/\1; '"python_version < '3.7'/" \
    -e 's/("(httpx)\b[^<"]*),[[:blank:]]*<[^"]*/\1/' \
    -e 's/("(mkdocs-material|ujson))\b[^"]*/\1/' \
    -e 's/("(aiofiles|)\b[^<"]*,[[:blank:]]*<0\.)6\.0/\17.0/' \
%if 0%{?fedora} && 0%{?fedora} < 35
    -e 's/([[:blank:]]*)("passlib)\[bcrypt\](.*)/\1"bcrypt",\n\1\2\3/' \
%endif
    pyproject.toml

# Remove bundled js-termynal 0.0.1:
find docs -type f -name 'termynal.*' |
  while read -r fn
  do
    echo '' > "${fn}"  # make it an empty file
  done
# In %%install, we will restore this functionality by symlinking the system
# copy.


%build
%pyproject_wheel
%if %{with html_docs}
mkdocs build
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}

install -t '%{buildroot}%{_pkgdocdir}' -D -m 0644 -p \
    CONTRIBUTING.md README.md
%if %{with html_docs}
cp -rp site '%{buildroot}%{_pkgdocdir}/'
%else
cp -rp docs '%{buildroot}%{_pkgdocdir}/markdown'
%endif

# We do not own these files; we temporarily install them in the buildroot so we
# do not have dangling symlinks.
install -d "$(dirname '%{buildroot}%{_jsdir}')"
cp -rp %{_jsdir} %{buildroot}%{_jsdir}

# Replace truncated js-termynal files with relative symbolic links
find docs -type f -name 'termynal.*' |
  while read -r fn
  do
    ln -s -f "%{buildroot}%{_jsdir}/$(basename "${fn}")" "${fn}"
    symlinks -c -o "${fn}"
  done

rm -rf '%{buildroot}%{_jsdir}'


%check
# Requires databases[sqlite]:
#   tests/test_tutorial/test_async_sql_databases/test_tutorial001.py
#   tests/test_tutorial/test_custom_response/test_tutorial001b.py
# Requires orjson:
#   tests/test_default_response_class.py
%pytest \
    --ignore=tests/test_tutorial/test_async_sql_databases/test_tutorial001.py \
    --ignore=tests/test_tutorial/test_custom_response/test_tutorial001b.py \
    --ignore=tests/test_default_response_class.py


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%files doc
%license LICENSE
%{_pkgdocdir}


%changelog
* Mon Apr 12 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-7
- Allow aiofiles 0.6.x: https://github.com/tiangolo/fastapi/pull/3075

* Tue Apr 06 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-6
- Do not use %%exclude for unpackaged files (RPM 4.17 compatibility)

* Sat Mar 27 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-5
- Typo fix in js-termynal symbolic links

* Thu Mar 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-4
- Improved source URL (better tarball name)

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-3
- Use system js-termynal to replace the (removed) bundled copy
- No longer need to work around missing python3dist(passlib[bcrypt]) on F35
- Fix typo in Summary(es)

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-2
- Drop python3dist(setuptools) BR, redundant with %%pyproject_buildrequires

* Sat Mar 06 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.63.0-1
- New upstream version 0.63.0
- Whitespace changes
- Drop obsolete %%python_provide macro
- Comment out orjson dependencies in package metadata
- Remove explicit/manual dependencies. This drops the hard dependency on uvicorn.
- Use pyproject-rpm-macros for generated BR’s
- Loosen all pinned dependencies
- Fix starlette 0.14.x compatibility
- Switch from PyPI tarball to GitHub tarball
- Add a metapackage for the “all” extra (which is really all-but-orjson)
- Add a separate -doc package; for now, we cannot build the HTML documentation,
  so we install the Markdown sources instead
- Improved and localized summaries and descriptions from upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.61.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct  7 00:24:09 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.61.1-2
- add missing deps.

* Wed Sep 30 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.61.1-1
- Initial package.
- Fix license TAG.

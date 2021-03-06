%global grafanapcp_arches %{lua: go_arches = {}
  for arch in rpm.expand("%{go_arches}"):gmatch("%S+") do
    go_arches[arch] = 1
  end
  for arch in rpm.expand("%{nodejs_arches}"):gmatch("%S+") do
    if go_arches[arch] then
      print(arch .. " ")
  end
end}

# gobuild and gotest macros are defined in go-rpm-macros, which is not available on RHEL
# definitions lifted from Fedora 34 podman.spec
%if ! 0%{?gobuild:1}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif
%if ! 0%{?gotest:1}
%define gotest() GO111MODULE=off go test -buildmode pie -compiler gc -ldflags "${LDFLAGS:-} -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" %{?**};
%endif

# Specify if the frontend and dashboards will be compiled as part of the build or are attached
# as a webpack tarball (in case of an unsuitable nodejs or jsonnet version on the build system)
%define compile_frontend 0

Name:           grafana-pcp
Version:        3.0.2
Release:        2%{?dist}
Summary:        Performance Co-Pilot Grafana Plugin
License:        ASL 2.0
URL:            https://github.com/performancecopilot/grafana-pcp

Source0:        https://github.com/performancecopilot/grafana-pcp/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        grafana-pcp-vendor-%{version}.tar.xz
%if %{compile_frontend} == 0
# Source2 contains the precompiled frontend and dashboards
Source2:        grafana-pcp-webpack-%{version}.tar.gz
%endif
Source3:        Makefile
Source4:        list_bundled_nodejs_packages.py

# Intersection of go_arches and nodejs_arches
ExclusiveArch:  %{grafanapcp_arches}

BuildRequires:  systemd-rpm-macros, golang, go-srpm-macros
%if 0%{?fedora} >= 31
BuildRequires:  go-rpm-macros
%endif
%if %{compile_frontend}
BuildRequires:  make, nodejs >= 1:12, nodejs < 1:13, yarnpkg, golang-github-google-jsonnet
%endif

# omit golang debugsource, see BZ 995136 and related
%global         dwz_low_mem_die_limit 0
%global         _debugsource_template %{nil}

%global         install_dir %{_sharedstatedir}/grafana/plugins/performancecopilot-pcp-app

Requires:       grafana >= 7.3.6
Suggests:       pcp >= 5.2.2
Suggests:       redis >= 5.0.0
Suggests:       bpftrace >= 0.9.2

# Obsolete old webapps
Obsoletes: pcp-webjs <= 4.3.4
Obsoletes: pcp-webapp-blinkenlights <= 4.3.4
Obsoletes: pcp-webapp-grafana <= 4.3.4
Obsoletes: pcp-webapp-graphite <= 4.3.4
Obsoletes: pcp-webapp-vector <= 4.3.4

# vendored golang and node.js build dependencies
# this is for security purposes, if nodejs-foo ever needs an update,
# affected packages can be easily identified.
# Note: generated by the Makefile (see README.md)
Provides: bundled(golang(github.com/grafana/grafana-plugin-sdk-go)) = 0.79.0
Provides: bundled(golang(github.com/smartystreets/goconvey)) = 1.6.4
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.12.1
Provides: bundled(npm(@grafana/data)) = 7.3.6
Provides: bundled(npm(@grafana/runtime)) = 7.3.6
Provides: bundled(npm(@grafana/toolkit)) = 7.3.6
Provides: bundled(npm(@grafana/ui)) = 7.3.6
Provides: bundled(npm(@types/blueimp-md5)) = 2.7.0
Provides: bundled(npm(@types/d3-selection)) = 1.4.3
Provides: bundled(npm(@types/enzyme)) = 3.10.5
Provides: bundled(npm(@types/enzyme-adapter-react-16)) = 1.0.6
Provides: bundled(npm(@types/expect-puppeteer)) = 3.3.1
Provides: bundled(npm(@types/jest)) = 24.0.13
Provides: bundled(npm(@types/jest-environment-puppeteer)) = 4.4.1
Provides: bundled(npm(@types/lodash)) = 4.14.165
Provides: bundled(npm(@types/memoize-one)) = 5.1.2
Provides: bundled(npm(@types/react-autosuggest)) = 9.3.14
Provides: bundled(npm(@types/react-redux)) = 7.1.12
Provides: bundled(npm(@types/redux)) = 3.6.0
Provides: bundled(npm(@types/redux-persist)) = 4.3.1
Provides: bundled(npm(@types/redux-persist-transform-filter)) = 0.0.4
Provides: bundled(npm(babel-plugin-remove-object-properties)) = 1.0.2
Provides: bundled(npm(blueimp-md5)) = 2.18.0
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(d3-flame-graph)) = 3.1.1
Provides: bundled(npm(d3-selection)) = 1.4.1
Provides: bundled(npm(emotion)) = 10.0.27
Provides: bundled(npm(enzyme)) = 3.11.0
Provides: bundled(npm(enzyme-adapter-react-16)) = 1.15.5
Provides: bundled(npm(eslint-plugin-prettier)) = 3.1.4
Provides: bundled(npm(jest)) = 25.5.4
Provides: bundled(npm(jest-date-mock)) = 1.0.8
Provides: bundled(npm(jest-puppeteer)) = 4.4.0
Provides: bundled(npm(lodash)) = 4.17.19
Provides: bundled(npm(loglevel)) = 1.7.1
Provides: bundled(npm(loglevel-plugin-prefix)) = 0.8.4
Provides: bundled(npm(memoize-one)) = 4.1.0
Provides: bundled(npm(monaco-editor)) = 0.20.0
Provides: bundled(npm(monaco-editor-webpack-plugin)) = 1.9.0
Provides: bundled(npm(prettier)) = 1.19.1
Provides: bundled(npm(prettier-plugin-organize-imports)) = 1.1.1
Provides: bundled(npm(puppeteer)) = 5.5.0
Provides: bundled(npm(react-autosuggest)) = 10.0.4
Provides: bundled(npm(react-monaco-editor)) = 0.36.0
Provides: bundled(npm(react-redux)) = 7.2.2
Provides: bundled(npm(react-use)) = 15.3.4
Provides: bundled(npm(redux)) = 3.7.2
Provides: bundled(npm(redux-persist)) = 4.10.2
Provides: bundled(npm(redux-thunk)) = 2.3.0
Provides: bundled(npm(ts-jest)) = 26.3.0
Provides: bundled(npm(utility-types)) = 3.10.0


%description
This Grafana plugin for Performance Co-Pilot includes datasources for
scalable time series from pmseries(1) and Redis, live PCP metrics and
bpftrace scripts from pmdabpftrace(1), as well as several dashboards.

%prep
%setup -q -T -D -b 0
%setup -q -T -D -b 1
%if %{compile_frontend} == 0
%setup -q -T -D -b 2
%endif

# Set up Go build subdir and links
mkdir -p %{_builddir}/src/github.com/performancecopilot
ln -s %{_builddir}/%{name}-%{version} \
    %{_builddir}/src/github.com/performancecopilot/grafana-pcp


%build
# Build frontend datasources
%if %{compile_frontend}
make dist-dashboards dist-frontend
# webpack/copy-webpack-plugin sometimes outputs files with mode = 666 due to reasons unknown (race condition/umask issue afaics)
chmod -R g-w,o-w dist
%endif

# Build backend datasource
cd %{_builddir}/src/github.com/performancecopilot/grafana-pcp
export GOPATH=%{_builddir}
%gobuild -o dist/datasources/redis/pcp_redis_datasource_$(go env GOOS)_$(go env GOARCH) ./pkg


%install
install -d -m 755 %{buildroot}/%{install_dir}
cp -a dist/* %{buildroot}/%{install_dir}

%postun
# uninstall of old package
%systemd_postun_with_restart grafana-server.service

%posttrans
# install or upgrade of new package
if [ -x /usr/bin/systemctl ]; then
  /usr/bin/systemctl try-restart grafana-server.service || :
fi


%check
# Test frontend datasources
%if %{compile_frontend}
yarn test
%endif

# Test backend datasource
cd %{_builddir}/src/github.com/performancecopilot/grafana-pcp
export GOPATH=%{_builddir}
%gotest ./pkg/...


%files
%{install_dir}

%license LICENSE NOTICE
%doc README.md


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Andreas Gerstmayr <agerstmayr@redhat.com> 3.0.2-1
- update to 3.0.2 tagged upstream community sources, see CHANGELOG

* Wed Dec 23 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 3.0.1-1
- update to 3.0.1 tagged upstream community sources, see CHANGELOG

* Thu Nov 26 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 3.0.0-1
- update to 3.0.0 tagged upstream community sources, see CHANGELOG
- bundle golang dependencies and (optionally) node.js dependencies

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 2.0.2-1
- vector, redis: remove autocompletion cache (PCP metrics can be added and removed dynamically)

* Thu Feb 20 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 2.0.1-1
- support for Grafana 6.6+, drop support for Grafana < 6.6
- vector, bpftrace: fix version checks on dashboard load (prevent multiple pmcd.version checks on dashboard load)
- vector, bpftrace: change datasource check box to red if URL is inaccessible
- redis: add tests
- flame graphs: support multidimensional eBPF maps (required to display e.g. the process name)
- dashboards: remove BCC metrics from Vector host overview (because the BCC PMDA is not installed by default)
- misc: update dependencies
- build: fix production build (implement workaround for https://github.com/systemjs/systemjs/issues/2117, https://github.com/grafana/grafana/issues/21785)

* Wed Jan 29 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.7-1
- redis: fix timespec (fixes empty graphs for large time ranges)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.6-1
- redis: support wildcards in metric names
- redis: fix label support
- redis: fix legends
- redis: set default sample interval to 60s (fixes empty graph borders)
- build: upgrade copy-webpack-plugin to mitigate XSS vulnerability in the serialize-javascript transitive dependency
- build: remove deprecated uglify-webpack-plugin

* Thu Dec 12 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.4-2
- remove node_modules/node-notifier directory from webpack (due to licensing issues)

* Wed Dec 11 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.4-1
- flame graphs: clean flame graph stacks every 5s (reduces CPU load)
- general: implement PCP version checks
- build: remove weak dependency (doesn't work with Node.js 12)
- build: upgrade terser-webpack-plugin to mitigate XSS vulnerability in the serialize-javascript transitive dependency

* Tue Nov 26 2019 Nathan Scott <nathans@redhat.com> 1.0.3-1
- fix flame graph dependency (flamegraph.destroy error in javascript console)

* Tue Nov 12 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.2-1
- handle counter wraps (overflows)
- convert time based counters to time utilization
- flame graphs: aggregate stack counts by selected time range in the Grafana UI
- flame graphs: add option to hide idle stacks
- vector: fix container dropdown in query editor
- vector: remove container setting from datasource settings page
- redis: fix value transformations (e.g. rate conversation of counters)
- request more datapoints from the datasource to fill the borders of the graph panel

* Fri Oct 11 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 1.0.0-1
- bpftrace: support for Flame Graphs
- bpftrace: context-sensitive auto completion for bpftrace probes, builtin variables and functions incl. help texts
- bpftrace: parse output of bpftrace scripts (e.g. using `printf()`) as CSV and display it in the Grafana table panel
- bpftrace: sample dashboards (BPFtrace System Analysis, BPFtrace Flame Graphs)
- vector: table output: show instance name in left column
- vector: table output: support non-matching instance names (cells of metrics which don't have the specific instance will be blank)
- vector & bpftrace: if the metric/script gets changed in the query editor, immeditately stop polling the old metric/deregister the old script
- vector & bpftrace: improve pmwebd compatibility
- misc: help texts for all datasources (visible with the **[ ? ]** button in the query editor)
- misc: renamed PCP Live to PCP Vector
- misc: logos for all datasources
- misc: improved error handling

* Fri Aug 16 2019 Andreas Gerstmayr <agerstmayr@redhat.com> 0.0.7-1
- converted into a Grafana app plugin, renamed to grafana-pcp
- redis: support for instance domains, labels, autocompletion, automatic rate conversation
- live and bpftrace: initial commit of datasources

* Tue Jun 11 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.6-1
- renamed package to grafana-pcp-redis, updated README, etc

* Wed Jun 05 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.5-1
- renamed package to grafana-pcp-datasource, README, etc

* Fri May 17 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.4-1
- add suggested pmproxy URL in config html
- updated instructions and README.md now that grafana is in Fedora

* Fri Apr 12 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.3-1
- require grafana v6.1.3 or later
- install directory is now below /var/lib/grafana/plugins

* Wed Mar 20 2019 Mark Goodwin <mgoodwin@redhat.com> 0.0.2-1
- initial version

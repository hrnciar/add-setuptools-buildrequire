%global srcname msal
%global _description %{expand:The Microsoft Authentication Library for Python enables applications to
integrate with the Microsoft identity platform. It allows you to sign in users
or apps with Microsoft identities (Azure AD, Microsoft Accounts and Azure AD B2C
accounts) and obtain tokens to call Microsoft APIs such as Microsoft Graph or
your own APIs registered with the Microsoft identity platform. It is built using
industry standard OAuth2 and OpenID Connect protocols.}

Name:           python-%{srcname}
Version:        1.10.0
Release:        1%{?dist}
Summary:        Microsoft Authentication Library (MSAL) for Python

License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Use sphinx-rtd-theme to build documentation instead of furo (not available in
# Fedora, see also https://bugzilla.redhat.com/show_bug.cgi?id=1910798)
Patch1:         %{name}-1.10.0-doc.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist pyjwt}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
# Required for documentation
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%if 0%{?fedora} <= 33
BuildRequires:  fonts-srpm-macros
%endif
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{_description}


%package doc
Summary:        Documentation for %{name}
%if 0%{?fedora} <= 33
Requires:       fontawesome-fonts
Requires:       google-roboto-slab-fonts
Requires:       lato-font
%endif

%description doc
This package provides documentation for %{name}.


%prep
%autosetup -n microsoft-authentication-library-for-python-%{version} -p1

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build

%make_build -C docs/ html
rm docs/_build/html/{.buildinfo,.nojekyll}


%install
%py3_install

# Drop bundled web fonts in HTML documentation
%if 0%{?fedora} <= 33
pushd docs/_build/html/_static/fonts/

for f in fontawesome-webfont.*; do
    rm "$f"
    [[ "${f##*.}" = "ttf" ]] && ln -s "%{_fontbasedir}/fontawesome/$f" .
done

pushd Lato/
rm *
for i in Bold BoldItalic Italic Regular; do
    ln -s "%{_fontbasedir}/lato/Lato-$i.ttf" "lato-${i,,}.ttf"
done
popd

pushd RobotoSlab/
rm *
for i in Bold Regular; do
    ln -s "%{_fontbasedir}/google-roboto-slab-fonts/RobotoSlab-$i.ttf" "roboto-slab-v7-${i,,}.ttf"
done
popd
popd
%endif


%check
# Tests requiring an Internet connection are disabled
%pytest \
    --deselect=tests/test_application.py::TestApplicationForRefreshInBehaviors::test_aging_token_and_available_aad_should_return_new_token \
    --deselect=tests/test_application.py::TestApplicationForRefreshInBehaviors::test_aging_token_and_unavailable_aad_should_return_old_token \
    --deselect=tests/test_application.py::TestApplicationForRefreshInBehaviors::test_expired_token_and_available_aad_should_return_new_token \
    --deselect=tests/test_application.py::TestApplicationForRefreshInBehaviors::test_expired_token_and_unavailable_aad_should_return_error \
    --deselect=tests/test_application.py::TestApplicationForRefreshInBehaviors::test_fresh_token_should_be_returned_from_cache \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentErrorBehaviors::test_acquire_token_silent_will_suppress_error \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentErrorBehaviors::test_acquire_token_silent_with_error_will_return_error \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentErrorBehaviors::test_atswe_will_map_some_suberror_to_classification_as_is \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentErrorBehaviors::test_atswe_will_map_some_suberror_to_classification_to_empty_string \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentErrorBehaviors::test_cache_empty_will_be_returned_as_None \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentFociBehaviors::test_family_app_remove_account \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentFociBehaviors::test_known_orphan_app_will_skip_frt_and_only_use_its_own_rt \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentFociBehaviors::test_preexisting_family_app_will_attempt_frt_and_return_error \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentFociBehaviors::test_unknown_family_app_will_attempt_frt_and_join_family \
    --deselect=tests/test_application.py::TestClientApplicationAcquireTokenSilentFociBehaviors::test_unknown_orphan_app_will_attempt_frt_and_not_remove_it \
    --deselect=tests/test_application.py::TestClientApplicationForAuthorityMigration::test_acquire_token_silent_should_find_at_under_different_alias \
    --deselect=tests/test_application.py::TestClientApplicationForAuthorityMigration::test_acquire_token_silent_should_find_rt_under_different_alias \
    --deselect=tests/test_application.py::TestClientApplicationForAuthorityMigration::test_get_accounts_should_find_accounts_under_different_alias \
    --deselect=tests/test_authority.py::TestAuthority::test_unknown_host_wont_pass_instance_discovery \
    --deselect=tests/test_authority.py::TestAuthority::test_wellknown_host_and_tenant \
    --deselect=tests/test_authority.py::TestAuthorityInternalHelperUserRealmDiscovery::test_memorize \
    --deselect=tests/test_authority_patch.py::TestAuthorityHonorsPatchedRequests::test_authority_honors_a_patched_requests \
    --deselect=tests/test_e2e.py::SshCertTestCase::test_ssh_cert_for_user \


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%files doc
%doc docs/_build/html/
%license LICENSE


%changelog
* Sun Mar 21 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Sat Feb 13 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Fri Jul 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sat Jun 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1
- Enable tests
- Add documentation subpackage

* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-1
- Initial RPM release

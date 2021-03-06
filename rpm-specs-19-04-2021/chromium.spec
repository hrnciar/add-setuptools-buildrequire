%define _lto_cflags %{nil}

%global numjobs 10
%ifarch aarch64
%global numjobs 8
%endif

# This flag is so I can build things very fast on a giant system.
# Do not enable in Koji builds.
%global use_all_cpus 0

%if %{use_all_cpus}
%global numjobs %{_smp_build_ncpus}
%endif

# Fancy build status, so we at least know, where we are..
# %1 where
# %2 what
%global build_target() \
	export NINJA_STATUS="[%2:%f/%t] " ; \
	../depot_tools/ninja -j %{numjobs} -C '%1' -vvv '%2'


# This was faster when it worked, but it didn't always.
# As of chromium 80, it is no longer supported. RIP.
%global use_jumbo 0

# We usually want this.
%global build_headless 1

# This doesn't work and it doesn't even build as of Chromium 83
%global build_remoting 1

# We'd like to always have this on...
# ... but the libva in EL7 is too old.
%if 0%{?rhel} == 7
%global use_vaapi 0
%else
%global use_vaapi 1
%endif

# Seems like we might need this sometimes
# Practically, no. But it's here in case we do.
%global use_gold 0

# 2020-08-20: F33+ aarch64 has a binutils bug trying to link clear_key_cdm
# https://bugzilla.redhat.com/show_bug.cgi?id=1869884
%global build_clear_key_cdm 1

# Since no one liked replacing just the media components, we do not build shared anymore.
%global shared 0

# NEVER EVER EVER turn this on in official builds
%global freeworld 0
%if %{freeworld}
%global lsuffix freeworld
%if 0%{?shared}
%global nsuffix -libs-media-freeworld
%else
%global nsuffix -freeworld
%endif
%else
%global lsuffix fedora
%global nsuffix %{nil}
%endif

# Disabled because of Google, starting with Chromium 88.
%global userestrictedapikeys 0
# We can still use the api key though. For now.
%global useapikey 1

# Leave this alone, please.
%global builddir out/Release
%global headlessbuilddir out/Headless
%global remotingbuilddir out/Remoting

# Debuginfo packages aren't very useful here. If you need to debug
# you should do a proper debug build (not implemented in this spec yet)
%global debug_package %{nil}

# %%{nil} for Stable; -beta for Beta; -dev for Devel
# dash in -beta and -dev is intentional !
%global chromium_channel %{nil}
%global chromium_menu_name Chromium
%global chromium_browser_channel chromium-browser%{chromium_channel}
%global chromium_path %{_libdir}/chromium-browser%{chromium_channel}
%global crd_path %{_libdir}/chrome-remote-desktop

# We don't want any libs in these directories to generate Provides
# Requires is trickier.

# To generate this list, go into %%{buildroot}%%{chromium_path} and run
# for i in `find . -name "*.so" | sort`; do NAME=`basename -s .so $i`; printf "$NAME|"; done
# for RHEL7, append libfontconfig to the end
# make sure there is not a trailing | at the end of the list

# We don't really need to do this unless we're building shared.

%if 0%{?shared}

%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so|%{chromium_path}/lib/.*\\.so.*
%if 0%{?rhel} == 7
%global privlibs libaccessibility|libandroid_mojo_bindings_shared|libanimation|libapdu|libaura|libaura_extra|libauthenticator_test_mojo_bindings_shared|libbase|libbase_i18n|libbindings|libbindings_base|libblink_common|libblink_controller|libblink_core|libblink_embedded_frame_sink_mojo_bindings_shared|libblink_features|libblink_modules|libblink_mojom_broadcastchannel_bindings_shared|libblink_platform|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture_base|libcapture_lib|libcbor|libcc|libcc_animation|libcc_base|libcc_debug|libcc_ipc|libcc_mojo_embedder|libcc_paint|libcertificate_matching|libcert_verifier|libchrome_features|libchromium_sqlite3|libclearkeycdm|libclient|libcloud_policy_proto_generated_compile|libcodec|libcolor_space|libcolor_utils|libcommon|libcompositor|libcontent|libcontent_common_mojo_bindings_shared|libcontent_public_common_mojo_bindings_shared|libcontent_service_cpp|libcontent_service_mojom|libcontent_service_mojom_shared|libcontent_settings_features|libcrash_key_lib|libcrcrypto|libcrdtp|libdbus|libdevice_base|libdevice_event_log|libdevice_features|libdevice_gamepad|libdevices|libdevice_vr|libdevice_vr_mojo_bindings|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libdevice_vr_test_mojo_bindings|libdevice_vr_test_mojo_bindings_blink|libdevice_vr_test_mojo_bindings_shared|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libdom_storage_mojom|libdom_storage_mojom_shared|libEGL|libEGL|libembedder|libembedder_switches|libevents|libevents_base|libevents_devices_x11|libevents_ozone_layout|libevents_x|libextras|libffmpeg|libfido|libfingerprint|libfreetype_harfbuzz|libgamepad_mojom|libgamepad_mojom_blink|libgamepad_mojom_shared|libgamepad_shared_typemap_traits|libgcm|libgeometry|libgeometry_skia|libgesture_detection|libgfx|libgfx_ipc|libgfx_ipc_buffer_types|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_switches|libgfx_x11|libgin|libgles2|libgles2_implementation|libgles2_utils|libGLESv2|libGLESv2|libgl_init|libgl_in_process_context|libgl_wrapper|libgpu|libgpu_ipc_service|libgtkui|libheadless_non_renderer|libhost|libicui18n|libicuuc|libinterfaces_shared|libipc|libipc_mojom|libipc_mojom_shared|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|liblearning_common|liblearning_impl|libleveldatabase|libleveldb_proto|libmanager|libmedia|libmedia_blink|libmedia_gpu|libmedia_learning_mojo_impl|libmedia_message_center|libmedia_mojo_services|libmedia_session_base_cpp|libmedia_session_cpp|libmedia_webrtc|libmemory_instrumentation|libmenu|libmessage_center|libmessage_support|libmetrics_cpp|libmidi|libmirroring_service|libmojo_base_lib|libmojo_base_mojom|libmojo_base_mojom_blink|libmojo_base_mojom_shared|libmojo_base_shared_typemap_traits|libmojo_core_embedder|libmojo_core_embedder_internal|libmojo_core_ports|libmojo_cpp_platform|libmojom_core_shared|libmojom_mhtml_load_result_shared|libmojom_modules_shared|libmojo_mojom_bindings|libmojo_mojom_bindings_shared|libmojom_platform_shared|libmojo_public_system|libmojo_public_system_cpp|libnative_theme|libnet|libnetwork_cpp|libnetwork_cpp_base|libnetwork_service|libnetwork_session_configurator|libonc|libos_crypt|libparsers|libpdfium|libperfetto|libperformace_manager_public_mojom|libperformace_manager_public_mojom_blink|libperformace_manager_public_mojom_shared|libplatform|libplatform_window|libplatform_window_common|libplatform_window_handler_libs|libpolicy_component|libpolicy_proto|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libproperties|libprotobuf_lite|libproxy_config|libpublic|librange|libraster|libresource_coordinator_public_mojom|libresource_coordinator_public_mojom_blink|libresource_coordinator_public_mojom_shared|libsandbox|libsandbox_services|libscheduling_metrics|libseccomp_bpf|libsecurity_state_features|libservice|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom|libservice_manager_mojom_blink|libservice_manager_mojom_constants|libservice_manager_mojom_constants_blink|libservice_manager_mojom_constants_shared|libservice_manager_mojom_shared|libservice_manager_mojom_traits|libservice_provider|libsessions|libshared_memory_support|libshared_with_blink|libshell_dialogs|libskia|libskia_shared_typemap_traits|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstorage_service_public|libstub_window|libsuid_sandbox_client|libsurface|libsystem_media_controls|libtab_count_metrics|libthread_linux|libtracing|libtracing_cpp|libtracing_mojom|libtracing_mojom_shared|libui_accessibility_ax_mojom|libui_accessibility_ax_mojom_blink|libui_accessibility_ax_mojom_shared|libui_base|libui_base_clipboard|libui_base_clipboard_types|libui_base_features|libui_base_idle|libui_base_ime|libui_base_ime_init|libui_base_ime_linux|libui_base_ime_types|libui_base_x|libui_data_pack|libui_devtools|libui_message_center_cpp|libui_touch_selection|liburl|liburl_ipc|liburl_matcher|libusb_shared|libuser_manager|libuser_prefs|libv8|libv8_libbase|libv8_libplatform|libviews|libviz_common|libviz_resource_format_utils|libviz_vulkan_context_provider|libVkICD_mock_icd|libvk_swiftshader|libvr_base|libvr_common|libvulkan_info|libvulkan_init|libvulkan_wrapper|libvulkan_x11|libvulkan_ycbcr_info|libweb_bluetooth_mojo_bindings_shared|libwebdata_common|libweb_dialogs|libweb_feature_mojo_bindings_mojom|libweb_feature_mojo_bindings_mojom_blink|libweb_feature_mojo_bindings_mojom_shared|libwebgpu|libweb_modal|libwebrtc_component|libwebview|libwm|libwm_public|libwtf|libwtf_support|libx11_events_platform|libx11_window|libzygote|libfontconfig
%else
%global privlibs libaccessibility|libandroid_mojo_bindings_shared|libanimation|libapdu|libaura|libaura_extra|libauthenticator_test_mojo_bindings_shared|libbase|libbase_i18n|libbindings|libbindings_base|libblink_common|libblink_controller|libblink_core|libblink_embedded_frame_sink_mojo_bindings_shared|libblink_features|libblink_modules|libblink_mojom_broadcastchannel_bindings_shared|libblink_platform|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture_base|libcapture_lib|libcbor|libcc|libcc_animation|libcc_base|libcc_debug|libcc_ipc|libcc_mojo_embedder|libcc_paint|libcertificate_matching|libcert_verifier|libchrome_features|libchromium_sqlite3|libclearkeycdm|libclient|libcloud_policy_proto_generated_compile|libcodec|libcolor_space|libcolor_utils|libcommon|libcompositor|libcontent|libcontent_common_mojo_bindings_shared|libcontent_public_common_mojo_bindings_shared|libcontent_service_cpp|libcontent_service_mojom|libcontent_service_mojom_shared|libcontent_settings_features|libcrash_key_lib|libcrcrypto|libcrdtp|libdbus|libdevice_base|libdevice_event_log|libdevice_features|libdevice_gamepad|libdevices|libdevice_vr|libdevice_vr_mojo_bindings|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libdevice_vr_test_mojo_bindings|libdevice_vr_test_mojo_bindings_blink|libdevice_vr_test_mojo_bindings_shared|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libdom_storage_mojom|libdom_storage_mojom_shared|libEGL|libEGL|libembedder|libembedder_switches|libevents|libevents_base|libevents_devices_x11|libevents_ozone_layout|libevents_x|libextras|libffmpeg|libfido|libfingerprint|libfreetype_harfbuzz|libgamepad_mojom|libgamepad_mojom_blink|libgamepad_mojom_shared|libgamepad_shared_typemap_traits|libgcm|libgeometry|libgeometry_skia|libgesture_detection|libgfx|libgfx_ipc|libgfx_ipc_buffer_types|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_switches|libgfx_x11|libgin|libgles2|libgles2_implementation|libgles2_utils|libGLESv2|libGLESv2|libgl_init|libgl_in_process_context|libgl_wrapper|libgpu|libgpu_ipc_service|libgtkui|libheadless_non_renderer|libhost|libicui18n|libicuuc|libinterfaces_shared|libipc|libipc_mojom|libipc_mojom_shared|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|liblearning_common|liblearning_impl|libleveldatabase|libleveldb_proto|libmanager|libmedia|libmedia_blink|libmedia_gpu|libmedia_learning_mojo_impl|libmedia_message_center|libmedia_mojo_services|libmedia_session_base_cpp|libmedia_session_cpp|libmedia_webrtc|libmemory_instrumentation|libmenu|libmessage_center|libmessage_support|libmetrics_cpp|libmidi|libmirroring_service|libmojo_base_lib|libmojo_base_mojom|libmojo_base_mojom_blink|libmojo_base_mojom_shared|libmojo_base_shared_typemap_traits|libmojo_core_embedder|libmojo_core_embedder_internal|libmojo_core_ports|libmojo_cpp_platform|libmojom_core_shared|libmojom_mhtml_load_result_shared|libmojom_modules_shared|libmojo_mojom_bindings|libmojo_mojom_bindings_shared|libmojom_platform_shared|libmojo_public_system|libmojo_public_system_cpp|libnative_theme|libnet|libnetwork_cpp|libnetwork_cpp_base|libnetwork_service|libnetwork_session_configurator|libonc|libos_crypt|libparsers|libpdfium|libperfetto|libperformace_manager_public_mojom|libperformace_manager_public_mojom_blink|libperformace_manager_public_mojom_shared|libplatform|libplatform_window|libplatform_window_common|libplatform_window_handler_libs|libpolicy_component|libpolicy_proto|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libproperties|libprotobuf_lite|libproxy_config|libpublic|librange|libraster|libresource_coordinator_public_mojom|libresource_coordinator_public_mojom_blink|libresource_coordinator_public_mojom_shared|libsandbox|libsandbox_services|libscheduling_metrics|libseccomp_bpf|libsecurity_state_features|libservice|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom|libservice_manager_mojom_blink|libservice_manager_mojom_constants|libservice_manager_mojom_constants_blink|libservice_manager_mojom_constants_shared|libservice_manager_mojom_shared|libservice_manager_mojom_traits|libservice_provider|libsessions|libshared_memory_support|libshared_with_blink|libshell_dialogs|libskia|libskia_shared_typemap_traits|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstorage_service_public|libstub_window|libsuid_sandbox_client|libsurface|libsystem_media_controls|libtab_count_metrics|libthread_linux|libtracing|libtracing_cpp|libtracing_mojom|libtracing_mojom_shared|libui_accessibility_ax_mojom|libui_accessibility_ax_mojom_blink|libui_accessibility_ax_mojom_shared|libui_base|libui_base_clipboard|libui_base_clipboard_types|libui_base_features|libui_base_idle|libui_base_ime|libui_base_ime_init|libui_base_ime_linux|libui_base_ime_types|libui_base_x|libui_data_pack|libui_devtools|libui_message_center_cpp|libui_touch_selection|liburl|liburl_ipc|liburl_matcher|libusb_shared|libuser_manager|libuser_prefs|libv8|libv8_libbase|libv8_libplatform|libviews|libviz_common|libviz_resource_format_utils|libviz_vulkan_context_provider|libVkICD_mock_icd|libvk_swiftshader|libvr_base|libvr_common|libvulkan_info|libvulkan_init|libvulkan_wrapper|libvulkan_x11|libvulkan_ycbcr_info|libweb_bluetooth_mojo_bindings_shared|libwebdata_common|libweb_dialogs|libweb_feature_mojo_bindings_mojom|libweb_feature_mojo_bindings_mojom_blink|libweb_feature_mojo_bindings_mojom_shared|libwebgpu|libweb_modal|libwebrtc_component|libwebview|libwm|libwm_public|libwtf|libwtf_support|libx11_events_platform|libx11_window|libzygote
%endif
%global __requires_exclude ^(%{privlibs})\\.so*

%endif

# AddressSanitizer mode
# https://www.chromium.org/developers/testing/addresssanitizer
%global asan 0

%if 0
# Chromium's fork of ICU is now something we can't unbundle.
# This is left here to ease the change if that ever switches.
BuildRequires:  libicu-devel >= 5.4
%global bundleicu 0
%else
%global bundleicu 1
%endif

%global bundlere2 1

# The libxml_utils code depends on the specific bundled libxml checkout
# which is not compatible with the current code in the Fedora package as of
# 2017-06-08.
%global bundlelibxml 1

# Fedora's Python 2 stack is being removed, we use the bundled Python libraries
# This can be revisited once we upgrade to Python 3
%global bundlepylibs 1

# RHEL 7.9 dropped minizip.
# It exists everywhere else though.
%global bundleminizip 0
%if 0%{?rhel} == 7
%global bundleminizip 1
%endif

# Chromium used to break on wayland, hidpi, and colors with gtk3 enabled.
# Hopefully it does not anymore.
%global gtk3 1

%if 0%{?rhel} == 7 || 0%{?rhel} == 8
%global dts_version 9

%global bundleopus 1
%global bundlelibusbx 1
%global bundleharfbuzz 1
%global bundlelibwebp 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%global bundlefreetype 1
%global bundlelibdrm 1
%global bundlefontconfig 1
%else
%global bundleharfbuzz 0
%global bundleopus 1
%global bundlelibusbx 0
%global bundlelibwebp 0
%global bundlelibpng 0
%global bundlelibjpeg 0
%global bundlefreetype 0
%global bundlelibdrm 0
%global bundlefontconfig 0
%endif

# Needs at least harfbuzz 2.4.0 now.
# 2019-09-13
%if 0%{?fedora} < 31
%global bundleharfbuzz 1
%else
%global bundleharfbuzz 0
%endif

### From 2013 until early 2021, Google permitted distribution builds of
### Chromium to access Google APIs that added significant features to
### Chromium including, but not limited to, Sync and geolocation.
### As of March 15, 2021, any Chromium builds which pass client_id and/or
### client_secret during build will prevent end-users from signing into their
### Google account.

### With Chromium 88, I have removed the calls to "google_default_client_id"
### and "google_default_client_secret" to comply with their changes.

### Honestly, at this point, you might be better off looking for a different
### FOSS browser.

### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%if %{useapikey}
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%else
%global api_key %nil
%endif

%if %{userestrictedapikeys}
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromoting_client_id 449907151817-8vnlfih032ni8c4jjps9int9t86k546t.apps.googleusercontent.com 
%else
%global default_client_id %nil
%global default_client_secret %nil
%global chromoting_client_id %nil
%endif

%global majorversion 89

%if %{freeworld}
Name:		chromium%{chromium_channel}%{nsuffix}
%else
Name:		chromium%{chromium_channel}
%endif
Version:	%{majorversion}.0.4389.128
Release:	1%{?dist}
%if %{?freeworld}
%if %{?shared}
# chromium-libs-media-freeworld
Summary:	Chromium media libraries built with all possible codecs
%else
# chromium-freeworld
Summary:	A WebKit (Blink) powered web browser built with all possible codecs
%endif
%else
Summary:	A WebKit (Blink) powered web browser that Google doesn't want you to use
%endif
Url:		http://www.chromium.org/Home
License:	BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)

### Chromium Fedora Patches ###
Patch0:		chromium-70.0.3538.67-sandbox-pie.patch
# Use /etc/chromium for initial_prefs
Patch1:		chromium-89.0.4389.72-initial_prefs-etc-path.patch
# Use gn system files
Patch2:		chromium-67.0.3396.62-gn-system.patch
# Do not prefix libpng functions
Patch3:		chromium-60.0.3112.78-no-libpng-prefix.patch
# Do not mangle libjpeg
Patch4:		chromium-60.0.3112.78-jpeg-nomangle.patch
# Do not mangle zlib
Patch5:		chromium-77.0.3865.75-no-zlib-mangle.patch
# Do not use unrar code, it is non-free
Patch6:		chromium-89.0.4389.72-norar.patch
# Use Gentoo's Widevine hack
# https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/chromium/files/chromium-widevine-r3.patch
Patch7:		chromium-71.0.3578.98-widevine-r3.patch
# Disable fontconfig cache magic that breaks remoting
Patch8:		chromium-83.0.4103.61-disable-fontconfig-cache-magic.patch
# drop rsp clobber, which breaks gcc9 (thanks to Jeff Law)
Patch9:	chromium-78.0.3904.70-gcc9-drop-rsp-clobber.patch
# Try to load widevine from other places
Patch10:	chromium-89.0.4389.72-widevine-other-locations.patch
# Try to fix version.py for Rawhide
Patch11:	chromium-71.0.3578.98-py2-bootstrap.patch
# Add "Fedora" to the user agent string
Patch12:	chromium-86.0.4240.75-fedora-user-agent.patch

# Needs to be submitted..
Patch51:	chromium-76.0.3809.100-gcc-remoting-constexpr.patch
# https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/chromium/files/chromium-unbundle-zlib.patch
Patch52:	chromium-81.0.4044.92-unbundle-zlib.patch
# Needs to be submitted..
Patch53:	chromium-77.0.3865.75-gcc-include-memory.patch
# https://github.com/stha09/chromium-patches/blob/master/chromium-78-protobuf-RepeatedPtrField-export.patch
Patch55:	chromium-78-protobuf-RepeatedPtrField-export.patch
# ../../third_party/perfetto/include/perfetto/base/task_runner.h:48:55: error: 'uint32_t' has not been declared
Patch56:	chromium-80.0.3987.87-missing-cstdint-header.patch
# Missing <cstring> (thanks c++17)
Patch57:	chromium-89.0.4389.72-missing-cstring-header.patch
# prepare for using system ffmpeg (clean)
# http://svnweb.mageia.org/packages/cauldron/chromium-browser-stable/current/SOURCES/chromium-53-ffmpeg-no-deprecation-errors.patch?view=markup
Patch58:	chromium-53-ffmpeg-no-deprecation-errors.patch
# https://github.com/stha09/chromium-patches/blob/chromium-89-patchset-7/chromium-89-dawn-include.patch
Patch60:	chromium-89-dawn-include.patch
# https://github.com/stha09/chromium-patches/blob/chromium-89-patchset-7/chromium-89-quiche-dcheck.patch
Patch61:	chromium-89-quiche-dcheck.patch
# https://github.com/stha09/chromium-patches/blob/chromium-89-patchset-7/chromium-89-quiche-private.patch
Patch62:	chromium-89-quiche-private.patch
# https://github.com/stha09/chromium-patches/blob/chromium-89-patchset-7/chromium-89-skia-CropRect.patch
Patch63:	chromium-89-skia-CropRect.patch
# https://github.com/stha09/chromium-patches/blob/chromium-89-patchset-7/chromium-89-AXTreeSerializer-include.patch
Patch64:	chromium-89-AXTreeSerializer-include.patch


# Silence GCC warnings during gn compile
Patch65:	chromium-84.0.4147.105-gn-gcc-cleanup.patch
# Fix missing cstring in remoting code
Patch66:	chromium-84.0.4147.125-remoting-cstring.patch
# Apply fix_textrels hack for i686 (even without lld)
Patch67:	chromium-84.0.4147.125-i686-fix_textrels.patch
# Work around binutils bug in aarch64 (F33+)
Patch68:	chromium-84.0.4147.125-aarch64-clearkeycdm-binutils-workaround.patch
# Fix sandbox code to properly handle the new way that glibc handles fstat in Fedora 34+
# Thanks to Kevin Kofler for the fix.
Patch75:	chromium-88.0.4324.96-fstatfix.patch
# Rawhide (f35) glibc defines SIGSTKSZ as a long instead of a constant
Patch76:	chromium-88.0.4324.182-rawhide-gcc-std-max-fix.patch
# Fix symbol visibility with gcc on swiftshader's libEGL
Patch77:	chromium-88.0.4324.182-gcc-fix-swiftshader-libEGL-visibility.patch
# Include support for futex_time64 (64bit time on 32bit platforms)
# https://chromium.googlesource.com/chromium/src/+/955a586c63c4f99fb734e44221db63f5b2ca25a9%5E%21/#F0
Patch78:	chromium-89.0.4389.82-support-futex_time64.patch
# Do not download proprietary widevine module in the background (thanks Debian)
Patch79:	chromium-89.0.4389.82-widevine-no-download.patch
# Fix crashes with components/cast_*
# Thanks to Gentoo
Patch80:	https://gitweb.gentoo.org/repo/gentoo.git/plain/www-client/chromium/files/chromium-89-EnumTable-crash.patch
# Fix build issues with newer libva ...
Patch81:	https://github.com/chromium/chromium/commit/7ae60470cdb0bea4548a0f5e8271b359f9450c79.patch
# ... this one is just for F35+
Patch82:	https://github.com/chromium/chromium/commit/e0b362edd9b49143b89fc76c4a31dd5603b6fbd0.patch


# Use lstdc++ on EPEL7 only
Patch101:	chromium-75.0.3770.100-epel7-stdc++.patch
# el7 only patch
Patch102:	chromium-80.0.3987.132-el7-noexcept.patch
# No linux/kcmp.h on EPEL7
Patch103:	chromium-86.0.4240.75-epel7-no-kcmp-h.patch
# Use old cups (chromium's code workaround breaks on gcc)
# Revert: https://github.com/chromium/chromium/commit/c3213f8779ddc427e89d982514185ed5e4c94e91
Patch104:	chromium-84.0.4147.89-epel7-old-cups.patch
# Still not wrong, but it seems like only EL needs it
Patch106:	chromium-77-clang.patch
# ARM failures on el8 related to int clashes
# error: incompatible types when initializing type 'int64_t' {aka 'long int'} using type 'int64x1_t'
# note: expected 'int8x16_t' but argument is of type 'uint8x16_t'
# Patch107:	chromium-84.0.4147.89-el8-arm-incompatible-ints.patch
# libdrm on EL7 is rather old and chromium assumes newer
# This gets us by for now
Patch108:	chromium-85.0.4183.83-el7-old-libdrm.patch
# EL-7 does not have sys/random.h
Patch109:	chromium-87.0.4280.66-el7-no-sys-random.patch

# VAAPI
# Upstream turned VAAPI on in Linux in 86
Patch202:	chromium-89.0.4389.72-enable-hardware-accelerated-mjpeg.patch
Patch203:	chromium-86.0.4240.75-vaapi-i686-fpermissive.patch
Patch205:	chromium-86.0.4240.75-fix-vaapi-on-intel.patch

# Apply these patches to work around EPEL8 issues
Patch300:	chromium-89.0.4389.82-rhel8-force-disable-use_gnome_keyring.patch

# And fixes for new compilers
Patch400:       %{name}-gcc11.patch

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium Fedora use chromium-latest.py --stable --ffmpegclean --ffmpegarm
# If you want to include the ffmpeg arm sources append the --ffmpegarm switch
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%%{version}.tar.xz
%if %{freeworld}
Source0:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
Source0:	chromium-%{version}-clean.tar.xz
%endif
# https://chromium.googlesource.com/chromium/tools/depot_tools.git/+archive/7e7a454f9afdddacf63e10be48f0eab603be654e.tar.gz
Source2:	depot_tools.git-master.tar.gz
Source3:	chromium-browser.sh
Source4:	%{chromium_browser_channel}.desktop
# Also, only used if you want to reproduce the clean tarball.
Source5:	clean_ffmpeg.sh
Source6:	chromium-latest.py
Source7:	get_free_ffmpeg_source_files.py
# Get the names of all tests (gtests) for Linux
# Usage: get_linux_tests_name.py chromium-%%{version} --spec
Source8:	get_linux_tests_names.py
# GNOME stuff
Source9:	chromium-browser.xml
Source11:	chrome-remote-desktop@.service
Source13:	master_preferences
# Unpackaged fonts
Source14:	https://fontlibrary.org/assets/downloads/gelasio/4d610887ff4d445cbc639aae7828d139/gelasio.zip
Source15:	http://download.savannah.nongnu.org/releases/freebangfont/MuktiNarrow-0.94.tar.bz2
Source16:	https://github.com/web-platform-tests/wpt/raw/master/fonts/Ahem.ttf
Source17:	GardinerModBug.ttf
Source18:	GardinerModCat.ttf
# RHEL 7 needs newer nodejs
%if 0%{?rhel} == 7
Source19:	https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-x64.tar.gz
%endif
# Bring xcb-proto with us (might need more than python on EPEL?)
Source20:	https://www.x.org/releases/individual/proto/xcb-proto-1.14.tar.xz

# We can assume gcc and binutils.
BuildRequires:	gcc-c++

BuildRequires:	alsa-lib-devel
BuildRequires:	atk-devel
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel
BuildRequires:	gperf
%if 0%{?bundleharfbuzz}
#nothing
%else
BuildRequires:	harfbuzz-devel >= 2.4.0
%endif
BuildRequires:	libatomic
BuildRequires:	libcap-devel
%if 0%{?bundlelibdrm}
#nothing
%else
BuildRequires:	libdrm-devel
%endif
BuildRequires:	libgcrypt-devel
BuildRequires:	libudev-devel
BuildRequires:	libuuid-devel
BuildRequires:	libusb-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXtst-devel
BuildRequires:	xcb-proto
BuildRequires:	mesa-libgbm-devel
# Old Fedora (before 30) uses the 1.2 minizip by default.
# Newer Fedora needs to use the compat package
%if 0%{?fedora} >= 30
BuildRequires:	minizip-compat-devel
%else
# RHEL 8 needs to use the compat-minizip (provided by minizip1.2)
%if 0%{?rhel} >= 8
BuildRequires:	minizip-compat-devel
%else
# RHEL 7 used to have minizip, but as of 7.9, it does not.
# BuildRequires:	minizip-devel
%endif
%endif
# RHEL 7's nodejs is too old
%if 0%{?rhel} == 7
# Use bundled.
%else
BuildRequires:	nodejs
%endif
BuildRequires:	nss-devel >= 3.26
BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel

# For screen sharing on Wayland, currently Fedora only thing - no epel
%if 0%{?fedora}
BuildRequires:	pkgconfig(libpipewire-0.2)
%endif

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

# gn needs these
BuildRequires:  libstdc++-static
BuildRequires:	libstdc++-devel, openssl-devel
# Fedora tries to use system libs whenever it can.
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	elfutils-libelf-devel
BuildRequires:	flac-devel
%if 0%{?bundlefreetype}
# nothing
%else
BuildRequires:	freetype-devel
%endif
BuildRequires:	hwdata
BuildRequires:	kernel-headers
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel
%if 0%{?bundleicu}
# If this is true, we're using the bundled icu.
# We'd like to use the system icu every time, but we cannot always do that.
%else
# Not newer than 54 (at least not right now)
BuildRequires:	libicu-devel = 54.1
%endif
%if 0%{?bundlelibjpeg}
# If this is true, we're using the bundled libjpeg
# which we need to do because the RHEL 7 libjpeg doesn't work for chromium anymore
%else
BuildRequires:	libjpeg-devel
%endif
%if 0%{?bundlelibpng}
# If this is true, we're using the bundled libpng
# which we need to do because the RHEL 7 libpng doesn't work right anymore
%else
BuildRequires:	libpng-devel
%endif
%if 0
# see https://code.google.com/p/chromium/issues/detail?id=501318
BuildRequires:	libsrtp-devel >= 1.4.4
%endif
BuildRequires:	libudev-devel
%if %{bundlelibusbx}
# Do nothing
%else
Requires:	libusbx >= 1.0.21-0.1.git448584a
BuildRequires:	libusbx-devel >= 1.0.21-0.1.git448584a
%endif
BuildRequires:	libva-devel
# We don't use libvpx anymore because Chromium loves to
# use bleeding edge revisions here that break other things
# ... so we just use the bundled libvpx.
%if %{bundlelibwebp}
# Do nothing
%else
BuildRequires:	libwebp-devel
%endif
BuildRequires:	libxslt-devel
BuildRequires:	libxshmfence-devel
# Same here, it seems.
# BuildRequires:	libyuv-devel
BuildRequires:	mesa-libGL-devel
%if %{bundleopus}
# Do nothing
%else
BuildRequires:	opus-devel
%endif
BuildRequires:	perl(Switch)
%if 0%{gtk3}
BuildRequires:	pkgconfig(gtk+-3.0)
%else
BuildRequires:	pkgconfig(gtk+-2.0)
%endif
BuildRequires:	/usr/bin/python2
BuildRequires:	python2-devel
%if 0%{?bundlepylibs}
# Using bundled bits, do nothing.
%else
%if 0%{?fedora}
BuildRequires:	python2-beautifulsoup4
BuildRequires:	python2-beautifulsoup
BuildRequires:	python2-html5lib
BuildRequires:	python2-markupsafe
BuildRequires:	python2-ply
%else
BuildRequires:	python-beautifulsoup4
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-html5lib
BuildRequires:	python-markupsafe
BuildRequires:	python-ply
%endif
BuildRequires:	python2-simplejson
%endif
%if 0%{?bundlere2}
# Using bundled bits, do nothing.
%else
Requires:	re2 >= 20160401
BuildRequires:	re2-devel >= 20160401
%endif
BuildRequires:	speech-dispatcher-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
%if 0%{?rhel} < 8
BuildRequires:	pkgconfig(gnome-keyring-1)
%endif
# remote desktop needs this
BuildRequires:	pam-devel
BuildRequires:	systemd
# for third_party/test_fonts
%if %{freeworld}
# dont need fonts for this
%else
%if 0%{?rhel} >= 7
Source100:      https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Bold.ttf
Source101:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-BoldItalic.ttf
Source102:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Italic.ttf
Source103:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Regular.ttf
Source104:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Bold.ttf
Source105:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-BoldItalic.ttf
Source106:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Italic.ttf
Source107:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Regular.ttf
Source108:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Bold.ttf
Source109:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-BoldItalic.ttf
Source110:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Italic.ttf
Source111:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Regular.ttf
%else
BuildRequires:	google-croscore-arimo-fonts
BuildRequires:	google-croscore-cousine-fonts
BuildRequires:	google-croscore-tinos-fonts
%endif
%if 0%{?rhel} == 7
Source112:	https://releases.pagure.org/lohit/lohit-gurmukhi-ttf-2.91.2.tar.gz
Source113:	https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip
%else
BuildRequires:  google-noto-sans-cjk-jp-fonts
BuildRequires:  lohit-gurmukhi-fonts
%endif
BuildRequires:	dejavu-sans-fonts
BuildRequires:	thai-scalable-garuda-fonts
BuildRequires:	lohit-devanagari-fonts
BuildRequires:	lohit-tamil-fonts
BuildRequires:	google-noto-sans-khmer-fonts
BuildRequires:	google-noto-emoji-color-fonts
%if 0%{?fedora} >= 30
BuildRequires:	google-noto-sans-symbols2-fonts
BuildRequires:	google-noto-sans-tibetan-fonts
%else
Source114:	https://github.com/googlefonts/noto-fonts/blob/master/unhinted/NotoSansSymbols2/NotoSansSymbols2-Regular.ttf
Source115:	https://github.com/googlefonts/noto-fonts/blob/master/hinted/NotoSansTibetan/NotoSansTibetan-Regular.ttf
%endif
%endif
# using the built from source version on aarch64
BuildRequires:	ninja-build
# Yes, java is needed as well..
BuildRequires:	java-1.8.0-openjdk-headless

%if 0%{?rhel} == 7
BuildRequires: devtoolset-%{dts_version}-toolchain, devtoolset-%{dts_version}-libatomic-devel
%endif

# We need to workaround a gcc 8 bug
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=94929
# https://bugs.gentoo.org/726604
%if 0%{?rhel} == 8
BuildRequires: gcc-toolset-%{dts_version}-toolchain, gcc-toolset-%{dts_version}-libatomic-devel
%endif

# There is a hardcoded check for nss 3.26 in the chromium code (crypto/nss_util.cc)
Requires:	nss%{_isa} >= 3.26
Requires:	nss-mdns%{_isa}

# GTK modules it expects to find for some reason.
%if 0%{gtk3}
Requires:	libcanberra-gtk3%{_isa}
%else
Requires:	libcanberra-gtk2%{_isa}
%endif

%if 0%{?fedora}
# This enables support for u2f tokens
Requires:	u2f-hidraw-policy
%endif

# Once upon a time, we tried to split these out... but that's not worth the effort anymore.
Provides:	chromium-ffmpegsumo = %{version}-%{release}
Obsoletes:	chromium-ffmpegsumo <= 35.0.1916.114
# This is a lie. v8 has its own version... but I'm being lazy and not using it here.
# Barring Google getting much faster on the v8 side (or much slower on the Chromium side)
# the true v8 version will be much smaller than the Chromium version that it came from.
Provides:	chromium-v8 = %{version}-%{release}
Obsoletes:	chromium-v8 <= 3.25.28.18
# This is a lie. webrtc never had any real version. 0.2 is greater than 0.1
Provides:	webrtc = 0.2
Obsoletes:	webrtc <= 0.1
Requires:	chromium-common%{_isa} = %{version}-%{release}
%if 0%{?shared}
%if 0%{?freeworld}
# chromium-libs-media-freeworld case
Provides:	chromium-libs-media = %{version}-%{release}
Provides:	chromium-libs-media%{_isa} = %{version}-%{release}
Requires:	chromium-libs%{_isa} = %{version}
Requires(post):		%{_sbindir}/update-alternatives
Requires(preun):	%{_sbindir}/update-alternatives
%else
# chromium case with shared libs
Requires:       chromium-libs%{_isa} = %{version}-%{release}
# This is broken out so it can be replaced.
Requires:	chromium-libs-media%{_isa} = %{version}-%{release}
%endif
# Nothing to do here. chromium-libs is real.
%else
Provides:	chromium-libs = %{version}-%{release}
Obsoletes:	chromium-libs <= %{version}-%{release}
%endif

%if 0%{?rhel} == 7
ExclusiveArch:  x86_64 i686
%else
ExclusiveArch:	x86_64 i686 aarch64
%endif

# Bundled bits (I'm sure I've missed some)
Provides: bundled(angle) = 2422
Provides: bundled(bintrees) = 1.0.1
# This is a fork of openssl.
Provides: bundled(boringssl)
Provides: bundled(brotli) = 222564a95d9ab58865a096b8d9f7324ea5f2e03e
Provides: bundled(bspatch)
Provides: bundled(cacheinvalidation) = 20150720
Provides: bundled(colorama) = 799604a104
Provides: bundled(crashpad)
Provides: bundled(dmg_fp)
Provides: bundled(expat) = 2.2.0
Provides: bundled(fdmlibm) = 5.3
# Don't get too excited. MPEG and other legally problematic stuff is stripped out.
Provides: bundled(ffmpeg) = 3.2git
Provides: bundled(fips181) = 2.2.3
%if 0%{?bundlefontconfig}
Provides: bundled(fontconfig) = 2.12.6
%endif
%if 0%{?bundlefreetype}
Provides: bundled(freetype) = 2.9.3
%endif
Provides: bundled(gperftools) = svn144
%if 0%{?bundleharfbuzz}
Provides: bundled(harfbuzz) = 2.4.0
%endif
Provides: bundled(hunspell) = 1.6.0
Provides: bundled(iccjpeg)
%if 0%{?bundleicu}
Provides: bundled(icu) = 58.1
%endif
Provides: bundled(kitchensink) = 1
Provides: bundled(leveldb) = 1.20
Provides: bundled(libaddressinput) = 0
%if 0%{?bundlelibdrm}
Provides: bundled(libdrm) = 2.4.85
%endif
Provides: bundled(libevent) = 1.4.15
Provides: bundled(libjingle) = 9564
%if 0%{?bundlelibjpeg}
Provides: bundled(libjpeg-turbo) = 1.4.90
%endif
Provides: bundled(libphonenumber) = a4da30df63a097d67e3c429ead6790ad91d36cf4
%if 0%{?bundlelibpng}
Provides: bundled(libpng) = 1.6.22
%endif
Provides: bundled(libsrtp) = 2cbd85085037dc7bf2eda48d4cf62e2829056e2d
%if %{bundlelibusbx}
Provides: bundled(libusbx) = 1.0.17
%endif
Provides: bundled(libvpx) = 1.6.0
%if %{bundlelibwebp}
Provides: bundled(libwebp) = 0.6.0
%endif
%if %{bundlelibxml}
# Well, it's actually newer than 2.9.4 and has code in it that has been reverted upstream... but eh.
Provides: bundled(libxml) = 2.9.4
%endif
Provides: bundled(libXNVCtrl) = 302.17
Provides: bundled(libyuv) = 1651
Provides: bundled(lzma) = 15.14
Provides: bundled(libudis86) = 1.7.1
Provides: bundled(mesa) = 9.0.3
Provides: bundled(NSBezierPath) = 1.0
Provides: bundled(mozc)
%if %{bundleopus}
Provides: bundled(opus) = 1.1.3
%endif
Provides: bundled(ots) = 8d70cffebbfa58f67a5c3ed0e9bc84dccdbc5bc0
Provides: bundled(protobuf) = 3.0.0.beta.3
Provides: bundled(qcms) = 4
%if 0%{?bundlere2}
Provides: bundled(re2)
%endif
Provides: bundled(sfntly) = 04740d2600193b14aa3ef24cd9fbb3d5996b9f77
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0
Provides: bundled(snappy) = 1.1.4-head
Provides: bundled(speech-dispatcher) = 0.7.1
Provides: bundled(sqlite) = 3.17patched
Provides: bundled(superfasthash) = 0
Provides: bundled(talloc) = 2.0.1
Provides: bundled(usrsctp) = 0
Provides: bundled(v8) = 5.9.211.31
Provides: bundled(webrtc) = 90usrsctp
Provides: bundled(woff2) = 445f541996fe8376f3976d35692fd2b9a6eedf2d
Provides: bundled(xdg-mime)
Provides: bundled(xdg-user-dirs)
# Provides: bundled(zlib) = 1.2.11

# For selinux scriptlet
Requires(post): /usr/sbin/semanage
Requires(post): /usr/sbin/restorecon
%if %{?shared}
# Do nothing
%else
Provides:	chromium-libs = %{version}-%{release}
Obsoletes:	chromium-libs <= %{version}-%{release}
Provides:	chromium-libs-media = %{version}-%{release}
Obsoletes:	chromium-libs-media <= %{version}-%{release}
# This may not actually be true (depending on how freeworld is set). But what
# is definite here is that if we're upgrading from a shared build to a static
# build none of the shared subpackages (or replacement packages) will work at
# all and without these provides/obsoletes, the upgrade transaction will fail.
# Since we have no way of conditionalizing whether the user has the freeworld
# replacement, we just assume they do.
Provides:	chromium-libs-media-freeworld = %{version}-%{release}
Obsoletes:	chromium-libs-media-freeworld <= %{version}-%{release}
%endif

%if %{?freeworld}
%if %{?shared}
%description
Chromium media libraries built with all possible codecs. Chromium is an
open-source web browser, powered by WebKit (Blink). This package replaces
the default chromium-libs-media package, which is limited in what it
can include.
%else
%description
Chromium built with all possible codecs. Chromium is an
open-source web browser, powered by WebKit (Blink).
%endif
%else
%description
Chromium is an open-source web browser, powered by WebKit (Blink).
%endif

%package common
Summary: Files needed for both the headless_shell and full Chromium
# Chromium needs an explicit Requires: minizip-compat
# We put it here to cover headless too.
%if 0%{?fedora} >= 30
Requires: minizip-compat%{_isa}
%else
%if %{?rhel} == 7
# Do nothing
%else
Requires: minizip%{_isa}
%endif
%endif
# -common doesn't have chrome-remote-desktop bits
# but we need to clean it up if it gets disabled again
# NOTE: Check obsoletes version to be sure it matches
%if ! %{build_remoting}
Provides: chrome-remote-desktop = %{version}-%{release}
Obsoletes: chrome-remote-desktop <= 81.0.4044.138
%endif

%description common
%{summary}.

%if 0%{?shared}
%package libs
Summary: Shared libraries used by chromium (and chrome-remote-desktop)
Requires: chromium-common%{_isa} = %{version}-%{release}
Requires: chromium-libs-media%{_isa} >= %{majorversion}
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description libs
Shared libraries used by chromium (and chrome-remote-desktop).

%if ! %{freeworld}
%package libs-media
Summary: Shared libraries used by the chromium media subsystem
Requires: chromium-libs%{_isa} = %{version}
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description libs-media
Shared libraries used by the chromium media subsystem.
%endif
%endif

%if %{build_remoting}
%package -n chrome-remote-desktop
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: xorg-x11-server-Xvfb
Requires: python2-psutil
%if 0%{?shared}
Requires: chromium-libs%{_isa} = %{version}-%{release}
%else
Requires: chromium-common%{_isa} = %{version}-%{release}
%endif
Summary: Remote desktop support for google-chrome & chromium

%description -n chrome-remote-desktop
Remote desktop support for google-chrome & chromium.
%endif

%package -n chromedriver
Summary:	WebDriver for Google Chrome/Chromium
%if 0%{?shared}
Requires:       chromium-libs%{_isa} = %{version}-%{release}
%else
Requires:	chromium-common%{_isa} = %{version}-%{release}
%endif
# From Russian Fedora (minus the epoch)
Provides:	chromedriver-stable = %{version}-%{release}
Conflicts:	chromedriver-testing
Conflicts:	chromedriver-unstable

%description -n chromedriver
WebDriver is an open source tool for automated testing of webapps across many
browsers. It provides capabilities for navigating to web pages, user input,
JavaScript execution, and more. ChromeDriver is a standalone server which
implements WebDriver's wire protocol for Chromium. It is being developed by
members of the Chromium and WebDriver teams.

%package headless
Summary:	A minimal headless shell built from Chromium
Requires:       chromium-common%{_isa} = %{version}-%{release}

%description headless
A minimal headless client built from Chromium. headless_shell is built
without support for alsa, cups, dbus, gconf, gio, kerberos, pulseaudio, or 
udev.

%prep
%setup -q -T -c -n depot_tools -a 2
%setup -q -n chromium-%{version}

### Chromium Fedora Patches ###
%patch0 -p1 -b .sandboxpie
%patch1 -p1 -b .etc
%patch2 -p1 -b .gnsystem
%patch3 -p1 -b .nolibpngprefix
# Upstream accidentally made the same change in 89, but they've already reverted it for 90+ so this patch will return
# %%patch4 -p1 -b .nolibjpegmangle
%patch5 -p1 -b .nozlibmangle
%patch6 -p1 -b .nounrar
%patch7 -p1 -b .widevine-hack
%patch8 -p1 -b .nofontconfigcache
%patch9 -p1 -b .gcc9
%patch10 -p1 -b .widevine-other-locations
%patch11 -p1 -b .py2

# Short term fixes (usually gcc and backports)
%patch51 -p1 -b .gcc-remoting-constexpr
%if 0%{?fedora} || 0%{?rhel} >= 8
%patch52 -p1 -b .unbundle-zlib
%endif
%patch53 -p1 -b .gcc-include-memory
%patch55 -p1 -b .protobuf-export
%patch56 -p1 -b .missing-cstdint
%patch57 -p1 -b .missing-cstring
%patch58 -p1 -b .ffmpeg-deprecations
%patch60 -p1 -b .dawn-include
%patch61 -p1 -b .quiche-dcheck
%patch62 -p1 -b .quiche-private
%patch63 -p1 -b .skia-CropRect
%patch64 -p1 -b .AXTreeSerializer-include
%patch65 -p1 -b .gn-gcc-cleanup
%patch66 -p1 -b .remoting-cstring
%patch67 -p1 -b .i686-textrels
%patch68 -p1 -b .aarch64-clearkeycdm-binutils-workaround
%patch75 -p1 -b .fstatfix
%if 0%{?fedora} >= 35
%patch76 -p1 -b .sigstkszfix
%endif
%patch77 -p1 -b .gcc-swiftshader-visibility
%patch78 -p1 -b .futex-time64
%patch79 -p1 -b .widevine-no-download
%patch80 -p1 -b .EnumTable-crash
%patch81 -p1 -b .libva-forward-compat
%if 0%{?fedora} >= 35
%patch82 -p1 -b .libva-no-legacy
%endif

# Fedora branded user agent
%if 0%{?fedora}
%patch12 -p1 -b .fedora-user-agent
%endif

# EPEL specific patches
%if 0%{?rhel} == 7
# %%patch101 -p1 -b .epel7
# %%patch102 -p1 -b .el7-noexcept
%patch103 -p1 -b .epel7-kcmp
%patch104 -p1 -b .el7cups
%patch108 -p1 -b .el7-old-libdrm
%patch109 -p1 -b .el7-no-sys-random
%endif

%if 0%{?rhel} == 8
# %%patch107 -p1 -b .el8-arm-incompatible-ints
%endif

# Feature specific patches
%if %{use_vaapi}
%patch202 -p1 -b .accel-mjpeg
%ifarch i686
%patch203 -p1 -b .i686permissive
%endif
%patch205 -p1 -b .vaapi-intel-fix
%endif

%if 0%{?rhel} == 8
%patch300 -p1 -b .disblegnomekeyring
%endif

%patch400 -p1 -b .gcc11

# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +

%if 0%{?asan}
export CC="clang"
export CXX="clang++"
%else
export CC="gcc"
export CXX="g++"
%endif
export AR="ar"
export RANLIB="ranlib"

rm -rf buildtools/third_party/libc++/BUILD.gn

# Unpack fonts
%if %{freeworld}
# no font fun needed.
%else
pushd third_party/test_fonts
mkdir test_fonts
cd test_fonts
unzip %{SOURCE14}
tar xf %{SOURCE15}
mv MuktiNarrow0.94/MuktiNarrow.ttf .
rm -rf MuktiNarrow0.94
cp %{SOURCE16} .
cp %{SOURCE17} .
cp %{SOURCE18} .
%if 0%{?rhel} >= 7
cp %{SOURCE100} .
cp %{SOURCE101} .
cp %{SOURCE102} .
cp %{SOURCE103} .
cp %{SOURCE104} .
cp %{SOURCE105} .
cp %{SOURCE106} .
cp %{SOURCE107} .
cp %{SOURCE108} .
cp %{SOURCE109} .
cp %{SOURCE110} .
cp %{SOURCE111} .
%else
%if 0%{?fedora} >= 33
cp -a /usr/share/fonts/google-arimo-fonts/Arimo-*.ttf .
cp -a /usr/share/fonts/google-cousine-fonts/Cousine-*.ttf .
cp -a /usr/share/fonts/google-tinos-fonts/Tinos-*.ttf .
%else
cp -a /usr/share/fonts/google-croscore/Arimo-*.ttf .
cp -a /usr/share/fonts/google-croscore/Cousine-*.ttf .
cp -a /usr/share/fonts/google-croscore/Tinos-*.ttf .
%endif
%endif
%if 0%{?rhel} == 7
tar xf %{SOURCE112}
mv lohit-gurmukhi-ttf-2.91.2/Lohit-Gurmukhi.ttf .
rm -rf lohit-gurmukhi-ttf-2.91.2
unzip %{SOURCE113}
%else
cp -a /usr/share/fonts/lohit-gurmukhi/Lohit-Gurmukhi.ttf .
cp -a /usr/share/fonts/google-noto-cjk/NotoSansCJKjp-Regular.otf .
%endif
%if 0%{?fedora} >= 32
cp -a /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf /usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf .
%else
cp -a /usr/share/fonts/dejavu/DejaVuSans.ttf /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf .
%endif
%if 0%{?fedora} >= 33
cp -a /usr/share/fonts/thai-scalable/Garuda.otf .
sed -i 's|Garuda.ttf|Garuda.otf|g' ../BUILD.gn
%else
cp -a /usr/share/fonts/thai-scalable/Garuda.ttf .
%endif
cp -a /usr/share/fonts/lohit-devanagari/Lohit-Devanagari.ttf /usr/share/fonts/lohit-tamil/Lohit-Tamil.ttf .
cp -a /usr/share/fonts/google-noto/NotoSansKhmer-Regular.ttf .
cp -a /usr/share/fonts/google-noto-emoji/NotoColorEmoji.ttf .
%if 0%{?fedora} >= 30
cp -a /usr/share/fonts/google-noto/NotoSansSymbols2-Regular.ttf /usr/share/fonts/google-noto/NotoSansTibetan-Regular.ttf .
%else
cp -a %{SOURCE114} %{SOURCE115} .
%endif
popd
%endif

# Core defines are flags that are true for both the browser and headless.
CHROMIUM_CORE_GN_DEFINES=""
CHROMIUM_CORE_GN_DEFINES+=' is_debug=false'
%ifarch x86_64 aarch64
CHROMIUM_CORE_GN_DEFINES+=' system_libdir="lib64"'
%endif
%if %{useapikey}
CHROMIUM_CORE_GN_DEFINES+=' google_api_key="%{api_key}"'
%endif
%if %{userestrictedapikeys}
CHROMIUM_CORE_GN_DEFINES+=' google_default_client_id="%{default_client_id}" google_default_client_secret="%{default_client_secret}"'
%endif
CHROMIUM_CORE_GN_DEFINES+=' is_clang=false use_sysroot=false fieldtrial_testing_like_official_build=true use_lld=false rtc_enable_symbol_export=true'
%if %{use_gold}
CHROMIUM_CORE_GN_DEFINES+=' use_gold=true'
%else
CHROMIUM_CORE_GN_DEFINES+=' use_gold=false'
%endif

%if %{freeworld}
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="ChromeOS" proprietary_codecs=true'
%else
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="Chromium" proprietary_codecs=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' treat_warnings_as_errors=false'
CHROMIUM_CORE_GN_DEFINES+=' use_custom_libcxx=false'
CHROMIUM_CORE_GN_DEFINES+=' use_kerberos=true'
%ifarch aarch64
CHROMIUM_CORE_GN_DEFINES+=' target_cpu="arm64"'
%endif
%if %{?use_jumbo}
CHROMIUM_CORE_GN_DEFINES+=' use_jumbo_build=true jumbo_file_merge_limit=8'
%endif
%if 0%{?rhel} == 8
CHROMIUM_CORE_GN_DEFINES+=' use_gnome_keyring=false use_glib=true'
%endif
export CHROMIUM_CORE_GN_DEFINES

CHROMIUM_BROWSER_GN_DEFINES=""
CHROMIUM_BROWSER_GN_DEFINES+=' use_gio=true use_pulseaudio=true icu_use_data_file=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_nacl=false'
%if 0%{?shared}
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=true is_component_build=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=false is_component_build=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' blink_symbol_level=0 enable_hangout_services_extension=true'
CHROMIUM_BROWSER_GN_DEFINES+=' use_aura=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_widevine=true'
%if %{use_vaapi}
%if 0%{?fedora} >= 28
CHROMIUM_BROWSER_GN_DEFINES+=' use_vaapi=true'
%endif
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_vaapi=false'
%endif
%if 0%{?fedora}
CHROMIUM_BROWSER_GN_DEFINES+=' rtc_use_pipewire=true rtc_link_pipewire=true'
%endif
export CHROMIUM_BROWSER_GN_DEFINES

CHROMIUM_HEADLESS_GN_DEFINES=""
CHROMIUM_HEADLESS_GN_DEFINES+=' use_ozone=true ozone_auto_platforms=false ozone_platform="headless" ozone_platform_headless=true'
CHROMIUM_HEADLESS_GN_DEFINES+=' headless_use_embedded_resources=false icu_use_data_file=false v8_use_external_startup_data=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' enable_nacl=false enable_print_preview=false enable_remoting=false use_alsa=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_cups=false use_dbus=false use_gio=false use_kerberos=false use_libpci=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_pulseaudio=false use_udev=false use_gtk=false use_glib=false use_x11=false'
export CHROMIUM_HEADLESS_GN_DEFINES

%if 0%{?rhel} == 7
pushd third_party/node/linux
tar xf %{SOURCE19}
mv node-v10.15.3-linux-x64 node-linux-x64
popd
%else
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node
%endif

# Remove most of the bundled libraries. Libraries specified below (taken from
# Gentoo's Chromium ebuild) are the libraries that needs to be preserved.
build/linux/unbundle/remove_bundled_libraries.py \
	'base/third_party/cityhash' \
	'base/third_party/cityhash_v103' \
	'base/third_party/double_conversion' \
	'base/third_party/dynamic_annotations' \
	'base/third_party/icu' \
	'base/third_party/libevent' \
	'base/third_party/nspr' \
	'base/third_party/superfasthash' \
	'base/third_party/symbolize' \
	'base/third_party/valgrind' \
	'base/third_party/xdg_mime' \
	'base/third_party/xdg_user_dirs' \
	'buildtools/third_party/libc++' \
	'buildtools/third_party/libc++abi' \
	'chrome/third_party/mozilla_security_manager' \
	'courgette/third_party' \
	'net/third_party/mozilla_security_manager' \
	'net/third_party/nss' \
	'net/third_party/quiche' \
	'net/third_party/uri_template' \
	'third_party/abseil-cpp' \
	'third_party/angle' \
	'third_party/angle/src/common/third_party/base' \
	'third_party/angle/src/common/third_party/smhasher' \
	'third_party/angle/src/common/third_party/xxhash' \
	'third_party/angle/src/third_party/compiler' \
	'third_party/angle/src/third_party/libXNVCtrl' \
	'third_party/angle/src/third_party/trace_event' \
	'third_party/angle/src/third_party/volk' \
	'third_party/apple_apsl' \
	'third_party/axe-core' \
	'third_party/blanketjs' \
	'third_party/blink' \
	'third_party/boringssl' \
	'third_party/boringssl/src/third_party/fiat' \
	'third_party/breakpad' \
	'third_party/breakpad/breakpad/src/third_party/curl' \
	'third_party/brotli' \
	'third_party/catapult' \
	'third_party/catapult/common/py_vulcanize/third_party/rcssmin' \
	'third_party/catapult/common/py_vulcanize/third_party/rjsmin' \
	'third_party/catapult/third_party/beautifulsoup4' \
	'third_party/catapult/third_party/google-endpoints' \
	'third_party/catapult/third_party/html5lib-python' \
	'third_party/catapult/third_party/polymer' \
	'third_party/catapult/third_party/six' \
	'third_party/catapult/tracing/third_party/d3' \
	'third_party/catapult/tracing/third_party/gl-matrix' \
	'third_party/catapult/tracing/third_party/jpeg-js' \
	'third_party/catapult/tracing/third_party/jszip' \
	'third_party/catapult/tracing/third_party/mannwhitneyu' \
	'third_party/catapult/tracing/third_party/oboe' \
	'third_party/catapult/tracing/third_party/pako' \
        'third_party/ced' \
	'third_party/cld_3' \
	'third_party/closure_compiler' \
	'third_party/crashpad' \
	'third_party/crashpad/crashpad/third_party/lss' \
	'third_party/crashpad/crashpad/third_party/zlib/' \
	'third_party/crc32c' \
	'third_party/cros_system_api' \
	'third_party/dav1d' \
	'third_party/dawn' \
	'third_party/depot_tools' \
	'third_party/devscripts' \
	'third_party/devtools-frontend' \
	'third_party/devtools-frontend/src/third_party/typescript' \
	'third_party/devtools-frontend/src/front_end/third_party/acorn' \
	'third_party/devtools-frontend/src/front_end/third_party/axe-core' \
	'third_party/devtools-frontend/src/front_end/third_party/chromium' \
	'third_party/devtools-frontend/src/front_end/third_party/codemirror' \
	'third_party/devtools-frontend/src/front_end/third_party/fabricjs' \
	'third_party/devtools-frontend/src/front_end/third_party/i18n' \
	'third_party/devtools-frontend/src/front_end/third_party/intl-messageformat' \
	'third_party/devtools-frontend/src/front_end/third_party/lighthouse' \
	'third_party/devtools-frontend/src/front_end/third_party/lit-html' \
	'third_party/devtools-frontend/src/front_end/third_party/lodash-isequal' \
	'third_party/devtools-frontend/src/front_end/third_party/marked' \
	'third_party/devtools-frontend/src/front_end/third_party/puppeteer' \
	'third_party/devtools-frontend/src/front_end/third_party/wasmparser' \
	'third_party/dom_distiller_js' \
	'third_party/emoji-segmenter' \
	'third_party/expat' \
	'third_party/ffmpeg' \
	'third_party/flac' \
        'third_party/flatbuffers' \
	'third_party/fontconfig' \
	'third_party/freetype' \
	'third_party/fusejs' \
	'third_party/google_input_tools' \
	'third_party/google_input_tools/third_party/closure_library' \
	'third_party/google_input_tools/third_party/closure_library/third_party/closure' \
	'third_party/google_trust_services' \
	'third_party/googletest' \
	'third_party/grpc' \
	'third_party/harfbuzz-ng' \
	'third_party/hunspell' \
	'third_party/iccjpeg' \
	'third_party/icu' \
	'third_party/inspector_protocol' \
	'third_party/jinja2' \
	'third_party/jsoncpp' \
	'third_party/jstemplate' \
	'third_party/khronos' \
	'third_party/leveldatabase' \
	'third_party/libXNVCtrl' \
	'third_party/libaddressinput' \
	'third_party/libaom' \
	'third_party/libaom/source/libaom/third_party/vector' \
	'third_party/libaom/source/libaom/third_party/x86inc' \
	'third_party/libavif' \
	'third_party/libdrm' \
	'third_party/libgifcodec' \
	'third_party/libjingle' \
	'third_party/libjpeg_turbo' \
	'third_party/libphonenumber' \
	'third_party/libpng' \
	'third_party/libsecret' \
        'third_party/libsrtp' \
	'third_party/libsync' \
	'third_party/libudev' \
	'third_party/liburlpattern' \
	'third_party/libusb' \
	'third_party/libva_protected_content' \
	'third_party/libvpx' \
	'third_party/libvpx/source/libvpx/third_party/x86inc' \
	'third_party/libwebm' \
	'third_party/libwebp' \
	'third_party/libx11' \
	'third_party/libxcb-keysyms' \
	'third_party/libxml' \
	'third_party/libxml/chromium' \
	'third_party/libxslt' \
	'third_party/libyuv' \
	'third_party/lottie' \
	'third_party/lss' \
	'third_party/lzma_sdk' \
	'third_party/mako' \
%if 0%{?bundlepylibs}
	'third_party/markupsafe' \
%endif
	'third_party/mesa' \
	'third_party/metrics_proto' \
	'third_party/minigbm' \
	'third_party/modp_b64' \
	'third_party/nasm' \
	'third_party/nearby' \
	'third_party/node' \
	'third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2' \
	'third_party/one_euro_filter' \
	'third_party/opencv' \
%if %{freeworld}
	'third_party/openh264' \
%endif
	'third_party/openscreen' \
	'third_party/openscreen/src/third_party/mozilla' \
	'third_party/openscreen/src/third_party/tinycbor' \
	'third_party/opus' \
	'third_party/ots' \
	'third_party/pdfium' \
	'third_party/pdfium/third_party/agg23' \
	'third_party/pdfium/third_party/base' \
	'third_party/pdfium/third_party/bigint' \
	'third_party/pdfium/third_party/freetype' \
	'third_party/pdfium/third_party/lcms' \
	'third_party/pdfium/third_party/libopenjpeg20' \
        'third_party/pdfium/third_party/libpng16' \
        'third_party/pdfium/third_party/libtiff' \
	'third_party/pdfium/third_party/skia_shared' \
	'third_party/perfetto' \
	'third_party/perfetto/protos/third_party/chromium' \
	'third_party/pffft' \
        'third_party/ply' \
	'third_party/polymer' \
	'third_party/private-join-and-compute' \
	'third_party/private_membership' \
	'third_party/protobuf' \
	'third_party/protobuf/third_party/six' \
	'third_party/pyjson5' \
	'third_party/qcms' \
	'third_party/qunit' \
%if 0%{?bundlere2}
	'third_party/re2' \
%endif
	'third_party/rnnoise' \
	'third_party/s2cellid' \
	'third_party/schema_org' \
	'third_party/securemessage' \
	'third_party/shell-encryption' \
	'third_party/simplejson' \
	'third_party/sinonjs' \
	'third_party/skia' \
	'third_party/skia/include/third_party/skcms' \
	'third_party/skia/include/third_party/vulkan' \
	'third_party/skia/third_party/skcms' \
	'third_party/skia/third_party/vulkan' \
	'third_party/smhasher' \
	'third_party/snappy' \
	'third_party/speech-dispatcher' \
	'third_party/sqlite' \
	'third_party/swiftshader' \
	'third_party/swiftshader/third_party/astc-encoder' \
	'third_party/swiftshader/third_party/llvm-subzero' \
	'third_party/swiftshader/third_party/llvm-10.0' \
	'third_party/swiftshader/third_party/marl' \
	'third_party/swiftshader/third_party/subzero' \
	'third_party/swiftshader/third_party/SPIRV-Headers' \
	'third_party/tcmalloc' \
	'third_party/test_fonts' \
	'third_party/ukey2' \
        'third_party/usb_ids' \
	'third_party/usrsctp' \
	'third_party/vulkan' \
	'third_party/wayland' \
	'third_party/web-animations-js' \
	'third_party/webdriver' \
	'third_party/webrtc' \
	'third_party/webrtc/common_audio/third_party/ooura' \
	'third_party/webrtc/common_audio/third_party/spl_sqrt_floor' \
	'third_party/webrtc/modules/third_party/fft' \
	'third_party/webrtc/modules/third_party/g711' \
	'third_party/webrtc/modules/third_party/g722' \
	'third_party/webrtc/rtc_base/third_party/base64' \
	'third_party/webrtc/rtc_base/third_party/sigslot' \
	'third_party/widevine' \
        'third_party/woff2' \
	'third_party/wuffs' \
	'third_party/x11proto' \
	'third_party/xcbproto' \
        'third_party/xdg-utils' \
	'third_party/zxcvbn-cpp' \
        'third_party/zlib' \
	'third_party/zlib/google' \
	'tools/gn/src/base/third_party/icu' \
	'tools/grit/third_party/six' \
	'url/third_party/mozilla' \
	'v8/src/third_party/siphash' \
	'v8/src/third_party/utf8-decoder' \
	'v8/src/third_party/valgrind' \
	'v8/third_party/v8' \
	'v8/third_party/inspector_protocol' \
	--do-remove

%if ! 0%{?bundlepylibs}
# Look, I don't know. This package is spit and chewing gum. Sorry.
rm -rf third_party/markupsafe
ln -s %{python2_sitearch}/markupsafe third_party/markupsafe
# We should look on removing other python2 packages as well i.e. ply
%endif

# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc

export PATH=$PATH:%{_builddir}/depot_tools

build/linux/unbundle/replace_gn_files.py --system-libraries \
%if 0%{?bundlefontconfig}
%else
	fontconfig \
%endif
%if 0%{?bundlefreetype}
%else
	freetype \
%endif
%if 0%{?bundleharfbuzz}
%else
	harfbuzz-ng \
%endif
%if 0%{?bundleicu}
%else
	icu \
%endif
%if %{bundlelibdrm}
%else
	libdrm \
%endif
%if %{bundlelibjpeg}
%else
	libjpeg \
%endif
%if %{bundlelibpng}
%else
	libpng \
%endif
%if %{bundlelibusbx}
%else
	libusb \
%endif
%if %{bundlelibwebp}
%else
	libwebp \
%endif
%if %{bundlelibxml}
%else
	libxml \
%endif
	libxslt \
%if %{bundleopus}
%else
	opus \
%endif
%if 0%{?bundlere2}
%else
	re2 \
%endif
%if 0%{?bundleminizip}
%else
	zlib \
%endif
	flac

# fix arm gcc
sed -i 's|arm-linux-gnueabihf-|arm-linux-gnu-|g' build/toolchain/linux/BUILD.gn

%ifarch aarch64
# We don't need to cross compile while building on an aarch64 system.
sed -i 's|aarch64-linux-gnu-||g' build/toolchain/linux/BUILD.gn

# Correct the ninja file to check for aarch64, not just x86.
sed -i '/${LONG_BIT}/ a \      aarch64)\' ../depot_tools/ninja
sed -i '/aarch64)/ a \        exec "/usr/bin/ninja-build" "$@";;\' ../depot_tools/ninja
%endif
sed -i 's|exec "${THIS_DIR}/ninja-linux${LONG_BIT}"|exec "/usr/bin/ninja-build"|g' ../depot_tools/ninja

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-%{dts_version}/enable
%endif

%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-%{dts_version}/enable
%endif

# Check that there is no system 'google' module, shadowing bundled ones:
if python2 -c 'import google ; print google.__path__' 2> /dev/null ; then \
    echo "Python 2 'google' module is defined, this will shadow modules of this build"; \
    exit 1 ; \
fi

tools/gn/bootstrap/bootstrap.py -v --no-clean --gn-gen-args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES"
%{builddir}/gn --script-executable=/usr/bin/python2 gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES" %{builddir}

%if %{freeworld}
# do not need to do headless gen
%else
%if %{build_headless}
%{builddir}/gn --script-executable=/usr/bin/python2 gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_HEADLESS_GN_DEFINES" %{headlessbuilddir}
%endif
%endif

%if %{build_remoting}
%{builddir}/gn --script-executable=/usr/bin/python2 gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES" %{remotingbuilddir}
%endif

%if %{bundlelibusbx}
# no hackity hack hack
%else
# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h
# we _shouldn't need to do this, but it looks like we do.
cp -a %{_includedir}/libusb-1.0/libusb.h third_party/libusb/src/libusb/libusb.h
%endif

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Fedora Project"/' $FILE

%build
# Turning the buildsystem up to 11.
ulimit -n 4096

# unpack a local copy of the xcb-proto bits
tar xf %{SOURCE20}

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-%{dts_version}/enable
%endif

%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-%{dts_version}/enable
%endif

# Decrease the debuginfo verbosity, so it compiles in koji
%ifarch %{ix86}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

export PYTHONPATH="../../third_party/pyjson5/src:../../third_party/catapult/third_party/google-endpoints:../../xcb-proto-1.14"

echo
# Now do the full browser
%if 0%{freeworld}
%build_target %{builddir} media
%else
%if %{build_headless}
# Do headless first.
%build_target %{headlessbuilddir} headless_shell
%endif

%build_target %{builddir} chrome
%build_target %{builddir} chrome_sandbox
%build_target %{builddir} chromedriver
%if %{build_clear_key_cdm}
%build_target %{builddir} clear_key_cdm
%endif
%build_target %{builddir} policy_templates

%if %{build_remoting}
# remote client
# ../../depot_tools/ninja -C ../%{builddir} -vvv remoting_me2me_host remoting_start_host remoting_it2me_native_messaging_host remoting_me2me_native_messaging_host remoting_native_messaging_manifests remoting_resources
%build_target %{remotingbuilddir} remoting_all
%endif
%endif

%install
rm -rf %{buildroot}

%if 0%{freeworld}
	mkdir -p %{buildroot}%{chromium_path}

	pushd %{builddir}
		cp -a libffmpeg.so* %{buildroot}%{chromium_path}
		cp -a libmedia.so* %{buildroot}%{chromium_path}
		mv %{buildroot}%{chromium_path}/libffmpeg.so{,.%{lsuffix}}
		mv %{buildroot}%{chromium_path}/libffmpeg.so.TOC{,.%{lsuffix}}
		mv %{buildroot}%{chromium_path}/libmedia.so{,.%{lsuffix}}
		mv %{buildroot}%{chromium_path}/libmedia.so.TOC{,.%{lsuffix}}
	popd
%else
	mkdir -p %{buildroot}%{_bindir}
	mkdir -p %{buildroot}%{chromium_path}
	cp -a %{SOURCE3} %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	export BUILD_TARGET=`cat /etc/redhat-release`
	export CHROMIUM_PATH=%{chromium_path}
	export CHROMIUM_BROWSER_CHANNEL=%{chromium_browser_channel}
	sed -i "s|@@BUILD_TARGET@@|$BUILD_TARGET|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	sed -i "s|@@CHROMIUM_PATH@@|$CHROMIUM_PATH|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	sed -i "s|@@CHROMIUM_BROWSER_CHANNEL@@|$CHROMIUM_BROWSER_CHANNEL|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	%if "%{chromium_channel}" == "%{nil}"
		sed -i "s|@@EXTRA_FLAGS@@||g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	%else
		# Enable debug outputs for beta and dev channels
		export EXTRA_FLAGS="--enable-logging=stderr --v=2"
		sed -i "s|@@EXTRA_FLAGS@@|$EXTRA_FLAGS|g" %{buildroot}%{chromium_path}/%{chromium_browser_channel}.sh
	%endif

	ln -s %{chromium_path}/%{chromium_browser_channel}.sh %{buildroot}%{_bindir}/%{chromium_browser_channel}
	mkdir -p %{buildroot}%{_mandir}/man1/

	pushd %{builddir}
		cp -a *.pak locales resources icudtl.dat %{buildroot}%{chromium_path}
		%ifarch x86_64 i686 aarch64
			cp -a swiftshader %{buildroot}%{chromium_path}
		%endif
		cp -a chrome %{buildroot}%{chromium_path}/%{chromium_browser_channel}
		cp -a chrome_sandbox %{buildroot}%{chromium_path}/chrome-sandbox
		cp -a ../../chrome/app/resources/manpage.1.in %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
		sed -i "s|@@PACKAGE@@|%{chromium_browser_channel}|g" %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
		sed -i "s|@@MENUNAME@@|%{chromium_menu_name}|g" %{buildroot}%{_mandir}/man1/%{chromium_browser_channel}.1
		# V8 initial snapshots
		# https://code.google.com/p/chromium/issues/detail?id=421063
		cp -a snapshot_blob.bin %{buildroot}%{chromium_path}
		cp -a v8_context_snapshot.bin %{buildroot}%{chromium_path}
		cp -a xdg-mime xdg-settings %{buildroot}%{chromium_path}
		cp -a MEIPreload %{buildroot}%{chromium_path}
		# This is ANGLE, not to be confused with the similarly named files under swiftshader/
		cp -a libEGL.so* libGLESv2.so* %{buildroot}%{chromium_path}

		%if %{build_clear_key_cdm}
			%ifarch i686
				cp -a ClearKeyCdm/_platform_specific/linux_x86/libclearkeycdm.so %{buildroot}%{chromium_path}
			%else
				%ifarch x86_64
					cp -a ClearKeyCdm/_platform_specific/linux_x64/libclearkeycdm.so %{buildroot}%{chromium_path}
				%else
					%ifarch aarch64
						cp -a ClearKeyCdm/_platform_specific/linux_arm64/libclearkeycdm.so %{buildroot}%{chromium_path}
					%else
						cp -a libclearkeycdm.so %{buildroot}%{chromium_path}
					%endif
				%endif
			%endif
		%endif

		%if 0%{?shared}
			cp -a lib*.so* %{buildroot}%{chromium_path}
			# cp -p %%{buildroot}%{chromium_path}/libwidevinecdm.so{,.fedora}
			cp -p %{buildroot}%{chromium_path}/libffmpeg.so{,.%{lsuffix}}
			cp -p %{buildroot}%{chromium_path}/libffmpeg.so.TOC{,.%{lsuffix}}
			cp -p %{buildroot}%{chromium_path}/libmedia.so{,.%{lsuffix}}
			cp -p %{buildroot}%{chromium_path}/libmedia.so.TOC{,.%{lsuffix}}
		%endif

		# chromedriver
		cp -a chromedriver %{buildroot}%{chromium_path}/chromedriver
		ln -s %{chromium_path}/chromedriver %{buildroot}%{_bindir}/chromedriver

		%if %{build_remoting}
			# Remote desktop bits
			mkdir -p %{buildroot}%{crd_path}

			%if 0%{?shared}
				pushd %{buildroot}%{crd_path}
					for i in ../chromium-browser%{?chromium_channel}/lib*.so; do
						libname=`basename $i`
						ln -s $i $libname
					done
				popd
			%endif
		%endif
	popd
	%if %{build_remoting}
		pushd %{remotingbuilddir}

			# See remoting/host/installer/linux/Makefile for logic
			cp -a remoting_native_messaging_host %{buildroot}%{crd_path}/native-messaging-host
			cp -a remote_assistance_host %{buildroot}%{crd_path}/remote-assistance-host
			cp -a remoting_locales %{buildroot}%{crd_path}/
			cp -a remoting_me2me_host %{buildroot}%{crd_path}/chrome-remote-desktop-host
			cp -a remoting_start_host %{buildroot}%{crd_path}/start-host
			cp -a remoting_user_session %{buildroot}%{crd_path}/user-session
			chmod +s %{buildroot}%{crd_path}/user-session

			# chromium
			mkdir -p %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts
			# google-chrome
			mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/
			cp -a remoting/* %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/
			for i in %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/*.json; do
				sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' $i
			done
			mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts
			pushd %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts
				for i in ../../../chromium/native-messaging-hosts/*; do
					# rpm gets unhappy when we symlink here
					cp -a $i .
				done
			popd
		popd

		mkdir -p %{buildroot}/var/lib/chrome-remote-desktop
		touch %{buildroot}/var/lib/chrome-remote-desktop/hashes

		mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
		pushd %{buildroot}%{_sysconfdir}/pam.d/
			ln -s system-auth chrome-remote-desktop
		popd
	%endif

	%if %{build_headless}
		pushd %{headlessbuilddir}
			cp -a headless_lib.pak headless_shell %{buildroot}%{chromium_path}
		popd
	%endif

	%if %{build_remoting}
		cp -a remoting/host/linux/linux_me2me_host.py %{buildroot}%{crd_path}/chrome-remote-desktop
		cp -a remoting/host/installer/linux/is-remoting-session %{buildroot}%{crd_path}/

		mkdir -p %{buildroot}%{_unitdir}
		cp -a %{SOURCE11} %{buildroot}%{_unitdir}/
		sed -i 's|@@CRD_PATH@@|%{crd_path}|g' %{buildroot}%{_unitdir}/chrome-remote-desktop@.service
	%endif

	# Add directories for policy management
	mkdir -p %{buildroot}%{_sysconfdir}/chromium/policies/managed
	mkdir -p %{buildroot}%{_sysconfdir}/chromium/policies/recommended

	cp -a out/Release/gen/chrome/app/policy/common/html/en-US/*.html .
	cp -a out/Release/gen/chrome/app/policy/linux/examples/chrome.json .

	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
	cp -a chrome/app/theme/chromium/product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{chromium_browser_channel}.png
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
	cp -a chrome/app/theme/chromium/product_logo_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{chromium_browser_channel}.png
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
	cp -a chrome/app/theme/chromium/product_logo_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{chromium_browser_channel}.png
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
	cp -a chrome/app/theme/chromium/product_logo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{chromium_browser_channel}.png
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
	cp -a chrome/app/theme/chromium/product_logo_24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{chromium_browser_channel}.png

	# Install the master_preferences file
	mkdir -p %{buildroot}%{_sysconfdir}/%{name}
	install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/%{name}/

	mkdir -p %{buildroot}%{_datadir}/applications/
	desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE4}

	install -D -m0644 chrome/installer/linux/common/chromium-browser/chromium-browser.appdata.xml ${RPM_BUILD_ROOT}%{_datadir}/metainfo/%{chromium_browser_channel}.appdata.xml
	appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/metainfo/%{chromium_browser_channel}.appdata.xml

	mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps/
	cp -a %{SOURCE9} %{buildroot}%{_datadir}/gnome-control-center/default-apps/

	mkdir -p %{buildroot}%{chromium_path}/PepperFlash

# freeworld conditional
%endif

%post
# Set SELinux labels - semanage itself will adjust the lib directory naming
# But only do it when selinux is enabled, otherwise, it gets noisy.
if selinuxenabled; then
	semanage fcontext -a -t bin_t /usr/lib/%{chromium_browser_channel} &>/dev/null || :
	semanage fcontext -a -t bin_t /usr/lib/%{chromium_browser_channel}/%{chromium_browser_channel}.sh &>/dev/null || :
	semanage fcontext -a -t chrome_sandbox_exec_t /usr/lib/chrome-sandbox &>/dev/null || :
	restorecon -R -v %{chromium_path}/%{chromium_browser_channel} &>/dev/null || :
fi

%if %{build_remoting}
%pretrans -n chrome-remote-desktop -p <lua> 
path = "/etc/opt/chrome/native-messaging-hosts"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end
%endif

%if %{shared}
%if %{freeworld}
%posttrans -n chromium-libs-media-freeworld
%{_sbindir}/update-alternatives --install \
  %{_libdir}/chromium-browser/libffmpeg.so libffmpeg.so \
  %{_libdir}/chromium-browser/libffmpeg.so.freeworld 20 \
  --slave %{_libdir}/chromium-browser/libffmpeg.so.TOC libffmpeg.so.TOC \
          %{_libdir}/chromium-browser/libffmpeg.so.TOC.freeworld \
  --slave %{_libdir}/chromium-browser/libmedia.so libmedia.so \
          %{_libdir}/chromium-browser/libmedia.so.freeworld \
  --slave %{_libdir}/chromium-browser/libmedia.so.TOC libmedia.so.TOC \
          %{_libdir}/chromium-browser/libmedia.so.TOC.freeworld

%preun -n chromium-libs-media-freeworld
if [ $1 = 0 ]; then
  %{_sbindir}/alternatives --remove libffmpeg.so \
    %{_libdir}/chromium-browser/libffmpeg.so.freeworld
fi
%else
%posttrans libs-media
%{_sbindir}/update-alternatives --install \
  %{_libdir}/chromium-browser/libffmpeg.so libffmpeg.so \
  %{_libdir}/chromium-browser/libffmpeg.so.fedora 10 \
  --slave %{_libdir}/chromium-browser/libffmpeg.so.TOC libffmpeg.so.TOC \
          %{_libdir}/chromium-browser/libffmpeg.so.TOC.fedora \
  --slave %{_libdir}/chromium-browser/libmedia.so libmedia.so \
          %{_libdir}/chromium-browser/libmedia.so.fedora \
  --slave %{_libdir}/chromium-browser/libmedia.so.TOC libmedia.so.TOC \
          %{_libdir}/chromium-browser/libmedia.so.TOC.fedora

%preun libs-media
if [ $1 = 0 ]; then
  %{_sbindir}/alternatives --remove libffmpeg.so \
    %{_libdir}/chromium-browser/libffmpeg.so.fedora
fi
%endif
%endif

%if %{build_remoting}
%pre -n chrome-remote-desktop
getent group chrome-remote-desktop >/dev/null || groupadd -r chrome-remote-desktop

%post -n chrome-remote-desktop
%systemd_post chrome-remote-desktop@.service

%preun -n chrome-remote-desktop
%systemd_preun chrome-remote-desktop@.service

%postun -n chrome-remote-desktop
%systemd_postun_with_restart chrome-remote-desktop@.service
%endif

%if 0%{freeworld}
# We only build libs-media-freeworld.
%else

%files
%doc AUTHORS
%doc chrome_policy_list.html *.json
%license LICENSE
%config %{_sysconfdir}/%{name}/
# %%dir %%{_sysconfdir}/%%{name}/native-messaging-hosts
# This is chrome-remote-desktop stuff
%exclude %{_sysconfdir}/%{name}/native-messaging-hosts/*
%{_bindir}/%{chromium_browser_channel}
%dir %{chromium_path}
%{chromium_path}/*.bin
%{chromium_path}/chrome_*.pak
%{chromium_path}/resources.pak
%{chromium_path}/icudtl.dat
%{chromium_path}/%{chromium_browser_channel}
%{chromium_path}/%{chromium_browser_channel}.sh
%{chromium_path}/libEGL.so*
%{chromium_path}/libGLESv2.so*
%{chromium_path}/MEIPreload/
%ifarch x86_64 i686 aarch64
%{chromium_path}/swiftshader/
%endif
%dir %{chromium_path}/PepperFlash/
%if 0
%{chromium_path}/protoc
%endif
# %%{chromium_path}/remoting_locales/
# %%{chromium_path}/pseudo_locales/
# %%{chromium_path}/plugins/
%attr(4755, root, root) %{chromium_path}/chrome-sandbox
%{chromium_path}/xdg-mime
%{chromium_path}/xdg-settings
%{_mandir}/man1/%{chromium_browser_channel}.*
%{_datadir}/icons/hicolor/*/apps/%{chromium_browser_channel}.png
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/gnome-control-center/default-apps/chromium-browser.xml

%files common
%if %{build_headless}
%{chromium_path}/headless_lib.pak
%endif
%if %{build_clear_key_cdm}
%{chromium_path}/libclearkeycdm.so
%endif
# %%{chromium_path}/mus_app_resources_*.pak
%if 0
%{chromium_path}/pyproto/
%endif
%{chromium_path}/resources/
%dir %{chromium_path}/locales/
%lang(am) %{chromium_path}/locales/am.pak*
%lang(ar) %{chromium_path}/locales/ar.pak*
%lang(bg) %{chromium_path}/locales/bg.pak*
%lang(bn) %{chromium_path}/locales/bn.pak*
%lang(ca) %{chromium_path}/locales/ca.pak*
%lang(cs) %{chromium_path}/locales/cs.pak*
%lang(da) %{chromium_path}/locales/da.pak*
%lang(de) %{chromium_path}/locales/de.pak*
%lang(el) %{chromium_path}/locales/el.pak*
%lang(en_GB) %{chromium_path}/locales/en-GB.pak*
# Chromium _ALWAYS_ needs en-US.pak as a fallback
# This means we cannot apply the lang code here.
# Otherwise, it is filtered out on install.
%{chromium_path}/locales/en-US.pak*
%lang(es) %{chromium_path}/locales/es.pak*
%lang(es) %{chromium_path}/locales/es-419.pak*
%lang(et) %{chromium_path}/locales/et.pak*
%lang(fa) %{chromium_path}/locales/fa.pak*
%lang(fi) %{chromium_path}/locales/fi.pak*
%lang(fil) %{chromium_path}/locales/fil.pak*
%lang(fr) %{chromium_path}/locales/fr.pak*
%lang(gu) %{chromium_path}/locales/gu.pak*
%lang(he) %{chromium_path}/locales/he.pak*
%lang(hi) %{chromium_path}/locales/hi.pak*
%lang(hr) %{chromium_path}/locales/hr.pak*
%lang(hu) %{chromium_path}/locales/hu.pak*
%lang(id) %{chromium_path}/locales/id.pak*
%lang(it) %{chromium_path}/locales/it.pak*
%lang(ja) %{chromium_path}/locales/ja.pak*
%lang(kn) %{chromium_path}/locales/kn.pak*
%lang(ko) %{chromium_path}/locales/ko.pak*
%lang(lt) %{chromium_path}/locales/lt.pak*
%lang(lv) %{chromium_path}/locales/lv.pak*
%lang(ml) %{chromium_path}/locales/ml.pak*
%lang(mr) %{chromium_path}/locales/mr.pak*
%lang(ms) %{chromium_path}/locales/ms.pak*
%lang(nb) %{chromium_path}/locales/nb.pak*
%lang(nl) %{chromium_path}/locales/nl.pak*
%lang(pl) %{chromium_path}/locales/pl.pak*
%lang(pt_BR) %{chromium_path}/locales/pt-BR.pak*
%lang(pt_PT) %{chromium_path}/locales/pt-PT.pak*
%lang(ro) %{chromium_path}/locales/ro.pak*
%lang(ru) %{chromium_path}/locales/ru.pak*
%lang(sk) %{chromium_path}/locales/sk.pak*
%lang(sl) %{chromium_path}/locales/sl.pak*
%lang(sr) %{chromium_path}/locales/sr.pak*
%lang(sv) %{chromium_path}/locales/sv.pak*
%lang(sw) %{chromium_path}/locales/sw.pak*
%lang(ta) %{chromium_path}/locales/ta.pak*
%lang(te) %{chromium_path}/locales/te.pak*
%lang(th) %{chromium_path}/locales/th.pak*
%lang(tr) %{chromium_path}/locales/tr.pak*
%lang(uk) %{chromium_path}/locales/uk.pak*
%lang(vi) %{chromium_path}/locales/vi.pak*
%lang(zh_CN) %{chromium_path}/locales/zh-CN.pak*
%lang(zh_TW) %{chromium_path}/locales/zh-TW.pak*

%if %{build_headless}
%files headless
%{chromium_path}/headless_shell
%endif

%if 0%{?shared}
%files libs
%exclude %{chromium_path}/libffmpeg.so*
%exclude %{chromium_path}/libmedia.so*
# %%exclude %%{chromium_path}/libwidevinecdm.so
%{chromium_path}/lib*.so*
%endif

%if %{build_remoting}
%files -n chrome-remote-desktop
%{crd_path}/chrome-remote-desktop
%{crd_path}/chrome-remote-desktop-host
%{crd_path}/is-remoting-session
%if 0%{?shared}
%{crd_path}/lib*.so
%endif
%{crd_path}/native-messaging-host
%{crd_path}/remote-assistance-host
%{_sysconfdir}/pam.d/chrome-remote-desktop
%{_sysconfdir}/chromium/native-messaging-hosts/*
%{_sysconfdir}/opt/chrome/
%{crd_path}/remoting_locales/
%{crd_path}/start-host
%{crd_path}/user-session
%{_unitdir}/chrome-remote-desktop@.service
/var/lib/chrome-remote-desktop/
%endif

%files -n chromedriver
%doc AUTHORS
%license LICENSE
%{_bindir}/chromedriver
%{chromium_path}/chromedriver

%endif

%if 0%{?shared}
%if %{freeworld}
%files -n chromium-libs-media-freeworld
%else
%files libs-media
%endif
%{chromium_path}/libffmpeg.so.%{lsuffix}*
%{chromium_path}/libffmpeg.so.TOC.%{lsuffix}*
%{chromium_path}/libmedia.so.%{lsuffix}*
%{chromium_path}/libmedia.so.TOC.%{lsuffix}*
%endif


%changelog
* Wed Apr 14 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.128-1
- update to 89.0.4389.128

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 89.0.4389.90-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Mon Mar 29 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.90-4
- fix libva compile in rawhide

* Thu Mar 25 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.90-3
- apply upstream fix for newer system libva

* Wed Mar 24 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.90-2
- fix crashes with components/cast_*

* Thu Mar 18 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.90-1
- update to 89.0.4389.90
- disable auto-download of widevine binary only blob

* Mon Mar 15 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.82-2
- add support for futex_time64

* Mon Mar  8 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.82-1
- update to 89.0.4389.82

* Thu Mar  4 2021 Tom Callaway <spot@fedoraproject.org> - 89.0.4389.72-1
- update to 89.0.4389.72

* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 88.0.4324.182-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 25 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4234.182-2
- fix swiftshader symbols in libEGL/libGLESv2 with gcc

* Wed Feb 17 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4234.182-1
- update to 88.0.4234.182

* Fri Feb  5 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4234.150-1
- update to 88.0.4234.150

* Tue Feb  2 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4234.146-1
- update to 88.0.4234.146

* Tue Feb  2 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4234.96-4
- turn on the API key (just the API key, not the client_id or client_secret)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 88.0.4324.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4324.96-2
- apply fix from Kevin Kofler for new glibc fstat sandbox handling

* Wed Jan 20 2021 Tom Callaway <spot@fedoraproject.org> - 88.0.4324.96-1
- 88 goes from beta to stable
- disable use of api keys (Google shut off API access)

* Wed Jan 13 2021 Tom Callaway <spot@fedoraproject.org>
- update to 87.0.4280.141

* Wed Dec 30 2020 Tom Callaway <spot@fedoraproject.org> - 88.0.4324.50-1
- update to 88.0.4324.50
- drop patches 74 & 75 (applied upstream)

* Thu Dec 17 2020 Tom Callaway <spot@fedoraproject.org>
- add two patches for missing headers to build with gcc 11

* Thu Dec  3 2020 Tom Callaway <spot@fedoraproject.org> - 88.0.4324.27-1
- dev release to prepare for next stable

* Thu Dec  3 2020 Tom Callaway <spot@fedoraproject.org> - 87.0.4280.88-1
- update to 87.0.4280.88

* Wed Nov 18 2020 Tom Callaway <spot@fedoraproject.org> - 87.0.4280.66-1
- update to 87.0.4280.66

* Thu Nov 12 2020 Jeff Law <law@fedoraproject.org> - 86.0.4240.198-1
- Fix missing #inclues for gcc-11
- Fix bogus volatile caught by gcc-11

* Thu Nov 12 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.198-1
- update to 86.0.4240.198

* Tue Nov 10 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.193-1
- update to 86.0.4240.193

* Wed Nov  4 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.183-1
- update to 86.0.4240.183

* Mon Nov  2 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.111-2
- fix conditional typo that was causing console logging to be turned on

* Wed Oct 21 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.111-1
- update to 86.0.4240.111

* Tue Oct 20 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.75-2
- use bundled zlib/minizip on el7 (thanks Red Hat. :P)

* Wed Oct 14 2020 Tom Callaway <spot@fedoraproject.org> - 86.0.4240.75-1
- update to 86.0.4240.75

* Mon Sep 28 2020 Tom Callaway <spot@fedoraproject.org> - 85.0.4183.121-2
- rebuild for libevent

* Mon Sep 21 2020 Tom Callaway <spot@fedoraproject.org> - 85.0.4183.121-1
- update to 85.0.4183.121
- apply upstream fix for networking issue with CookieMonster

* Tue Sep  8 2020 Tom Callaway <spot@fedoraproject.org> - 85.0.4183.102-1
- update to 85.0.4183.102
- install ANGLE so files (libEGL.so, libGLESv2.so)

* Wed Aug 26 2020 Tom Callaway <spot@fedoraproject.org> - 85.0.4183.83-1
- update to 85.0.4183.83

* Thu Aug 20 2020 Tom Callaway <spot@fedoraproject.org> - 84.0.4147.135-1
- update to 84.0.4147.135
- conditionalize build_clear_key_cdm
- disable build_clear_key_cdm on F33+ aarch64 until binutils bug is fixed
- properly install libclearkeycdm.so everywhere else (whoops)

* Mon Aug 17 2020 Tom Callaway <spot@fedoraproject.org> - 84.0.4147.125-2
- force fix_textrels fix in ffmpeg for i686 (even without lld)

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 84.0.4147.125-1
- update to 84.0.4147.125

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 84.0.4147.105-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 31 2020 Tom Callaway <spot@fedoraproject.org> - 84.0.4147.105-1
- update to 84.0.4147.105

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 84.0.4147.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Tom Callaway <spot@fedoraproject.org> - 84.0.4147.89-1
- update to 84.0.4147.89

* Sat Jun 27 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.116-3
- only set ozone on headless
- enable use_kerberos

* Tue Jun 23 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.116-2
- do not force ozone into x11

* Tue Jun 23 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.116-1
- update to 83.0.4103.116

* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.106-1
- update to 83.0.4103.106
- remove duplicate ServiceWorker fix
- add fix to work around gcc bug on aarch64
- disable python byte compiling (we do not need it)

* Tue Jun 16 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.97-5
- add ServiceWorker fix

* Mon Jun 15 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.97-4
- use old cups handling on epel7
- fix skia attribute overrides with gcc

* Wed Jun 10 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.97-3
- fix issue on epel7 where linux/kcmp.h does not exist

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.97-2
- more fixes from gentoo

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.97-1
- update to 83.0.4103.97

* Tue Jun  2 2020 Tom Callaway <spot@fedoraproject.org> - 83.0.4103.61-1
- update to 83.0.4103.61
- conditionalize and disable remoting

* Thu May  7 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.138-1
- update to 81.0.4044.138

* Tue May  5 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.129-1
- update to 81.0.4044.129

* Thu Apr 23 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.122-1
- update to 81.0.4044.122

* Tue Apr 21 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.113-2
- add explicit Requires: chromium-common

* Thu Apr 16 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.113-1
- update to 81.0.4044.113

* Mon Apr 13 2020 Tom Callaway <spot@fedoraproject.org> - 81.0.4044.92-1
- update to 81.0.4044.92
- squelch the selinux output in the post scriptlet
- add Provides/Obsoletes in case we're build with shared set to 0
- add ulimit -n 4096 (needed for static builds, probably not harmful for shared builds either)
- do static build

* Sat Apr  4 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.163-1
- update to 80.0.3987.163

* Wed Apr  1 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.162-1
- update to 80.0.3987.162

* Wed Mar 18 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.149-1
- update to 80.0.3987.149

* Thu Feb 27 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.132-1
- update to 80.0.3987.132
- disable C++17 changes (this means f32+ will no longer build, but it segfaulted immediately)

* Thu Feb 27 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.122-1
- update to 80.0.3987.122

* Mon Feb 17 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.106-1
- update to 80.0.3987.106

* Wed Feb  5 2020 Tom Callaway <spot@fedoraproject.org> - 80.0.3987.87-1
- update to 80.0.3987.87

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 79.0.3945.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.130-1
- update to 79.0.3945.130

* Thu Jan  9 2020 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.117-1
- update to 79.0.3945.117

* Tue Dec 17 2019 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.88-1
- update to 79.0.3945.88

* Tue Dec 10 2019 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.79-1
- update to 79.0.3945.79

* Wed Dec  4 2019 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.56-2
- fix lib provides filtering

* Tue Dec  3 2019 Tom Callaway <spot@fedoraproject.org> - 79.0.3945.56-1
- update to current beta (rawhide only)
- switch to upstream patch for clock_nanosleep fix

* Mon Nov 25 2019 Tom Callaway <spot@fedoraproject.org> - 78.0.3904.108-1
- update to 78.0.3904.108

* Sun Nov 17 2019 Tom Callaway <spot@fedoraproject.org> - 78.0.3904.97-2
- allow clock_nanosleep through seccomp (bz #1773289)

* Thu Nov  7 2019 Tom Callaway <spot@fedoraproject.org> - 78.0.3904.97-1
- update to 78.0.3904.97

* Fri Nov  1 2019 Tom Callaway <spot@fedoraproject.org> - 78.0.3904.87-1
- update to 78.0.3904.87
- apply most of the freeworld changes in PR 23/24/25

* Wed Oct 23 2019 Tom Callaway <spot@fedoraproject.org> - 78.0.3904.80-1
- update to 78.0.3904.80

* Wed Oct 16 2019 Tom Callaway <spot@fedoraproject.org> - 77.0.3865.120-4
- upstream fix for zlib symbol exports with gcc

* Wed Oct 16 2019 Tom Callaway <spot@fedoraproject.org> - 77.0.3865.120-3
- silence outdated build noise (bz1745745)

* Tue Oct 15 2019 Tom Callaway <spot@fedoraproject.org> - 77.0.3865.120-2
- fix node handling for EPEL-8

* Mon Oct 14 2019 Tomas Popela <tpopela@redhat.com> - 77.0.3865.120-1
- Update to 77.0.3865.120

* Thu Oct 10 2019 Tom Callaway <spot@fedoraproject.org> - 77.0.3865.90-4
- enable aarch64 for EPEL-8

* Wed Oct  9 2019 Tom Callaway <spot@fedoraproject.org> - 77.0.3865.90-3
- spec cleanups and changes to make EPEL8 try to build

* Mon Sep 23 2019 Tomas Popela <tpopela@redhat.com> - 77.0.3865.90-2
- Fix the icon
- Remove quite a few of downstream patches
- Fix the crashes by backporting an upstream bug
- Resolves: rhbz#1754179

* Thu Sep 19 2019 Tomas Popela <tpopela@redhat.com> - 77.0.3865.90-1
- Update to 77.0.3865.90

* Mon Sep 16 2019 Tomas Popela <tpopela@redhat.com> - 77.0.3865.75-2
- Update the list of private libraries

* Fri Sep 13 2019 Tomas Popela <tpopela@redhat.com> - 77.0.3865.75-1
- Update to 77.0.3865.75

* Tue Sep 03 2019 Tomas Popela <tpopela@redhat.com> - 76.0.3809.132-2
- Backport patch to fix certificate transparency

* Tue Aug 27 2019 Tomas Popela <tpopela@redhat.com> - 76.0.3809.132-1
- Update to 76.0.3809.132

* Tue Aug 13 2019 Tomas Popela <tpopela@redhat.com> - 76.0.3809.100-1
- Update to 76.0.3809.100

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 75.0.3770.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Tom Callaway <spot@fedoraproject.org> - 75.0.3770.100-3
- apply upstream fix to resolve issue where it is dangerous to post a
  task with a RenderProcessHost pointer because the RenderProcessHost
  can go away before the task is run (causing a segfault).

* Tue Jun 25 2019 Tom Callaway <spot@fedoraproject.org> - 75.0.3770.100-2
- fix v8 compile with gcc

* Thu Jun 20 2019 Tom Callaway <spot@fedoraproject.org> - 75.0.3770.100-1
- update to 75.0.3770.100

* Fri Jun 14 2019 Tom Callaway <spot@fedoraproject.org> - 75.0.3770.90-1
- update to 75.0.3770.90

* Wed Jun  5 2019 Tom Callaway <spot@fedoraproject.org> - 75.0.3770.80-1
- update to 75.0.3770.80
- disable vaapi (via conditional), too broken

* Fri May 31 2019 Tom Callaway <spot@fedoraproject.org> - 74.0.3729.169-1
- update to 74.0.3729.169

* Thu Apr 11 2019 Tom Callaway <spot@fedoraproject.org> - 73.0.3683.103-1
- update to 73.0.3683.103
- add CLONE_VFORK logic to seccomp filter for linux to handle glibc 2.29 change

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> - 73.0.3683.86-2
- remove lang macro from en-US.pak* because Chromium crashes if it is not present
  (bz1692660)

* Fri Mar 22 2019 Tom Callaway <spot@fedoraproject.org> - 73.0.3683.86-1
- update to 73.0.3683.86

* Tue Mar 19 2019 Tom Callaway <spot@fedoraproject.org> - 73.0.3683.75-2
- do not include pyproto/protoc files in package

* Tue Mar 12 2019 Tom Callaway <spot@fedoraproject.org> - 73.0.3683.75-1
- update to 73.0.3683.75

* Sat Mar  9 2019 Tom Callaway <spot@fedoraproject.org> - 72.0.3626.121-1
- update to 72.0.3626.121

* Tue Feb 26 2019 Tom Callaway <spot@fedoraproject.org> - 71.0.3578.98-5
- rebuild for libva api change

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 71.0.3578.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Tom Callaway <spot@fedoraproject.org> - 71.0.3578.98-3
- rebuild with widevine fix

* Tue Jan  8 2019 Tom Callaway <spot@fedoraproject.org> - 71.0.3578.98-2
- drop rsp clobber, which breaks gcc9 (thanks to Jeff Law)

* Fri Dec 14 2018 Tom Callaway <spot@fedoraproject.org> - 71.0.3578.98-1
- update to 71.0.3578.98

* Tue Nov 27 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.110-2
- enable vaapi support (thanks to Akarshan Biswas for doing the hard work here)

* Mon Nov 26 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.110-1
- update to .110

* Wed Nov  7 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.77-4
- fix library requires filtering

* Tue Nov  6 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.77-3
- fix build with harfbuzz2 in rawhide

* Mon Nov  5 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.77-2
- drop jumbo_file_merge_limit to 8 to (hopefully) avoid OOMs on aarch64

* Fri Nov  2 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.77-1
- .77 came out while I was working on this. :/

* Fri Nov  2 2018 Tom Callaway <spot@fedoraproject.org> - 70.0.3538.67-1
- update to 70

* Tue Oct 16 2018 Tom Callaway <spot@fedoraproject.org> - 69.0.3497.100-2
- do not play with fonts on freeworld builds

* Thu Oct  4 2018 Tom Callaway <spot@fedoraproject.org> - 69.0.3497.100-1
- update to 69.0.3497.100

* Wed Sep 12 2018 Tom Callaway <spot@fedoraproject.org> - 69.0.3497.92-1
- update to 69.0.3497.92

* Wed Sep  5 2018 Tom Callaway <spot@fedoraproject.org> - 69.0.3497.81-1
- update to 69.0.3497.81

* Tue Aug 28 2018 Patrik Novotn?? <panovotn@redhat.com> - 68.0.3440.106-4
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sun Aug 19 2018 Tom Callaway <spot@fedoraproject.org> - 68.0.3440.106-3
- fix library filters

* Fri Aug 17 2018 Tom Callaway <spot@fedoraproject.org> - 68.0.3440.106-2
- fix error with defaulting on redeclaration

* Thu Aug  9 2018 Tom Callaway <spot@fedoraproject.org> - 68.0.3440.106-1
- update to 68.0.3440.106

* Wed Aug  8 2018 Tom Callaway <spot@fedoraproject.org> - 68.0.3440.84-1
- update to 68.0.3440.84

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 68.0.3440.75-1
- update to 68.0.3440.75

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 67.0.3396.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.99-1
- update to 67.0.3396.99

* Mon Jun 25 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.87-2
- add "Fedora" to the user agent string

* Tue Jun 19 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.87-1
- update to 67.0.3396.87

* Thu Jun  7 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.79-1
- update to 67.0.3396.79

* Wed Jun  6 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.62-2
- work around bug in RHEL7 python exec

* Wed May 30 2018 Tom Callaway <spot@fedoraproject.org> 67.0.3396.62-1
- 67 releases of chromium on the wall...

* Tue May 29 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.181-3
- also filter out fontconfig on epel7

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.181-2
- fix missing files

* Mon May 21 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.181-1
- update to 66.0.3359.181

* Tue May 15 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.170-2
- only x86_64 i686 have swiftshader
- fix gcc8 alignof issue on i686

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.170-1
- update to 66.0.3359.170
- include swiftshader files

* Tue May  1 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.139-1
- update to 66.0.3359.139

* Wed Apr 18 2018 Tom Callaway <spot@fedoraproject.org> 66.0.3359.117-1
- update to 66.0.3359.117

* Tue Apr 17 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.181-3
- use system fontconfig (except on epel7)

* Wed Apr  4 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.181-2
- add explicit dependency on minizip (bz 1534282)

* Wed Mar 28 2018 Tom Callaway <spot@fedoraproject.org>
- check that there is no system 'google' module, shadowing bundled ones
- conditionalize api keys (on by default)

* Wed Mar 21 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.181-1
- update to 65.0.3325.181

* Mon Mar 19 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.162-3
- use bundled libdrm on epel7

* Fri Mar 16 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.162-2
- disable StartupNotify in chromium-browser.desktop (not in google-chrome desktop file)
  (bz1545241)
- use bundled freetype on epel7

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.162-1
- update to 65.0.3325.162

* Wed Mar  7 2018 Tom Callaway <spot@fedoraproject.org> 65.0.3325.146-1
- update to 65.0.3325.146

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> 64.0.3282.186-1
- update to 64.0.3282.186

* Fri Feb 16 2018 Tom Callaway <spot@fedoraproject.org> 64.0.3282.167-1
- update to 64.0.3282.167
- include workaround for gcc8 bug in gn
- disable unnecessary aarch64 glibc symbol change

* Fri Feb  2 2018 Tom Callaway <spot@fedoraproject.org> 64.0.3282.140-1
- update to 64.0.3282.140

* Thu Feb  1 2018 Tom Callaway <spot@fedoraproject.org> 64.0.3282.119-2
- include user-session binary in chrome-remote-desktop subpackage

* Thu Jan 25 2018 Tom Callaway <spot@fedoraproject.org> 64.0.3282.119-1
- update to 64.0.3282.119

* Fri Dec 15 2017 Tomas Popela <tpopela@redhat.com> 63.0.3239.108-1
- Update to 63.0.3239.108

* Thu Dec  7 2017 Tom Callaway <spot@fedoraproject.org> 63.0.3239.84-1
- update to 63.0.3239.84

* Wed Nov  8 2017 Tom Callaway <spot@fedoraproject.org> 62.0.3202.89-1
- update to 62.0.3202.89

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> 62.0.3202.75-1
- update to 62.0.3202.75
- use devtoolset-7-toolchain to build on epel7

* Tue Oct 24 2017 Tom Callaway <spot@fedoraproject.org> 62.0.3202.62-1.1
- do not attempt std=c++14 on epel7

* Wed Oct 18 2017 Tom Callaway <spot@fedoraproject.org> 62.0.3202.62-1
- update to 62.0.3202.62

* Fri Sep 22 2017 Tom Callaway <spot@fedoraproject.org> 61.0.3163.100-1
- update to 61.0.3163.100
- lots of epel7 specific fixes
- use bundled libpng on epel7

* Wed Sep  6 2017 Tom Callaway <spot@fedoraproject.org> 61.0.3163.79-1
- update to 61.0.3163.79

* Mon Aug 28 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.113-2
- disable aarch64 on rhel7, missing libatomic.so for some reason

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.113-1
- fix ffmpeg clean script to not delete aarch64 file
- update to 60.0.3112.113

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.101-3
- apply aarch64 fixes from Ryan Blakely <rblakely@redhat.com>

* Thu Aug 17 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.101-2
- fix dep issue with chrome-remote-desktop on el7

* Wed Aug 16 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.101-1
- update to 60.0.3112.101
- apply upstream fix for cameras which report zero resolution formats
  (bz1465357)

* Mon Aug 14 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.90-3
- apply more workarounds to coax code to build with epel7 gcc

* Wed Aug  9 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.90-2
- apply post 60 code commit to get code building on epel7

* Fri Aug  4 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.90-1
- update to 60.0.3112.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 59.0.3071.115-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> 60.0.3112.78-1
- update to 60.0.3112.78

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 59.0.3071.115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.115-4
- put common files in -common subpackage
- build headless_shell for -headless subpackage

* Fri Jul 21 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.115-3
- use posttrans to ensure that old libs are gone before trying to make alternative symlinks

* Thu Jul 13 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.115-2
- fix scriptlets

* Wed Jul 12 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.115-1
- 59.0.3071.115
- conditionalize spec so it can be easily used to make -libs-media-freeworld

* Wed Jun 28 2017 Dominik Mierzejewski <dominik@greysector.net> 59.0.3071.109-6
- use alternatives for widevine stub and media libs to allow third-party
  packages to replace them without conflicts

* Mon Jun 26 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.109-5
- fix path in pretrans scriptlet

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.109-4
- copy files into /etc/opt/chrome/native-messaging-hosts instead of making symlinks
  this results in duplicate copies of the same files, but eh. making rpm happy.

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.109-3
- use pretrans scriptlet to remove symlink on /etc/opt/chrome/native-messaging-hosts
  (it is now a directory)

* Thu Jun 22 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.109-2
- fix duplication between chrome-remote-desktop and chromium

* Thu Jun 22 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.109-1
- update to .109
- fix native-messaging-hosts dir to be a true dir instead of a symlink

* Fri Jun 16 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.104-1
- update to .104

* Fri Jun 16 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.86-4
- actually fix mp3 playback support

* Tue Jun 13 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.86-3
- fix filtering

* Mon Jun 12 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.86-2
- pnacl/nacl now needs llvm to build the bootstrap lib

* Mon Jun 12 2017 Tom Callaway <spot@fedoraproject.org> 59.0.3071.86-1
- update to 59.0.3071.86
- include smaller logo files

* Tue May 16 2017 Tom Callaway <spot@fedoraproject.org> 58.0.3029.110-2
- strip provides/requires on libsensors

* Mon May 15 2017 Tom Callaway <spot@fedoraproject.org> 58.0.3029.110-1
- update to 58.0.3029.110

* Mon May  8 2017 Tom Callaway <spot@fedoraproject.org> 58.0.3029.96-1
- update to 58.0.3029.96

* Fri Apr 21 2017 Tom Callaway <spot@fedoraproject.org> 58.0.3029.81-1
- update to 58.0.3029.81

* Thu Mar 30 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.133-1
- update to 57.0.2987.133

* Sun Mar 26 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.110-4
- copy compat stdatomic.h in for RHEL. Re-enable mp3 enablement.
- fix issue in gtk_ui.cc revealed by RHEL build

* Sun Mar 26 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.110-3
- fix mp3 enablement
- disable mp3 enablement on RHEL (compiler too old)

* Tue Mar 21 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.110-2
- fix privlibs

* Mon Mar 20 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.110-1
- update to 57.0.2987.110

* Tue Mar 14 2017 Tom Callaway <spot@fedoraproject.org> 57.0.2987.98-1
- update to 57.0.2987.98

* Sun Mar  5 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-8
- enable mp3 support

* Sat Mar  4 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-7
- fix desktop file to have "new window" and "new private window" actions

* Tue Feb 28 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-6
- fix issue with gcc7 compile in v8 (thanks to Ben Noordhuis)

* Fri Feb 24 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-5
- versioning sync build on rawhide

* Fri Feb 24 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-4.1
- fix issue with unique_ptr move on return with old gcc

* Tue Feb 21 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-4
- disable debuginfo

* Mon Feb 13 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-3
- fix compilation issue
- build third_party/WebKit with -fpermissive
- use bundled jinja everywhere

* Fri Feb 10 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-2
- add BR: gtk3-devel

* Fri Feb 10 2017 Tom Callaway <spot@fedoraproject.org> 56.0.2924.87-1
- update to 56.0.2924.87

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 55.0.2883.87-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Tom Callaway <spot@fedoraproject.org> 55.0.2883.87-1.1
- use bundled jinja2 on RHEL (or Fedora older than 23)
- fix rvalue issue in remoting code

* Tue Dec 13 2016 Tom Callaway <spot@fedoraproject.org> 55.0.2883.87-1
- update to 55.0.2883.87

* Mon Dec 12 2016 Tom Callaway <spot@fedoraproject.org> 55.0.2883.75-1
- update to 55.0.2883.75

* Fri Dec  2 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.100-1
- update to 54.0.2840.100

* Fri Nov  4 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.90-3
- when use_aura is on, chrome/browser needs to link to ui/snapshot

* Wed Nov  2 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.90-2
- export setOpaque in cc_blink

* Wed Nov  2 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.90-1
- update to 54.0.2840.90
- undo ld manipulation for i686, just use -g1 there

* Tue Nov  1 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.71-2
- disable debugging

* Wed Oct 26 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.71-1
- update to 54.0.2840.71

* Wed Oct 26 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.59-2
- fix deps

* Thu Oct 13 2016 Tom Callaway <spot@fedoraproject.org> 54.0.2840.59-1
- 54.0.2840.59
- use bundled opus, libevent

* Fri Sep 30 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.143-1
- 53.0.2785.143

* Tue Sep 20 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.116-1
- 53.0.2785.116

* Wed Sep 14 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.113-1
- 53.0.2785.113

* Thu Sep  8 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.101-1
- 53.0.2785.101
- happy star trek day. live long and prosper.

* Wed Sep  7 2016 Tom Callaway <spot@fedoraproject.org> 53.0.2785.92-1
- add basic framework for gn tooling (disabled because it doesn't work yet)
- update to 53.0.2785.92
- fix HOME environment issue in chrome-remote-desktop service file

* Mon Aug 29 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-11
- conditionalize Requires: u2f-hidraw-policy so that it is only used on Fedora
- use bundled harfbuzz on EL7

* Thu Aug 18 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-10
- disable gtk3 because it breaks lots of things
- re-enable hidpi setting

* Tue Aug 16 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-9
- filter out Requires/Provides for chromium-only libs and plugins

* Tue Aug 16 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-8
- fix path on Requires(post) line for semanage

* Mon Aug 15 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-7
- add Requires(post) items for selinux scriptlets

* Mon Aug 15 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-6
- disable the "hidpi" setting
- unset MADV_FREE if set (should get F25+ working again)

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-5
- do not package libwidevinecdm*.so, they are just empty shells
  instead, to enable widevine, get these files from Google Chrome

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-4
- add "freeworld" conditional for testing netflix/widevine

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-3
- move PepperFlash directory out of the nacl conditional (thanks to churchyard)
- fix widevine (thanks to David V??squez and UnitedRPMS)

* Wed Aug 10 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-2
- include clearkeycdm and widevinecdm files in libs-media

* Mon Aug  8 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.116-1
- update to 52.0.2743.116

* Thu Aug  4 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-13
- change libs split to "libs-media", as that actually works.
- add PepperFlash directory (nothing in it though, sorry)

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-12
- split out libs package beyond ffmpeg, into libs and libs-content
- fix libusbx conditional for el7 to not nuke libusb headers
- disable speech-dispatcher header prefix setting if not fedora (el7)

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-11
- split out chromium-libs-ffmpeg so it can be easily replaced
- conditionalize opus and libusbx for el7

* Wed Aug  3 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-10
- Add ICU Text Codec aliases (from openSUSE via Russian Fedora)
- Use PIE in the Linux sandbox (from openSUSE via Russian Fedora)
- Enable ARM CPU detection for webrtc (from archlinux via Russian Fedora)
- Do not force -m32 in icu compile on ARM (from archlinux via Russian Fedora)
- Enable gtk3 support (via conditional)
- Enable fpic on linux
- Enable hidpi
- Force aura on
- Enable touch_ui
- Add chromedriver subpackage (from Russian Fedora)
- Set default master_preferences location to /etc/chromium
- Add master_preferences file as config file
- Improve chromium-browser.desktop (from Russian Fedora)

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-9
- fix conditional to disable verbose logging output unless beta/dev

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-8
- disable nacl/pnacl for Fedora 23 (and older)

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-7
- fix post scriptlet so that selinux stuff only happens when selinux is enabled

* Thu Jul 28 2016 Richard Hughes <richard@hughsie.com> 52.0.2743.82-6
- Add an AppData file so that Chromium appears in the software center

* Wed Jul 27 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-5
- enable nacl/pnacl (chromium-native_client has landed in Fedora)
- fix chromium-browser.sh to report Fedora build target properly

* Wed Jul 27 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-4
- compile with -fno-delete-null-pointer-checks (fixes v8 crashes, nacl/pnacl)
- turn nacl/pnacl off until chromium-native_client lands in Fedora

* Tue Jul 26 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-3
- turn nacl back on for x86_64

* Thu Jul 21 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-2
- fix cups 2.2 support
- try to enable widevine compatibility (you still need to get the binary .so files from chrome)

* Thu Jul 21 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.82-1
- update to 52.0.2743.82
- handle locales properly
- cleanup spec

* Tue Jul 19 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.75-1
- update to 52.0.2743.75

* Wed Jul 6 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2743.60-1
- bump to 52.0.2743.60, disable nacl for now

* Mon May 9 2016 Tom Callaway <spot@fedoraproject.org> 52.0.2723.2-1
- force to dev to see if it works better on F24+

* Wed May 4 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-6
- apply upstream fix for https://bugs.chromium.org/p/chromium/issues/detail?id=604534

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-5
- use bundled re2 (conditionalize it)

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-4
- disable asan (it never quite built)
- do not preserve re2 bundled tree, causes header/library mismatch

* Mon May 2 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-3
- enable AddressSanize (ASan) for debugging

* Sat Apr 30 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-2
- use bundled icu always. *sigh*

* Fri Apr 29 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.94-1
- update to 50.0.2661.94

* Wed Apr 27 2016 Tom Callaway <spot@fedoraproject.org> 50.0.2661.86-1
- update to 50.0.2661.86

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-4
- protect third_party/woff2

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-3
- add BuildRequires: libffi-devel

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-2
- explicitly disable sysroot

* Thu Mar 17 2016 Tom Callaway <spot@fedoraproject.org> 49.0.2623.87-1
- update to 49.0.2623.87

* Mon Feb 29 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-3
- Happy Leap Day!
- add Requires: u2f-hidraw-policy for u2f token support
- add Requires: xorg-x11-server-Xvfb for chrome-remote-desktop

* Fri Feb 26 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-2
- fix icu BR

* Wed Feb 24 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.116-1
- Update to 48.0.2564.116
- conditionalize icu properly
- fix libusbx handling (bz1270324)

* Wed Feb 17 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.103-2
- fixes for gcc6

* Mon Feb  8 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.103-1
- update to 48.0.2564.103
- use bundled libsrtp (because upstream has coded themselves into an ugly corner)

* Fri Jan 22 2016 Tom Callaway <spot@fedoraproject.org> 48.0.2564.82-1
- update to 48.0.2564.82

* Fri Jan 15 2016 Tom Callaway <spot@fedoraproject.org> 47.0.2526.111-1
- update to 47.0.2526.111

* Thu Jan 07 2016 Tomas Popela <tpopela@redhat.com> 47.0.2526.106-2
- compare hashes when downloading the tarballs
- Google started to include the Debian sysroots in tarballs - remove them while
  processing the tarball
- add a way to not use the system display server for tests instead of Xvfb
- update the depot_tools checkout to get some GN fixes
- use the remove_bundled_libraries script
- update the clean_ffmpeg script to print errors when some files that we are
  processing are missing
- update the clean_ffmpeg script to operate on tarball's toplevel folder
- don't show comments as removed tests in get_linux_tests_names script
- rework the process_ffmpeg_gyp script (also rename it to
  get_free_ffmpeg_source_files) to use the GN files insted of GYP (but we still
  didn't switched to GN build)

* Wed Dec 16 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.106-1
- update to 47.0.2526.106

* Tue Dec 15 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-4
- entirely patch out the broken fd counter from the nacl loader code
  killing it with fire would be better, but then chromium is on fire
  and that somehow makes it worse.

* Mon Dec 14 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-3
- revert nacl fd patch (now we see 6 fds! 6 LIGHTS!)

* Fri Dec 11 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-2
- build everything shared, but when we do shared builds, make -libs subpackage
- make chrome-remote-desktop dep on -libs subpackage in shared builds

* Wed Dec  9 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.80-1
- update to 47.0.2526.80
- only build ffmpeg shared, not any other libs
  this is because if we build the other libs shared, then our
  chrome-remote-desktop build deps on those libs and we do not want that

* Tue Dec  8 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.73-2
- The nacl loader claims it sees 7 fds open ALL THE TIME, and fails
  So, we tell it that it is supposed to see 7.
  I suspect building with shared objects is causing this disconnect.

* Wed Dec  2 2015 Tom Callaway <spot@fedoraproject.org> 47.0.2526.73-1
- update to 47.0.2526.73
- rework chrome-remote-desktop subpackage to work for google-chrome and chromium

* Wed Dec  2 2015 Tomas Popela <tpopela@redhat.com> 47.0.2526.69-1
- Update to 47.0.2526.69

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-4
- still more remote desktop changes

* Mon Nov 30 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-3
- lots of remote desktop cleanups

* Thu Nov 12 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.86-2
- re-enable Requires/BuildRequires for libusbx
- add remote-desktop subpackage

* Wed Nov 11 2015 Tomas Popela <tpopela@redhat.com> 46.0.2490.86-1
- update to 46.0.2490.86
- clean the SPEC file
- add support for policies: https://www.chromium.org/administrators/linux-quick-start
- replace exec_mem_t SELinux label with bin_t - see rhbz#1281437
- refresh scripts that are used for processing the original tarball

* Fri Oct 30 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-5
- tls_edit is a nacl thing. who knew?

* Thu Oct 29 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-4
- more nacl fixups for i686 case

* Thu Oct 29 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-3
- conditionalize nacl/nonacl, disable nacl on i686, build for i686

* Mon Oct 26 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-2
- conditionalize shared bits (enable by default)

* Fri Oct 23 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.80-1
- update to 46.0.2490.80

* Thu Oct 15 2015 Tom Callaway <spot@fedoraproject.org> 46.0.2490.71-1
- update to 46.0.2490.71

* Thu Oct 15 2015 Tom Callaway <spot@fedoraproject.org> 45.0.2454.101-2
- fix icu handling for f21 and older

* Mon Oct  5 2015 Tom Callaway <spot@fedoraproject.org> 45.0.2454.101-1
- update to 45.0.2454.101

* Thu Jun 11 2015 Tom Callaway <spot@fedoraproject.org> 43.0.2357.124-1
- update to 43.0.2357.124

* Tue Jun  2 2015 Tom Callaway <spot@fedoraproject.org> 43.0.2357.81-1
- update to 43.0.2357.81

* Thu Feb 26 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.115-1
- update to 40.0.2214.115

* Thu Feb 19 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.111-1
- update to 40.0.2214.111

* Mon Feb  2 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.94-1
- update to 40.0.2214.94

* Tue Jan 27 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.93-1
- update to 40.0.2214.93

* Sat Jan 24 2015 Tom Callaway <spot@fedoraproject.org> 40.0.2214.91-1
- update to 40.0.2214.91

* Wed Jan 21 2015 Tom Callaway <spot@fedoraproject.org> 39.0.2171.95-3
- use bundled icu on Fedora < 21, we need 5.2

* Tue Jan  6 2015 Tom Callaway <spot@fedoraproject.org> 39.0.2171.95-2
- rebase off Tomas's spec file for Fedora

* Fri Dec 12 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.95-1
- Update to 39.0.2171.95
- Resolves: rhbz#1173448

* Wed Nov 26 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.71-1
- Update to 39.0.2171.71
- Resolves: rhbz#1168128

* Wed Nov 19 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.65-2
- Revert the chrome-sandbox rename to chrome_sandbox
- Resolves: rhbz#1165653

* Wed Nov 19 2014 Tomas Popela <tpopela@redhat.com> 39.0.2171.65-1
- Update to 39.0.2171.65
- Use Red Hat Developer Toolset for compilation
- Set additional SELinux labels
- Add more unit tests
- Resolves: rhbz#1165653

* Fri Nov 14 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.122-1
- Update to 38.0.2125.122
- Resolves: rhbz#1164116

* Wed Oct 29 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.111-1
- Update to 38.0.2125.111
- Resolves: rhbz#1158347

* Fri Oct 24 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.104-2
- Fix the situation when the return key (and keys from numpad) does not work
  in HTML elements with input
- Resolves: rhbz#1153988
- Dynamically determine the presence of the PepperFlash plugin
- Resolves: rhbz#1154118

* Thu Oct 16 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.104-1
- Update to 38.0.2125.104
- Resolves: rhbz#1153012

* Thu Oct 09 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-2
- The boringssl is used for tests, without the possibility of using
  the system openssl instead. Remove the openssl and boringssl sources
  when not building the tests.
- Resolves: rhbz#1004948

* Wed Oct 08 2014 Tomas Popela <tpopela@redhat.com> 38.0.2125.101-1
- Update to 38.0.2125.101
- System openssl is used for tests, otherwise the bundled boringssl is used
- Don't build with clang
- Resolves: rhbz#1004948

* Wed Sep 10 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.120-1
- Update to 37.0.2062.120
- Resolves: rhbz#1004948

* Wed Aug 27 2014 Tomas Popela <tpopela@redhat.com> 37.0.2062.94-1
- Update to 37.0.2062.94
- Include the pdf viewer library

* Wed Aug 13 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.143-1
- Update to 36.0.1985.143
- Use system openssl instead of bundled one
- Resolves: rhbz#1004948

* Thu Jul 17 2014 Tomas Popela <tpopela@redhat.com> 36.0.1985.125-1
- Update to 36.0.1985.125
- Add libexif as BR
- Resolves: rhbz#1004948

* Wed Jun 11 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.153-1
- Update to 35.0.1916.153
- Resolves: rhbz#1004948

* Wed May 21 2014 Tomas Popela <tpopela@redhat.com> 35.0.1916.114-1
- Update to 35.0.1916.114
- Bundle python-argparse
- Resolves: rhbz#1004948

* Wed May 14 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.137-1
- Update to 34.0.1847.137
- Resolves: rhbz#1004948

* Mon May 5 2014 Tomas Popela <tpopela@redhat.com> 34.0.1847.132-1
- Update to 34.0.1847.132
- Bundle depot_tools and switch from make to ninja
- Remove PepperFlash
- Resolves: rhbz#1004948

* Mon Feb 3 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.102-1
- Update to 32.0.1700.102

* Thu Jan 16 2014 Tomas Popela <tpopela@redhat.com> 32.0.1700.77-1
- Update to 32.0.1700.77
- Properly kill Xvfb when tests fails
- Add libdrm as BR
- Add libcap as BR

* Tue Jan 7 2014 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-2
- Minor changes in spec files and scripts
- Add Xvfb as BR for tests
- Add policycoreutils-python as Requires
- Compile unittests and run them in chech phase, but turn them off by default
  as many of them are failing in Brew

* Thu Dec 5 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.67-1
- Update to 31.0.1650.63

* Thu Nov 21 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.57-1
- Update to 31.0.1650.57

* Wed Nov 13 2013 Tomas Popela <tpopela@redhat.com> 31.0.1650.48-1
- Update to 31.0.1650.48
- Minimal supported RHEL6 version is now RHEL 6.5 due to GTK+

* Fri Oct 25 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.114-1
- Update to 30.0.1599.114
- Hide the infobar with warning that this version of OS is not supported
- Polished the chromium-latest.py

* Thu Oct 17 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.101-1
- Update to 30.0.1599.101
- Minor changes in scripts

* Wed Oct 2 2013 Tomas Popela <tpopela@redhat.com> 30.0.1599.66-1
- Update to 30.0.1599.66
- Automated the script for cleaning the proprietary sources from ffmpeg.

* Thu Sep 19 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.76-1
- Update to 29.0.1547.76
- Added script for removing the proprietary sources from ffmpeg. This script is called during cleaning phase of ./chromium-latest --rhel

* Mon Sep 16 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-2
- Compile with Dproprietary_codecs=0 and Dffmpeg_branding=Chromium to disable proprietary codecs (i.e. MP3)

* Mon Sep 9 2013 Tomas Popela <tpopela@redhat.com> 29.0.1547.65-1
- Initial version based on Tom Callaway's <spot@fedoraproject.org> work


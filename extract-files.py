#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/andromeda',
    'hardware/qcom-caf/sm8150',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.hardware.fm@1.0'
        'com.qualcomm.qti.imscmservice@1.0'
        'com.qualcomm.qti.imscmservice@2.0'
        'com.qualcomm.qti.imscmservice@2.1'
        'com.qualcomm.qti.imscmservice@2.2'
        'com.qualcomm.qti.uceservice@2.0'
        'com.qualcomm.qti.uceservice@2.1'
        'com.qualcomm.qti.uceservice@2.2'
        'com.qualcomm.qti.uceservice@2.3'
        'vendor.qti.hardware.data.cne.internal.constants@1.0'
        'vendor.qti.hardware.data.cne.internal.server@1.0'
        'vendor.qti.hardware.data.connection@1.0'
        'vendor.qti.hardware.data.connection@1.1'
        'vendor.qti.hardware.data.dynamicdds@1.0'
        'vendor.qti.hardware.data.iwlan@1.0'
        'vendor.qti.hardware.data.latency@1.0'
        'vendor.qti.hardware.data.qmi@1.0'
        'vendor.qti.hardware.qccsyshal@1.0'
        'vendor.qti.hardware.qccvndhal@1.0'
        'vendor.qti.hardware.slmadapter@1.0'
        'vendor.qti.ims.callcapability@1.0'
        'vendor.qti.ims.callinfo@1.0'
        'vendor.qti.ims.factory@1.0'
        'vendor.qti.ims.factory@1.1'
        'vendor.qti.ims.rcsconfig@1.0'
        'vendor.qti.ims.rcsconfig@1.1'
        'vendor.qti.ims.rcsconfig@2.0'
        'vendor.qti.ims.rcsconfig@2.1'
        'vendor.qti.imsrtpservice@3.0'
        'vendor.qti.latency@2.0'
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    (
    'vendor/etc/media_codecs.xml',
    'vendor/etc/media_codecs_vendor.xml',
    ): blob_fixup()
        .regex_replace('.+media_codecs_(google_audio|google_c2|google_telephony|vendor_audio).+\n', ''),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/lib/soundfx/libdirac.so': blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib/libmmcamera_faceproc.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/lib64/libsnpe_dsp_domains_v2.so': blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
        .clear_symbol_version('remote_register_dma_handle'),
    (
    'vendor/lib64/mediadrm/libwvdrmengine.so',
    'vendor/lib64/libwvhidl.so',
    ): blob_fixup()
        .add_needed('libcrypto_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'andromeda',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

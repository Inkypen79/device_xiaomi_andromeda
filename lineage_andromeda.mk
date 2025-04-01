#
# Copyright (C) 2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_p.mk)

# Inherit some common Lineage stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Gapps
ifeq ($(WITH_GMS), true)
$(call inherit-product,vendor/gapps/arm64/arm64-vendor.mk)
endif

# Inherit from andromeda device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

# Inherit device firmware
$(call inherit-product-if-exists, vendor/xiaomi/andromeda-firmware/firmware.mk)

# Device identifier. This must come after all inclusions.
PRODUCT_NAME := lineage_andromeda
PRODUCT_DEVICE := andromeda
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := Mi MIX 3 5G
PRODUCT_MANUFACTURER := Xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc=andromeda-user 9 PKQ1.190321.001 V12.0.7.0.PEMEUXM release-keys \
    BuildFingerprint=Xiaomi/andromeda_eea/andromeda:9/PKQ1.190321.001/V12.0.7.0.PEMEUXM:user/release-keys \
    DeviceName=andromeda \
    DeviceProduct=andromeda

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

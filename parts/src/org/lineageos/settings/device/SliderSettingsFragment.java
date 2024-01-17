/*
 * Copyright (C) 2018 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.lineageos.settings.device;

import android.content.Context;
import android.os.Bundle;
import android.os.SystemProperties;
import android.view.MenuItem;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.Preference.OnPreferenceChangeListener;
import androidx.preference.PreferenceFragmentCompat;
import androidx.preference.SwitchPreferenceCompat;

import org.lineageos.settings.R;
import org.lineageos.settings.utils.FileUtils;

public class SliderSettingsFragment extends PreferenceFragmentCompat implements
        OnPreferenceChangeListener {

    private ListPreference mSoundPreference;
    private SwitchPreferenceCompat mSliderPreference;

    private static final String SLIDER_DISABLE_KEY = "slider_disable";
    private static final String SLIDER_DISABLE_PROPERTY = "persist.slider.disable";
    private static final String SLIDER_SOUND_KEY = "slider_sound";
    private static final String SLIDER_SOUND_PROPERTY = "persist.slider.sound";

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.slider_settings, rootKey);
        mSliderPreference = (SwitchPreferenceCompat) findPreference(SLIDER_DISABLE_KEY);
        mSliderPreference.setEnabled(true);
        mSliderPreference.setOnPreferenceChangeListener(this);

        mSoundPreference = (ListPreference) findPreference(SLIDER_SOUND_KEY);
        mSoundPreference.setOnPreferenceChangeListener(this);

        int sliderDisabled = SystemProperties.getInt(SLIDER_DISABLE_PROPERTY, 0);
        if (sliderDisabled == 1) {
            mSoundPreference.setEnabled(false);
        } else {
            mSoundPreference.setEnabled(true);
        }
    }

    @Override
    public boolean onPreferenceChange(Preference preference, Object newValue) {
        switch (preference.getKey()) {
            case SLIDER_DISABLE_KEY:
                int slider = SystemProperties.getInt(SLIDER_DISABLE_PROPERTY, 0);
                if (slider == 1) {
                    SystemProperties.set(SLIDER_DISABLE_PROPERTY, "0");
                    mSoundPreference.setEnabled(true);
                } else {
                    SystemProperties.set(SLIDER_DISABLE_PROPERTY, "1");
                    mSoundPreference.setEnabled(false);
                }
                return true;
            case SLIDER_SOUND_KEY:
                SystemProperties.set(SLIDER_SOUND_PROPERTY, (String.valueOf(newValue)));
                return true;
            default: return false;
        }
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == android.R.id.home) {
            getActivity().onBackPressed();
            return true;
        }
        return false;
    }

}

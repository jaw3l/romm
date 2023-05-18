<script setup>
import { ref, inject } from "vue"
import { useTheme } from "vuetify"
import { useDiscStreaming, getDiscStreaming } from '@/stores/discStreaming.js'

// Props
const tab = ref('ui')
const theme = useTheme()
const discStreaming = (getDiscStreaming() == true) ? ref(true) : ref(false)
const darkMode = (localStorage.getItem('theme') == 'rommDark') ? ref(true) : ref(false)
const ROMM_VERSION = import.meta.env.VITE_ROMM_VERSION

// Event listeners bus
const emitter = inject('emitter')

// Functions
function toggleTheme() {
    theme.global.name.value = darkMode.value ? "rommDark" : "rommLight"
    darkMode.value ? localStorage.setItem('theme', 'rommDark') : localStorage.setItem('theme', 'rommLight')
}

function togglePPSSPPDiscStreaming() {
    useDiscStreaming(emitter)
    console.log("[togglePPSSPPDiscStreaming] Local Store Disc Streaming:", getDiscStreaming());
}
</script>
<template>
    <v-tabs v-model="tab" slider-color="rommAccent1" class="bg-primary">
        <v-tab value="general" rounded="0">General</v-tab>
        <v-tab value="ui" rounded="0">User Interface</v-tab>
    </v-tabs>
    <v-window v-model="tab">
        <v-window-item value="general" class="pa-2">
            <v-row no-gutters>
                <v-switch v-model="discStreaming"
                    @change="togglePPSSPPDiscStreaming()"
                    label="PPSSPP Remote Disc Streaming"
                    class="ml-2"
                    prepend-icon="mdi-gamepad"
                    hide-details
                    inset
                />
            </v-row>
            <v-row no-gutters>
                <v-btn
                    color="rommAccent1"
                    class="ml-2"
                    @click="$router.push('/disc-streaming')"
                    >PSP ROMs</v-btn>
            </v-row>
        </v-window-item>
        <v-window-item value="ui" class="pa-2">
            <v-row no-gutters>
                <v-switch
                    @change="toggleTheme()"
                    v-model="darkMode"
                    prepend-icon="mdi-theme-light-dark"
                    hide-details
                    inset/>
            </v-row>
        </v-window-item>
    </v-window>

    <v-bottom-navigation :elevation="0" height="36" class="text-caption">
        <v-row class="align-center justify-center" no-gutters>
            <span class="text-rommAccent1">RomM</span><span class="ml-1">v{{ ROMM_VERSION }}</span>
        </v-row>
    </v-bottom-navigation>

</template>

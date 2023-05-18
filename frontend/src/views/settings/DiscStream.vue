<script setup>
import axios from 'axios';
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { getDiscStreaming } from '@/stores/discStreaming.js';

const roms = ref([]);
const discStreaming = ref(getDiscStreaming());

onMounted(() => {
    window.addEventListener('storage', handleStorageChange);
})

onBeforeUnmount(() => {
    window.removeEventListener('storage', handleStorageChange);
})

function handleStorageChange(event) {
    if (event.key === 'discStreaming') {
        discStreaming.value = getDiscStreaming();
    }
}

async function fetchRoms() {
    const response = await axios.get('/api/platforms/psp/roms');
    for (const rom of response.data.data) {
        const isoFullPath = "/assets/romm/library/" + rom.file_path + "/" + rom.file_name;
        const iso = await fetch(isoFullPath);
        rom.iso_url = iso.url;
        rom.iso_full_path = isoFullPath

    }
    roms.value = response.data.data;
}

if (discStreaming.value) {
    fetchRoms();
}
</script>
<template>
    <v-container>
        <h1 class="mb-4">PSP ROMs</h1>
        <v-card v-if="discStreaming">
            <v-card-text>
                <v-list dense>
                    <v-list-item v-for="rom in roms" :key="rom.id">
                        <a v-bind:href="rom.iso_full_path">{{ "/assets/romm/library/" + rom.file_path + "/" + rom.file_name }}</a>
                        <br>
                        <a v-bind:href="rom.iso_url">{{ rom.iso_url }}</a>
                    </v-list-item>
                </v-list>
            </v-card-text>
        </v-card>
        <v-card v-else>
            <v-card-text>
                <p>Please enable Disc Streaming to view PSP roms.</p>
            </v-card-text>
        </v-card>
    </v-container>
</template>
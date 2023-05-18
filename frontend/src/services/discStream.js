import axios from 'axios';
import { fetchPlatforms } from "@/services/api.js";
import { getDiscStreaming } from "@/stores/discStreaming.js";

export const startDiscStreaming = (emitter) => {
  console.log("[startDiscStreaming] Current Status:", getDiscStreaming());

  // Print out the platforms using fetchPlatforms
  fetchPlatforms()
    .then((platforms) => {
      checkForPlatform(platforms, emitter);
    })
    .catch((error) => {
      console.error("[discStreaming] Error fetching platforms:", error);
    });
};

export const stopDiscStreaming = (emitter) => {};

// Check if the "PSP" platform is in the platforms array
function checkForPlatform(platforms, emitter) {
  const slugs = platforms.data.data.map((p) => p.slug);
  let foundPsp = false;
  for (let i = 0; i < slugs.length; i++) {
    const slug = slugs[i];
    if (slug === "psp") {
      foundPsp = true;
      break;
    }
  }
  if (!foundPsp) {
    emitter.emit("snackbarScan", {
      msg: "PSP platform not found!",
      icon: "mdi-alert",
      color: "red",
    });
    console.log("[startDiscStreaming] Not Found");
    throw new Error("PSP platform not found!");
  }
}

// Get the roms using axios and return the info of roms
function getRoms() {}
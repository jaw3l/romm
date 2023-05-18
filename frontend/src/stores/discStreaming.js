import { ref } from "vue";
import {
  startDiscStreaming,
  stopDiscStreaming,
} from "@/services/discStream.js";

const STORAGE_KEY = "discStreaming";

export const getDiscStreaming = () => {
  const value = localStorage.getItem(STORAGE_KEY);
  return value !== null ? JSON.parse(value) : false;
};

export const useDiscStreaming = (emitter) => {
  const discStreaming = ref(getDiscStreaming());
  if (discStreaming.value === true) {
    stopDiscStreaming(emitter);
    localStorage.setItem(STORAGE_KEY, false);
  } else {
    startDiscStreaming(emitter);
    localStorage.setItem(STORAGE_KEY, true);
  }
};

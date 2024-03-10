import Vue from "vue";
import App from "./App.vue";
import axios from "axios";

// Set up axios as a global property
Vue.prototype.$http = axios.create({
  baseURL: "http://127.0.0.1:8000", // backend url
});

new Vue({
  el: "#app",
  render: (h) => h(App),
});

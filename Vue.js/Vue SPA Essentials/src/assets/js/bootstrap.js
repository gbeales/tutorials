import Vue from "vue";
import VueRouter from "vue-router";
import axios from "axios";

window.Vue = Vue;
window.Vue.use(VueRouter);

window.axios = axios;

axios.defaults.headers.common = {
  "X-Requested-With": "XMLHttpRequest"
};

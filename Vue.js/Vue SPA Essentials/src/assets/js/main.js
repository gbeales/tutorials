import "./bootstrap.js";
import router from "./routes";

window.Vue.config.productionTip = false;

new window.Vue({
  el: "#app",

  router: router
});

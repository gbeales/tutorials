import VueRouter from "vue-router";

// import Home from "./views/Home.vue";
import About from "./views/About.vue";
import Contact from "./views/Contact.vue";
import Login from "./views/Login.vue";

let routes = [
  {
    path: "/",
    component: require("./views/Home.vue").default
  },
  {
    path: "/about",
    component: About
  },
  {
    path: "/contact",
    component: Contact
  },
  {
    path: "/login",
    component: Login
  }
];

export default new VueRouter({
  routes,
  linkActiveClass: "is-active"
});

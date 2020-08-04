import Vue from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import VueCookies from 'vue-cookies';
import VueBreadcrumbs from 'vue-2-breadcrumbs'

Vue.use(VueCookies);
Vue.use(VueBreadcrumbs)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

import Vue from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import api from './api';

import 'semantic-ui-css/semantic.min.css';
import SuiVue from 'semantic-ui-vue';
import AsyncComputed from 'vue-async-computed';
import VueAxios from 'vue-axios';

Vue.use(SuiVue);
Vue.use(AsyncComputed)
Vue.use(VueAxios, api);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');

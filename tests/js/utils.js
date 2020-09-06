import VueRouter from 'vue-router';
import Vuex, { Store } from 'vuex';
import SuiVue from 'semantic-ui-vue';

import { createLocalVue } from '@vue/test-utils';

export const localVue = createLocalVue();
localVue.use(VueRouter);
localVue.use(Vuex);
localVue.use(SuiVue);

export const getStore = (module, storeOpts = {}) =>
  new Store({ modules: { [module]: storeOpts } });

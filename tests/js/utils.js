import VueRouter from 'vue-router';
import Vuex, { Store } from 'vuex';

import { createLocalVue } from '@vue/test-utils';

export const localVue = createLocalVue();
localVue.use(VueRouter);
localVue.use(Vuex);

export const getStore = (module, storeOpts = {}) =>
  new Store({ modules: { [module]: { namespaced: true, ...storeOpts } } });

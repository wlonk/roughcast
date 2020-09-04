import { shallowMount } from '@vue/test-utils';
import BreadCrumbs from '@/components/BreadCrumbs.vue';
import { getStore, localVue } from '../utils';
import VueRouter from 'vue-router';

const router = new VueRouter();

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        dryUser: () => () => undefined,
        dryTeam: () => () => undefined,
        dryGame: () => () => undefined,
        dryVersion: () => () => undefined,
      },
    });
    const wrapper = shallowMount(BreadCrumbs, { store, localVue, router });
    expect(wrapper.find('.ui.breadcrumb').exists()).toBe(true);
  });
});

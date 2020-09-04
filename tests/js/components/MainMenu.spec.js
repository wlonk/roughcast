import { shallowMount } from '@vue/test-utils';
import MainMenu from '@/components/MainMenu.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        currentUser: () => null,
      },
    });
    const wrapper = shallowMount(MainMenu, { store, localVue });
    expect(wrapper.find('#page-header').exists()).toBe(true);
  });
});

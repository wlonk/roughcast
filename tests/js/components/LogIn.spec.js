import { shallowMount } from '@vue/test-utils';
import LogIn from '@/components/LogIn.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        loginErrors: () => ({}),
      },
    });
    const wrapper = shallowMount(LogIn, { store, localVue });
    expect(wrapper.find('form').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import UserControlMenu from '@/components/UserControlMenu.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        currentUser: () => ({
          username: 'user',
        }),
      },
    });
    const wrapper = shallowMount(UserControlMenu, { store, localVue });
    expect(wrapper.find('.dropdown-menu').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import UserPanel from '@/components/UserPanel.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        currentUser: () => ({
          avatar: '',
          username: 'user',
          first_name: 'Alex Rodriguez',
        }),
      },
    });
    const wrapper = shallowMount(UserPanel, { store, localVue });
    expect(wrapper.find('.user-panel').exists()).toBe(true);
  });
});

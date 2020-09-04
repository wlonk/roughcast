import { shallowMount } from '@vue/test-utils';
import PublicProfileBlock from '@/components/PublicProfileBlock.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        currentUser: () => ({
          avatar: '',
          bio: '',
          first_name: 'Alex Rodriguez',
        }),
      },
    });
    const wrapper = shallowMount(PublicProfileBlock, { store, localVue });
    expect(wrapper.find('#public').exists()).toBe(true);
  });
});

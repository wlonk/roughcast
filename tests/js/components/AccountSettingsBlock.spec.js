import { shallowMount } from '@vue/test-utils';
import AccountSettingsBlock from '@/components/AccountSettingsBlock.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        currentUser: () => null,
      },
    });
    const wrapper = shallowMount(AccountSettingsBlock, { store, localVue });
    expect(wrapper.find('#account').exists()).toBe(true);
  });
});

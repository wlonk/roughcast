import { shallowMount } from '@vue/test-utils';
import AccountSettingsInfo from '@/components/AccountSettingsInfo.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User');
    const wrapper = shallowMount(AccountSettingsInfo, { store, localVue });
    expect(wrapper.find('.info-block').exists()).toBe(true);
  });
});

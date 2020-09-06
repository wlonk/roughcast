import { shallowMount } from '@vue/test-utils';
import AccountSettingsInfo from '@/components/AccountSettingsInfo.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(AccountSettingsInfo);
    expect(wrapper.find('.info-block').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import AccountSettingsBlock from '@/components/AccountSettingsBlock.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(AccountSettingsBlock);
    expect(
      wrapper.find('#account').exists(),
    ).toBe(true);
  });
});

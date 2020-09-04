import { shallowMount } from '@vue/test-utils';
import LogOut from '@/components/LogOut.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(LogOut);
    expect(
      wrapper.find('form').exists(),
    ).toBe(true);
  });
});

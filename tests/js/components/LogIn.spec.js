import { shallowMount } from '@vue/test-utils';
import LogIn from '@/components/LogIn.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(LogIn);
    expect(
      wrapper.find('form').exists(),
    ).toBe(true);
  });
});

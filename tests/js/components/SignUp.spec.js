import { shallowMount } from '@vue/test-utils';
import SignUp from '@/components/SignUp.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(SignUp);
    expect(
      wrapper.find('.page-form').exists(),
    ).toBe(true);
  });
});

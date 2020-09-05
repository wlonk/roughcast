import { shallowMount } from '@vue/test-utils';
import ResetPasswordForm from '@/forms/ResetPasswordForm.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(ResetPasswordForm);
    expect(wrapper.find('.page-form').exists()).toBe(true);
  });
});

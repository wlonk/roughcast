import { shallowMount } from '@vue/test-utils';
import ChangePasswordForm from '@/components/ChangePasswordForm.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(ChangePasswordForm);
    expect(wrapper.find('#password-change').exists()).toBe(true);
  });
});

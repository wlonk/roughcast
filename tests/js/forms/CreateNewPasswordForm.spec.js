import { shallowMount } from '@vue/test-utils';
import CreateNewPasswordForm from '@/forms/CreateNewPasswordForm.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(CreateNewPasswordForm);
    expect(wrapper.find('.page-form').exists()).toBe(true);
  });
});

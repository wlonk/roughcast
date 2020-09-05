import { shallowMount } from '@vue/test-utils';
import EditAccountSettingsForm from '@/forms/EditAccountSettingsForm.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(EditAccountSettingsForm);
    expect(wrapper.find('.page-form').exists()).toBe(true);
  });
});

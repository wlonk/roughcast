import { shallowMount } from '@vue/test-utils';
import EditPublicProfileForm from '@/components/EditPublicProfileForm.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(EditPublicProfileForm);
    expect(
      wrapper.find('.page-form.public').exists(),
    ).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import VersionSection from '@/components/VersionSection.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(VersionSection);
    expect(
      wrapper.find('.version-section').exists(),
    ).toBe(true);
  });
});

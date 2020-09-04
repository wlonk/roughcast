import { shallowMount } from '@vue/test-utils';
import VersionCard from '@/components/VersionCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(VersionCard);
    expect(
      wrapper.find('.version-card').exists(),
    ).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import VersionList from '@/components/VersionSection.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(VersionList);
    expect(
      wrapper.find('.version-list').exists(),
    ).toBe(true);
  });
});

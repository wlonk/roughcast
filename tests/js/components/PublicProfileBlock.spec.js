import { shallowMount } from '@vue/test-utils';
import PublicProfileBlock from '@/components/PublicProfileBlock.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(PublicProfileBlock);
    expect(
      wrapper.find('#public').exists(),
    ).toBe(true);
  });
});

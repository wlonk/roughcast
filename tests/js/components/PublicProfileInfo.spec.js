import { shallowMount } from '@vue/test-utils';
import PublicProfileInfo from '@/components/PublicProfileInfo.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(PublicProfileInfo);
    expect(
      wrapper.find('.info-block.public').exists(),
    ).toBe(true);
  });
});

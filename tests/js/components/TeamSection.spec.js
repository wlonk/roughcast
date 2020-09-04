import { shallowMount } from '@vue/test-utils';
import TeamSection from '@/components/TeamSection.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(TeamSection);
    expect(
      wrapper.find('.ui.grid').exists(),
    ).toBe(true);
  });
});

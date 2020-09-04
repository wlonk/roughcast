import { shallowMount } from '@vue/test-utils';
import TeamCard from '@/components/TeamCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(TeamCard);
    expect(
      wrapper.find('.ui.card').exists(),
    ).toBe(true);
  });
});

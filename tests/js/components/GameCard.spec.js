import { shallowMount } from '@vue/test-utils';
import GameCard from '@/components/GameCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(GameCard);
    expect(
      wrapper.find('.game-card').exists(),
    ).toBe(true);
  });
});

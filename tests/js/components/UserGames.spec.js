import { shallowMount } from '@vue/test-utils';
import UserGames from '@/components/UserGames.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(UserGames);
    expect(
      wrapper.find('.user-game-block').exists(),
    ).toBe(true);
  });
});

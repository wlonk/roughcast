import { shallowMount } from '@vue/test-utils';
import UserGames from '@/components/UserGames.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(UserGames, {
      propsData: {
        group: { name: 'Team' },
        games: [],
      },
    });
    expect(wrapper.find('.user-game-block').exists()).toBe(true);
  });
});

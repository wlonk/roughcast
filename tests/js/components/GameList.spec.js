import { shallowMount } from '@vue/test-utils';
import GameList from '@/components/GameList.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(GameList);
    expect(
      wrapper.find('.game-list').exists(),
    ).toBe(true);
  });
});

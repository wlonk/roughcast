import { shallowMount } from '@vue/test-utils';
import GameList from '@/components/GameList.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        hydratedGame: () => () => undefined,
      },
    });
    const wrapper = shallowMount(GameList, {
      store,
      localVue,
      propsData: {
        team: {
          slug: 'team',
        },
        games: [],
        userCanAddGames: true,
      },
    });
    expect(wrapper.find('.content-list').exists()).toBe(true);
  });
});

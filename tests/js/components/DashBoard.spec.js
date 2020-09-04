import { shallowMount } from '@vue/test-utils';
import DashBoard from '@/components/DashBoard.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        listGames: () => [],
        hydratedGame: () => () => undefined,
        listTeams: () => [],
      },
    });
    const wrapper = shallowMount(DashBoard, { store, localVue });
    expect(wrapper.find('#dashboard').exists()).toBe(true);
  });
});

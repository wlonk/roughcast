import { shallowMount } from '@vue/test-utils';
import TeamTabs from '@/components/TeamTabs.vue';

describe('App.vue', () => {
  it('renders', () => {
    const allGames = { name: 'All games', slug: '*' };
    const wrapper = shallowMount(TeamTabs, {
      propsData: {
        teams: [],
        chosen: allGames,
      },
    });
    expect(wrapper.find('.team-tabs').exists()).toBe(true);
  });
});

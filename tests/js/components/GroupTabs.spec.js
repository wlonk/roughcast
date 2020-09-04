import { shallowMount } from '@vue/test-utils';
import GroupTabs from '@/components/GroupTabs.vue';

describe('App.vue', () => {
  it('renders', () => {
    const allGames = { name: 'All games', slug: '*' };
    const wrapper = shallowMount(GroupTabs, {
      propsData: {
        groups: [],
        chosen: allGames,
      },
    });
    expect(wrapper.find('.group-tabs').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import GameCard from '@/components/GameCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(GameCard, {
      propsData: {
        avatar: '',
        id: 'id',
        name: 'Game',
        slug: 'game',
        description: '',
        team: {
          name: 'Team',
          slug: 'team',
        },
        latest_version: {
          name: 'v1',
        },
        permissions: {
          'this:edit': true,
        },
        likes: 0,
        comments: 0,
      },
    });
    expect(wrapper.find('.game-card').exists()).toBe(true);
  });
});

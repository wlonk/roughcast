import { shallowMount } from '@vue/test-utils';
import GameSection from '@/components/GameSection.vue';

describe('GameSection', () => {
  it('renders', () => {
    const wrapper = shallowMount(GameSection, {
      propsData: {
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
          slug: 'v1',
        },
        permissions: {
          'this:delete': true,
          'this:edit': true,
        },
      },
    });
    expect(wrapper.find('.game-section').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import TeamCard from '@/components/TeamCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(TeamCard, {
      propsData: {
        name: 'Test Team',
      },
    });
    expect(wrapper.find('.team-card').exists()).toBe(true);
  });
});

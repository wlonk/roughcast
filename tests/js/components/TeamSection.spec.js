import { shallowMount } from '@vue/test-utils';
import TeamSection from '@/components/TeamSection.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(TeamSection, {
      propsData: {
        id: 'id',
        name: 'Team',
        permissions: {
          'this:edit': true,
        },
        slug: 'team',
        url: '',
        description: '',
        user_is_owner: true,
      },
    });
    expect(wrapper.find('.ui.grid').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import TeamList from '@/components/TeamList.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(TeamList);
    expect(wrapper.find('.content-list').exists()).toBe(true);
  });
});

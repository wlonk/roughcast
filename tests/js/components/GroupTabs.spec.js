import { shallowMount } from '@vue/test-utils';
import GroupTabs from '@/components/GroupTabs.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(GroupTabs);
    expect(
      wrapper.find('.group-tabs').exists(),
    ).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import ScrollingEditMenu from '@/components/ScrollingEditMenu.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(ScrollingEditMenu);
    expect(wrapper.find('.scrolling-menu').exists()).toBe(true);
  });
});

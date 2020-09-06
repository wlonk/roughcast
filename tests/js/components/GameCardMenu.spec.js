import { shallowMount } from '@vue/test-utils';
import GameCardMenu from '@/components/GameCardMenu.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(GameCardMenu);
    expect(wrapper.find('.dropdown-menu').exists()).toBe(true);
  });
});

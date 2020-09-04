import { shallowMount } from '@vue/test-utils';
import MainMenu from '@/components/MainMenu.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(MainMenu);
    expect(
      wrapper.find('#page-header').exists(),
    ).toBe(true);
  });
});

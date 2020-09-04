import { shallowMount } from '@vue/test-utils';
import UserControlMenu from '@/components/UserControlMenu.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(UserControlMenu);
    expect(
      wrapper.find('.dropdown-menu').exists(),
    ).toBe(true);
  });
});

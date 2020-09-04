import { shallowMount } from '@vue/test-utils';
import DashBoard from '@/components/DashBoard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(DashBoard);
    expect(
      wrapper.find('#dashboard').exists(),
    ).toBe(true);
  });
});

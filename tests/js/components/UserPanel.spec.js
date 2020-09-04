import { shallowMount } from '@vue/test-utils';
import UserPanel from '@/components/UserPanel.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(UserPanel);
    expect(
      wrapper.find('.user-panel').exists(),
    ).toBe(true);
  });
});

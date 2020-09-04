import { shallowMount } from '@vue/test-utils';
import NotificationPreferences from '@/components/NotificationPreferences.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(NotificationPreferences);
    expect(
      wrapper.find('#notifications').exists(),
    ).toBe(true);
  });
});

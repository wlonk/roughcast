import { shallowMount } from '@vue/test-utils';
import NotificationTypeCard from '@/components/NotificationTypeCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(NotificationTypeCard);
    expect(
      wrapper.find('.notification-type-card').exists(),
    ).toBe(true);
  });
});

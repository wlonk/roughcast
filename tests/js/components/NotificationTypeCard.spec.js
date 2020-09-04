import { shallowMount } from '@vue/test-utils';
import NotificationTypeCard from '@/components/NotificationTypeCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(NotificationTypeCard, {
      propsData: {
        name: 'New Comments',
        apiName: 'comments',
        order: 0,
        notifs: {
          in_app: true,
          instant_email: true,
          digest_email: false,
        },
      },
    });
    expect(wrapper.find('.notification-type-card').exists()).toBe(true);
  });
});

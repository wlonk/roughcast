import { shallowMount } from '@vue/test-utils';
import NotificationList from '@/components/NotificationList.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('Notification', {
      getters: {
        allNotifications: () => [
          {
            id: 'abc123',
            notification_type: 'comment',
            seen_at: null,
            path: '/t/test',
            subject: 'Test notification',
          },
        ],
      },
    });
    const wrapper = shallowMount(NotificationList, { store, localVue });
    expect(wrapper.find('.dropdown-menu').exists()).toBe(true);
  });
});

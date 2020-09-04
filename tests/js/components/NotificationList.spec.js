import { shallowMount } from '@vue/test-utils';
import NotificationList from '@/components/NotificationList.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(NotificationList);
    expect(wrapper.find('.dropdown-menu').exists()).toBe(true);
  });
});

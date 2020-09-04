import { shallowMount } from '@vue/test-utils';
import NoPageNotification from '@/components/NoPageNotification.vue';

describe('NoPageNotification', () => {
  it('renders', () => {
    const wrapper = shallowMount(NoPageNotification);
    expect(wrapper.find('.welcome-block').exists()).toBe(true);
  });
});

import { shallowMount } from '@vue/test-utils';
import UserCard from '@/components/UserCard.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(UserCard);
    expect(wrapper.find('.user-profile-card').exists()).toBe(true);
  });
});

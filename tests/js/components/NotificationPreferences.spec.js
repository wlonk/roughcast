import { shallowMount } from '@vue/test-utils';
import NotificationPreferences from '@/components/NotificationPreferences.vue';
import { getStore, localVue } from '../utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {
      getters: {
        profile: () => ({
          notif_comments: {
            in_app: true,
            instant_email: true,
            digest_email: false,
          },
          notif_mentions: {
            in_app: true,
            instant_email: true,
            digest_email: false,
          },
          notif_games: {
            in_app: true,
            instant_email: true,
            digest_email: false,
          },
          notif_versions: {
            in_app: true,
            instant_email: true,
            digest_email: false,
          },
        }),
      },
    });
    const wrapper = shallowMount(NotificationPreferences, { store, localVue });
    expect(wrapper.find('#notifications').exists()).toBe(true);
  });
});

import NoPageNotification from '@/components/NoPageNotification.vue';
import { getStore, localVue } from '../utils';

  it('renders') => {
    const store = getStore('User', {});
    const wrapper = shallowMount(NoPageNotification, { localVue, store });
    expect(
      wrapper.find('#app').exists(),
    ).toBe(true);
  });
});

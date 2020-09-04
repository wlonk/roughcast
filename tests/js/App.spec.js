import { shallowMount } from '@vue/test-utils';
import App from '@/App.vue';
import { getStore, localVue } from './utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {});
    const wrapper = shallowMount(App, { localVue, store });
    expect(
      wrapper.find('#app').exists(),
    ).toBe(true);
  });
});

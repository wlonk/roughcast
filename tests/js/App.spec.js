import { shallowMount } from '@vue/test-utils';
import App from '@/App.vue';
import { getStore, localVue } from './utils';

describe('App.vue', () => {
  it('renders', () => {
    const store = getStore('User', {});
    const wrapper = shallowMount(App, { localVue, store });
    expect(
      wrapper.find('.ui.raised.very.padded.text.container.segment').exists(),
    ).toBe(true);
  });
});

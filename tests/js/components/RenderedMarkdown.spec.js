import { shallowMount } from '@vue/test-utils';
import RenderedMarkdown from '@/components/RenderedMarkdown.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(RenderedMarkdown);
    expect(
      wrapper.find('.rendered').exists(),
    ).toBe(true);
  });
});

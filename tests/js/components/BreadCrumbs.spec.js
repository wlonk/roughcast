import { shallowMount } from '@vue/test-utils';
import BreadCrumbs from '@/components/BreadCrumbs.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(BreadCrumbs);
    expect(
      wrapper.find('.ui.breadcrumb').exists(),
    ).toBe(true);
  });
});

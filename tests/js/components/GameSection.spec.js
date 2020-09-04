import GameSection from '@/components/GameSection.vue';
import { getStore, localVue } from '../utils';

  it('renders') => {
    const store = getStore('User', {});
    const wrapper = shallowMount(GameSection, { localVue, store });
    expect(
      wrapper.find('.game-section').exists(),
    ).toBe(true);
  });
});

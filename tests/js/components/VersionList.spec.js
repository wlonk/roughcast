import { shallowMount } from '@vue/test-utils';
import VersionList from '@/components/VersionList.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(VersionList, {
      propsData: {
        team: 'team',
        game: 'game',
        versions: [],
        userCanAddVersions: true,
        defaultVisibleTo: [],
      },
    });
    expect(wrapper.find('.versions-list').exists()).toBe(true);
  });
});

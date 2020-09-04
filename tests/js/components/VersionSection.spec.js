import { shallowMount } from '@vue/test-utils';
import VersionSection from '@/components/VersionSection.vue';

describe('App.vue', () => {
  it('renders', () => {
    const wrapper = shallowMount(VersionSection, {
      propsData: {
        id: 'id',
        name: 'version',
        team: 'team',
        gameSlug: 'game',
        slug: 'v1',
        changelog: '',
        archive_link: '',
        permissions: {
          'this:delete': true,
          'this:edit': true,
        },
        attachedFiles: [],
      },
    });
    expect(wrapper.find('.version-section').exists()).toBe(true);
  });
});

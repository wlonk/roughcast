<template>
  <div>
    <a :href="archive_link">
      <i class="right floated file archive outline icon"></i>
    </a>
    <router-link :to="`/p/${publisher}/${game}/${slug}`">
      {{ name }}
    </router-link>
    <span>{{ changelog_short }}</span>
  </div>
</template>

<script>
import _ from 'lodash';

import { mapState } from 'vuex';

export default {
  name: 'VersionCard',
  props: {
    id: String,
    name: String,
    version: String,
    publisher: String,
    changelog: String,
    changelog_short: String,
    game: String,
    slug: String,
    archive_link: String,
    permissions: Object,
  },
  computed: {
    ...mapState(['AttachedFile']),
    attachedFiles() {
      return _.filter(this.AttachedFile.all, af => af.version_id === this.id);
    },
  },
};
</script>

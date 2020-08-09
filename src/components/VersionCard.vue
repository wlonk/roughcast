<template>
  <div>
    <h4>
      <a :href="archive_link">
        <i class="right floated file archive outline icon"></i>
      </a>
      <router-link :to="`/p/${publisher}/${game}/${slug}`">
        {{ name }}
      </router-link>
    </h4>
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

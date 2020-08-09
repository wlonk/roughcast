<template>
  <div>
    <h4>
      <router-link :to="`/p/${publisher}/${game}/${slug}`">
        {{ name }}
      </router-link>
      <a :href="archive_link">
        <i class="right floated file archive outline icon"></i>
      </a>
      <ul v-if="isDetail">
        <li v-for="(file, i) in attachedFiles" :key="i">
          <a :href="file.attached_file"> <i class="file pdf outline icon"></i> {{ file.name }} </a>
        </li>
      </ul>
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
    isDetail: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    ...mapState(['AttachedFile']),
    attachedFiles() {
      return _.filter(this.AttachedFile.all, af => af.version_id === this.id);
    },
  },
};
</script>

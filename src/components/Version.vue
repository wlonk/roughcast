<template>
  <div>
    <h4>
      <router-link :to="`/p/${publisher}/${game}/${slug}`">
        {{ name }}
      </router-link>
      <a :href="archive_link">
        <IconArchive />
      </a>
      <ul v-if="isDetail">
        <li v-for="(file, i) in attachedFiles" :key="i">
          <a :href="file.attached_file"> <IconPdf /> {{ file.name }} </a>
        </li>
      </ul>
    </h4>
  </div>
</template>

<script>
import _ from 'lodash';
import IconArchive from '@/icons/Archive';
import IconPdf from '@/icons/Pdf';

import { mapState } from 'vuex';

export default {
  name: 'Version',
  props: {
    id: String,
    name: String,
    version: String,
    publisher: String,
    game: String,
    slug: String,
    archive_link: String,
    isDetail: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    IconArchive,
    IconPdf,
  },
  computed: {
    ...mapState(['AttachedFile']),
    attachedFiles() {
      return _.filter(this.AttachedFile.all, af => af.version === this.slug);
    },
  },
};
</script>

<style scoped>
ul {
  padding-left: 0;
  list-style: none;
}
</style>

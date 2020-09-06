<template>
  <VersionProfileCard v-bind="version" />
  <!-- Files
  <h4 class="ui horizontal divider">
    files
  </h4>
  <ul>
    <li v-for="file in version.attachedFiles" :key="file.id">
      <a :href="file.attached_file">
        <i class="file pdf outline icon"></i> {{ file.name }}
      </a>
    </li>
  </ul> -->
  <!-- Comments
  <h4 class="ui horizontal divider">
    coming soon: discussion
  </h4>
  <div class="ui raised segment">
    <div class="ui placeholder">
      <div class="image header">
        <div class="line"></div>
        <div class="line"></div>
      </div>
      <div class="paragraph">
        <div class="medium line"></div>
        <div class="short line"></div>
      </div>
    </div>
  </div>
  <div class="ui raised segment">
    <div class="ui placeholder">
      <div class="image header">
        <div class="line"></div>
        <div class="line"></div>
      </div>
      <div class="paragraph">
        <div class="medium line"></div>
        <div class="short line"></div>
      </div>
    </div>
  </div>
  <div class="ui raised segment">
    <div class="ui placeholder">
      <div class="image header">
        <div class="line"></div>
        <div class="line"></div>
      </div>
      <div class="paragraph">
        <div class="medium line"></div>
        <div class="short line"></div>
      </div>
    </div>
  </div> -->
</template>

<script>
import { mapGetters } from 'vuex';

import VersionProfileCard from '@/components/VersionProfileCard';

export default {
  name: 'VersionDetail',
  components: { VersionProfileCard },
  computed: {
    ...mapGetters(['hydratedVersion']),
    version() {
      return this.hydratedVersion(this.$route.params.version);
    },
  },
  created() {
    this.$store.dispatch('getVersionBySlugs', this.$route.params);
    this.$store.dispatch('retrieveAttachedFiles');
  },
};
</script>

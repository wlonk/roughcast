<template>
  <div>
    <VersionProfileCard v-bind="version" />
    <div class="version-content main-content">
      <FileList :files="version.attachedFiles" />
      <!-- Comments here -->
    </div>
  </div>
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
import FileList from '@/components/FileList';

export default {
  name: 'VersionDetail',
  components: { VersionProfileCard, FileList },
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

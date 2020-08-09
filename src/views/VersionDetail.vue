<template>
  <div>
    <VersionSection v-bind="version" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import VersionSection from '@/components/VersionSection';

export default {
  name: 'VersionDetail',
  components: { VersionSection },
  computed: {
    ...mapState(['Version']),
    version() {
      return _.find(
        this.Version.all,
        v => v.slug === this.$route.params.version,
      );
    },
  },
  created() {
    this.$store.dispatch('getVersionBySlugs', this.$route.params);
    this.$store.dispatch('retrieveAttachedFiles');
  },
};
</script>

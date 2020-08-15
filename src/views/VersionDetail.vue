<template>
  <VersionSection v-bind="version" />
</template>

<script>
import _ from 'lodash';
import { mapGetters } from 'vuex';

import VersionSection from '@/components/VersionSection';

export default {
  name: 'VersionDetail',
  components: { VersionSection },
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

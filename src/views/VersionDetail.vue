<template>
  <div>
    <VersionCard v-bind="version" :isDetail="true" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import VersionCard from '@/components/VersionCard';

export default {
  name: 'VersionDetail',
  components: { VersionCard },
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

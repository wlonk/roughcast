<template>
  <div>
    <Version v-bind="version" :isDetail="true" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import Version from '@/components/Version';

export default {
  name: 'VersionDetail',
  components: { Version },
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
    this.$store.dispatch('getVersionById', this.$route.params.version);
    this.$store.dispatch('retrieveAttachedFiles');
  },
};
</script>

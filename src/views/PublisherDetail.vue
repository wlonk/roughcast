<template>
  <div>
    <Publisher v-bind="publisher" :isOwner="isOwner" :isDetail="true" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import Publisher from '@/components/Publisher';

export default {
  name: 'PublisherDetail',
  components: { Publisher },
  computed: {
    ...mapState(['User', 'Publisher', 'PublisherMembership']),
    isOwner() {
      return (
        _.find(
          this.PublisherMembership.all,
          pm => pm.user === this.User.current.id && pm.is_owner,
        ) !== undefined
      );
    },
    publisher() {
      return _.find(
        this.Publisher.all,
        p => p.slug === this.$route.params.publisher,
      );
    },
  },
  created() {
    this.$store.dispatch('retrievePublisherMemberships');
    this.$store.dispatch('getPublisherById', this.$route.params.publisher);
  },
};
</script>

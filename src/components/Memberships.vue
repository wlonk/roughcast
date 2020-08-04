<template>
  <div>
    <h2>Your Publishers</h2>
    <Publisher
      v-for="(membership, id) in hydratedMemberships"
      :key="id"
      v-bind="membership.publisher"
      :isOwner="membership.is_owner"
    />
    <PublisherForm />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import Publisher from '@/components/Publisher';
import PublisherForm from '@/forms/PublisherForm';

export default {
  name: 'Memberships',
  components: { Publisher, PublisherForm },
  computed: {
    ...mapState(['User', 'Publisher', 'PublisherMembership']),
    hydratedMemberships() {
      // TODO: Filter this to current user!
      const filteredPublisherMemberships = _.filter(
        this.PublisherMembership.all,
        pm => pm.user === this.User.current.username,
      );
      return _.mapValues(filteredPublisherMemberships, pm => ({
        ...pm,
        publisher: this.Publisher.all[pm.publisher_id],
      }));
    },
  },
  created() {
    this.$store.dispatch('retrievePublishers');
    this.$store.dispatch('retrievePublisherMemberships');
  },
};
</script>

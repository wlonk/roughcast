<template>
  <div>
    <PublisherCard v-bind="publisher" />
    <GameList :userCanAddGames="publisher.permissions['game:add']" :games="games" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import PublisherCard from '@/components/PublisherCard';
import GameList from '@/components/GameList';

export default {
  name: 'PublisherDetail',
  components: { PublisherCard, GameList },
  created() {
    this.$store.dispatch('getPublisherById', this.$route.params.publisher);
    this.$store.dispatch('retrieveGames');
  },
  computed: {
    ...mapState(['Publisher', 'Game']),
    publisher() {
      return _.find(
        this.Publisher.all,
        (p) => p.slug === this.$route.params.publisher,
      );
    },
    games() {
      return _.filter(
        this.Game.all,
        (g) => g.publisher === this.publisher.slug
      );
    }
  },
};
</script>

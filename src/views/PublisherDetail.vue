<template>
  <div>
    <PublisherSection v-bind="publisher" />
    <h3 class="ui horizontal divider">
      Games
    </h3>
    <GameList
      :userCanAddGames="publisher.permissions['game:add']"
      :games="games"
    />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import PublisherSection from '@/components/PublisherSection';
import GameList from '@/components/GameList';

export default {
  name: 'PublisherDetail',
  components: { PublisherSection, GameList },
  created() {
    this.$store.dispatch('getPublisherById', this.$route.params.publisher);
    this.$store.dispatch('retrieveGames');
  },
  computed: {
    ...mapState(['Publisher', 'Game']),
    publisher() {
      return _.find(
        this.Publisher.all,
        p => p.slug === this.$route.params.publisher,
      );
    },
    games() {
      return _.filter(this.Game.all, g => g.publisher === this.publisher.slug);
    },
  },
};
</script>

<template>
  <div>
    <GameCard v-bind="game" />
    <VersionList :userCanAddVersions="game.permissions['version:add']" :versions="versions" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import GameCard from '@/components/GameCard';
import VersionList from '@/components/VersionList';

export default {
  name: 'GameDetail',
  components: { GameCard, VersionList },
  computed: {
    ...mapState(['Game', 'Version']),
    game() {
      return _.find(this.Game.all, g => g.slug === this.$route.params.game);
    },
    versions() {
      return _.filter(
        this.Version.all,
        (v) => v.game === this.game.slug
      );
    },
  },
  created() {
    this.$store.dispatch('getGameById', this.$route.params.game);
  },
};
</script>

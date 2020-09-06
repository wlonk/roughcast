<template>
  <div>
    <GameProfileCard v-bind="game" />
    <!-- <div class="box-title">
      <h5>Recent version</h5>
    </div> -->
    <!-- <VersionList
      :team="teamSlug"
      :game="game.slug"
      :userCanAddVersions="game.permissions['version:add']"
      :versions="game.versions"
      :defaultVisibleTo="game.default_visible_to"
    /> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import GameProfileCard from '@/components/GameProfileCard';
import VersionList from '@/components/VersionList';

export default {
  name: 'GameDetail',
  components: { GameProfileCard, VersionList },
  computed: {
    ...mapGetters(['hydratedGame']),
    teamSlug() {
      return this.$route.params.team;
    },
    game() {
      return this.hydratedGame(this.$route.params.game);
    },
  },
  created() {
    this.$store.dispatch('getGameById', this.$route.params.game);
  },
};
</script>

<template>
  <div>
    <GameSection v-bind="game" />
    <h3 class="ui horizontal divider">
      Versions
    </h3>
    <VersionList
      :publisher="publisherSlug"
      :game="game.slug"
      :userCanAddVersions="game.permissions['version:add']"
      :versions="game.versions"
    />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapGetters } from 'vuex';

import GameSection from '@/components/GameSection';
import VersionList from '@/components/VersionList';

export default {
  name: 'GameDetail',
  components: { GameSection, VersionList },
  computed: {
    ...mapGetters(['hydratedGame']),
    publisherSlug() {
      return this.$route.params.publisher;
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

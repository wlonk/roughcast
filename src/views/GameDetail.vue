<template>
  <div>
    <GameSection v-bind="game" />
    <h3 class="ui horizontal divider">
      Versions
    </h3>
    <VersionList :userCanAddVersions="game.permissions['version:add']" :versions="versions" />
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import GameSection from '@/components/GameSection';
import VersionList from '@/components/VersionList';

export default {
  name: 'GameDetail',
  components: { GameSection, VersionList },
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

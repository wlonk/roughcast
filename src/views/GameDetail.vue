<template>
  <div>
    <Game v-bind="game" :isDetail="true" />
  </div>
</template>

<script>
/*
 * TODO:
 * - Show latest version always
 * - Include all-files zip and each-file links
 */
import _ from 'lodash';
import { mapState } from 'vuex';

import Game from '@/components/Game';

export default {
  name: 'GameDetail',
  components: { Game },
  computed: {
    ...mapState(['Game']),
    game() {
      return _.find(this.Game.all, g => g.slug === this.$route.params.game);
    },
  },
  created() {
    this.$store.dispatch('getGameById', this.$route.params.game);
  },
};
</script>

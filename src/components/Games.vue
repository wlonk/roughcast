<template>
  <div>
    <h2>Games</h2>
    <div class="ui cards">
      <Game v-for="(game, id) in Game.all" :key="id" v-bind="game" />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import Game from '@/components/Game';

export default {
  name: 'Games',
  components: { Game },
  computed: mapState(['Game']),
  created() {
    this.$store.dispatch('retrieveGames');
  },
};
</script>

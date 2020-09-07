<template>
  <div>
    <div class="block-content game-list">
      <GameCard v-for="game in gamesWithTeam" :key="game.id" v-bind="game" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GameCard from '@/components/GameCard';

export default {
  name: 'GameList',
  props: {
    team: Object,
    games: Array,
    userCanAddGames: Boolean,
  },
  components: {
    GameCard,
  },
  computed: {
    ...mapGetters(['hydratedGame']),
    gamesWithTeam() {
      return this.games.map(g => this.hydratedGame(g.slug));
    },
  },
};
</script>

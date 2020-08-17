<template>
  <div>
    <div class="ui cards">
      <GameCard
        v-for="game in gamesWithPublisher"
        :key="game.id"
        v-bind="game"
      />
    </div>
    <div v-if="userCanAddGames">
      <h4 class="ui horizontal divider">
        add a game
      </h4>
      <GameForm :forPublisher="publisher.slug" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GameCard from '@/components/GameCard';
import GameForm from '@/forms/GameForm';

export default {
  name: 'GameList',
  props: {
    publisher: Object,
    games: Array,
    userCanAddGames: Boolean,
  },
  components: {
    GameCard,
    GameForm,
  },
  computed: {
    ...mapGetters(['hydratedGame']),
    gamesWithPublisher() {
      return this.games.map(g => this.hydratedGame(g.slug));
    },
  },
};
</script>

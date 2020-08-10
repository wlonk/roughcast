<template>
  <div>
    <div class="ui cards">
      <GameCard v-for="game in games" :key="game.id" v-bind="game" />
    </div>
    <div v-if="userCanAddGames">
      <h4 class="ui horizontal divider">
        add a game
      </h4>
      <GameForm />
    </div>
  </div>
</template>

<script>
import GameCard from '@/components/GameCard';
import GameForm from '@/forms/GameForm';

export default {
  name: 'GameList',
  props: {
    games: Array,
    userCanAddGames: Boolean,
  },
  components: {
    GameCard,
    GameForm,
  },
}
</script>

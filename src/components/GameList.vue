<template>
  <div>
    <GameCard v-for="game in games" :key="game.id" v-bind="game" />
    <GameForm v-if="userCanAddGames" />
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

<template>
  <div class="content-list">
    <GameCard v-for="game in games" :key="game.slug" v-bind="game" />
  </div>
</template>

<script>
import GameCard from '@/components/GameCard';

export default {
  name: 'UserGames',
  components: {
    GameCard,
  },
  props: {
    games: Array,
  },
};
</script>

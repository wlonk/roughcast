<template>
  <div class="user-game-block">
    <div class="box-title">
      <h5>{{ group.name }}</h5>
    </div>
    <div class="content-list">
      <GameCard v-for="game in games" :key="game.slug" v-bind="game" />
    </div>
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
    group: Object,
    games: Array,
  },
};
</script>

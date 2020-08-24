<template>
  <div class="user-game-block">
    <div class="box-title">
      <h5>All games</h5>
    </div>
    <div class="games">
      <GameCard v-for="(game, index) in games" :key="index" v-bind="game"/>
      <GameCard v-for="(game, index) in games" :key="index" v-bind="game"/>
      <GameCard v-for="(game, index) in games" :key="index" v-bind="game"/>
    </div>
  </div>
</template>

<script>
import GameCard from '@/components/GameCard';

export default {
  name: 'UserGames',
  data() {
    return {
      games: [{
        id: "id",
        name:"Coven",
        slug: "transneptune-games",
        description:"A game about witches. The Coven can be played with friends.",
        team: { name: "Transneptune Games" },
        latest_version: { name: "v0.2.2" },
        permissions: { delete: true, },
      }]
    }
  },
  components: {
    GameCard
  }
};
</script>

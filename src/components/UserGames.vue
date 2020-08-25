<template>
  <div class="user-game-block">
    <div class="box-title">
      <h5>{{ group }}</h5>
    </div>
    <div class="games">
      <GameCard v-for="(game, index) in games" :key="0" v-bind="game"/>
      <GameCard v-for="(game, index) in games" :key="1" v-bind="game"/>
      <GameCard v-for="(game, index) in games" :key="2" v-bind="game"/>
    </div>
  </div>
</template>

<script>
import GameCard from '@/components/GameCard';

export default {
  name: 'UserGames',
  components: {
    GameCard
  },
  props: {
    group: String
  },
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
};
</script>

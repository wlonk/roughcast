<template>
  <div id="dashboard">
    <h1>Dashboard</h1>
    <h2 class="ui horizontal divider header">
      games
    </h2>
    <GameList :userCanAddGames="false" :games="gamesWithTeam" />

    <h2 class="ui horizontal divider header">
      groups
    </h2>
    <TeamList :teams="listTeams" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GameList from '@/components/GameList';
import TeamList from '@/components/TeamList';

export default {
  name: 'DashBoard',
  components: {
    GameList,
    TeamList,
  },
  computed: {
    ...mapGetters(['listGames', 'hydratedGame', 'listTeams']),
    gamesWithTeam() {
      return this.listGames.map(g => this.hydratedGame(g.slug));
    },
  },
};
</script>

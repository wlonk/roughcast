<template>
  <div>
    <TeamProfileCard v-bind="team" />
    <div class="box-title">
      <h5>All games</h5>
    </div>
    <GameList
      :team="team"
      :userCanAddGames="team.permissions['game:add']"
      :games="team.games"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import TeamProfileCard from '@/components/TeamProfileCard';
import GameList from '@/components/GameList';

export default {
  name: 'TeamDetail',
  components: { TeamProfileCard, GameList },
  created() {
    this.$store.dispatch('getTeamById', this.$route.params.team);
    this.$store.dispatch('retrieveGames');
  },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team() {
      return this.hydratedTeam(this.$route.params.team);
    },
  },
};
</script>

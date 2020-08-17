<template>
  <div>
    <TeamSection v-bind="team" />
    <h3 class="ui horizontal divider">
      Games
    </h3>
    <GameList
      :team="team"
      :userCanAddGames="team.permissions['game:add']"
      :games="team.games"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import TeamSection from '@/components/TeamSection';
import GameList from '@/components/GameList';

export default {
  name: 'TeamDetail',
  components: { TeamSection, GameList },
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

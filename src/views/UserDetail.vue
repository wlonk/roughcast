<template>
  <div class="user-elements">
    <UserProfileCard v-bind="user" />
    <div class="wrapper">
      <div>
        <div class="box-title">
          <h5>{{ chosenTeam.name }}</h5>
        </div>
        <TeamTabs
          @choose-team="changeActiveTeam"
          :teams="teams"
          :chosen="chosenTeam"
        />
      </div>
      <UserGames :games="filteredGames" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import UserProfileCard from '@/components/UserProfileCard';
import UserGames from '@/components/UserGames';
import TeamTabs from '@/components/TeamTabs';

const allGames = { name: 'All games', slug: '*' };

export default {
  name: 'UserDetail',
  components: {
    UserProfileCard,
    TeamTabs,
    UserGames,
  },
  data() {
    return {
      chosenTeam: allGames,
    };
  },
  methods: {
    changeActiveTeam(team) {
      this.chosenTeam = team;
    },
  },
  computed: {
    ...mapGetters(['hydratedUser', 'myTeams', 'listGames', 'gamesForTeam']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
    teams() {
      return [
        allGames,
        ...this.myTeams.map((t) => ({ name: t.name, slug: t.slug })),
      ];
    },
    filteredGames() {
      if (this.chosenTeam.slug === '*') {
        return this.listGames;
      }
      return this.gamesForTeam(this.chosenTeam.slug);
    },
  },
  created() {
    this.$store.dispatch('getUserById', this.$route.params.username);
    this.$store.dispatch('retrieveTeams');
  },
};
</script>

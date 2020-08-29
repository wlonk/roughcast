<template>
  <div>
    <UserCard v-bind="user" />
    <div class="user-elements">
      <GroupTabs
        @choose-group="changeActiveGroup"
        :groups="groups"
        :chosen="chosenGroup"  />
      <UserGames
        :group="chosenGroup"
        :games="filteredGames"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import UserCard from '@/components/UserCard';
import GroupTabs from '@/components/GroupTabs';
import UserGames from '@/components/UserGames';

const allGames = { name: 'All games', slug: '*' };

export default {
  name: 'UserDetail',
  components: {
    UserCard,
    GroupTabs,
    UserGames
  },
  data() {
    return {
      chosenGroup: allGames,
    }
  },
  methods: {
    changeActiveGroup(group)  {
      return this.chosenGroup = group;
    }
  },
  computed: {
    ...mapGetters(['hydratedUser', 'myTeams', 'listGames', 'gamesForTeam']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
    groups() {
      return [
        allGames,
        ...this.myTeams.map(t => ({ name: t.name, slug: t.slug })),
      ];
    },
    filteredGames() {
      if (this.chosenGroup.slug === '*') {
        return this.listGames;
      }
      return this.gamesForTeam(this.chosenGroup.slug);
    },
  },
  created() {
    this.$store.dispatch('getUserById', this.$route.params.username);
    this.$store.dispatch('retrieveTeams');
  },
};
</script>

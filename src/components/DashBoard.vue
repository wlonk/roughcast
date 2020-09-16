<template>
  <div class="dashboard">
    <div class="header">
      <h2 class="page-title">
        Welcome back,
        <router-link :to="`/u/${currentUser.username}`" class="accent-link">
          {{ currentUser.first_name || currentUser.username }}
        </router-link>
      </h2>
      <div class="dashboard-tabs">
        <button
          @click="toggleTab"
          :class="active_tab === 'games' && 'active'"
          data-tab="games"
        >
          Games
        </button>
        <button
          @click="toggleTab"
          :class="active_tab === 'group' && 'active'"
          data-tab="group"
        >
          Groups
        </button>
        <div class="bottom-border"></div>
      </div>
    </div>
    <SearchAndFiltersPanel />
    <GameList
      v-if="active_tab === 'games'"
      :userCanAddGames="false"
      :games="gamesWithTeam"
    />
    <TeamList v-if="active_tab === 'group'" :teams="listTeams" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GameList from '@/components/GameList';
import TeamList from '@/components/TeamList';
import SearchAndFiltersPanel from '@/components/SearchAndFiltersPanel';

export default {
  name: 'DashBoard',
  data() {
    return {
      active_tab: 'games',
    };
  },
  components: {
    GameList,
    TeamList,
    SearchAndFiltersPanel,
  },
  computed: {
    ...mapGetters(['listGames', 'hydratedGame', 'listTeams', 'currentUser']),
    gamesWithTeam() {
      return this.listGames.map(g => this.hydratedGame(g.slug));
    },
  },
  methods: {
    toggleTab(e) {
      this.active_tab = e.target.dataset.tab;
    },
  },
};
</script>

<template>
  <div>
    <h1>Dashboard</h1>
    <h2 class="ui horizontal divider header">
      games
    </h2>
    <GameList :userCanAddGames="false" :games="gamesWithPublisher" />

    <h2 class="ui horizontal divider header">
      groups
    </h2>
    <PublisherList :publishers="listPublishers" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GameList from '@/components/GameList';
import PublisherList from '@/components/PublisherList';

export default {
  name: 'DashBoard',
  components: {
    GameList,
    PublisherList,
  },
  computed: {
    ...mapGetters(['listGames', 'hydratedGame', 'listPublishers']),
    gamesWithPublisher() {
      return this.listGames.map(g => this.hydratedGame(g.slug));
    },
  },
};
</script>

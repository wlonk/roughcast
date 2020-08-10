<template>
  <div>
    <h1>Dashboard</h1>
    <h2 class="ui horizontal divider header">
      games
    </h2>
    <GameList :userCanAddGames="false" :games="games" />

    <h2 class="ui horizontal divider header">
      groups
    </h2>
    <PublisherList :publishers="publishers" />

  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';
import GameList from '@/components/GameList';
import PublisherList from '@/components/PublisherList';

export default {
  name: 'DashBoard',
  components: {
    GameList,
    PublisherList,
  },
  computed: {
    ...mapState(['Game', 'Publisher']),
    games() {
      return _.values(this.Game.all);
    },
    publishers() {
      return _.values(this.Publisher.all);
    },
  }
}
</script>

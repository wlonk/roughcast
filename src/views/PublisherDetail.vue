<template>
  <div>
    <PublisherSection v-bind="publisher" />
    <h3 class="ui horizontal divider">
      Games
    </h3>
    <GameList
      :publisher="publisher"
      :userCanAddGames="publisher.permissions['game:add']"
      :games="publisher.games"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import PublisherSection from '@/components/PublisherSection';
import GameList from '@/components/GameList';

export default {
  name: 'PublisherDetail',
  components: { PublisherSection, GameList },
  created() {
    this.$store.dispatch('getPublisherById', this.$route.params.publisher);
    this.$store.dispatch('retrieveGames');
  },
  computed: {
    ...mapGetters(['hydratedPublisher']),
    publisher() {
      return this.hydratedPublisher(this.$route.params.publisher);
    },
  },
};
</script>

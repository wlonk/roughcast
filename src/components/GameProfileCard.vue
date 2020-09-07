<template>
  <div class="game-profile-card">
    <img v-if="banner" :src="banner" alt="banner" />
    <img v-else src="../assets/no-game-image.svg" alt="no game banner" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <div class="team">
          <router-link :to="`/t/${team.slug}`" class="link">
            {{ shorted_team_name }}
          </router-link>
        </div>
      </div>
      <div>
        <div>
          <h5>Description</h5>
          <RenderedMarkdown v-if="description" :body="description" />
          <p v-else class="no-bio">There is no game description yet...</p>
        </div>
        <GameCardControlPanel
          :permissions="permissions"
          :slug="slug"
          :team_slug="team.slug"
          :is_subscribed="is_subscribed"
        />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';
import GameCardControlPanel from '@/components/GameCardControlPanel';

export default {
  name: 'GameProfileCard',
  components: {
    RenderedMarkdown,
    GameCardControlPanel,
  },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    team: Object,
    latest_version: Object,
    permissions: Object,
    banner: String,
    is_subscribed: Boolean,
    is_owner: Boolean,
  },
  computed: {
    shorted_team_name() {
      const team_name = this.team.name;
      return team_name.length > 20
        ? team_name.substring(0, 20) + '...'
        : team_name;
    },
  },
};
</script>

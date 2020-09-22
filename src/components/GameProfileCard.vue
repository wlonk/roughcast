<template>
  <div class="game-profile-card profile-card">
    <img v-if="banner" :src="banner" :alt="`${name} banner`" />
    <img v-else src="../assets/no-game-image.svg" alt="No game banner" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <div class="team">
          <router-link :to="`/t/${team.slug}`" class="link">
            {{ shortened_team_name }}
          </router-link>
        </div>
      </div>
      <div>
        <div>
          <h6 class="section-title">Description</h6>
          <RenderedMarkdown v-if="description" :body="description" />
          <p v-else class="no-bio">There is no game description yet&hellip;</p>
        </div>
        <GameCardControlPanel
          :permissions="permissions"
          :slug="slug"
          :team_slug="team.slug"
          :gameId="id"
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
    shortened_team_name() {
      const team_name = this.team.name;
      return team_name.length > 20
        ? team_name.substring(0, 20) + '\u2026'
        : team_name;
    },
  },
};
</script>

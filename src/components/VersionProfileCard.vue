<template>
  <div class="version-profile-card profile-card">
    <img v-if="game.banner" :src="game.banner" :alt="`${game.name} banner`" />
    <img v-else src="../assets/no-game-image.svg" alt="No game banner" />
    <div>
      <div class="header">
        <h4 class="card-title">
          <router-link :to="`/t/${game.team}/${game.slug}`" class="accent-link">
            {{ game.name }}
          </router-link>
          <span>@{{ name }}</span>
        </h4>
        <div v-if="added">
          <h6 class="section-title">Added</h6>
          <p>{{ added }}</p>
        </div>
      </div>
      <div class="team">
        <router-link :to="`/t/${game.team}`" class="link">
          {{ team_name }}
        </router-link>
      </div>
      <div>
        <div class="description">
          <h6 class="section-title">Changes</h6>
          <RenderedMarkdown v-if="changelog" :body="changelog" />
          <p v-else class="no-bio">There is no changes yet&hellip;</p>
        </div>
        <div class="controls">
          <router-link
            :to="`/t/${game.team}/${game.slug}/${slug}/edit`"
            v-if="permissions['this:edit']"
            class="accent-link"
          >
            Edit Version
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'VersionSection',
  props: {
    id: String,
    name: String,
    team: String,
    game: Object,
    gameSlug: String,
    slug: String,
    changelog: String,
    archive_link: String,
    permissions: Object,
    attachedFiles: Array,
    added: String,
  },
  components: { RenderedMarkdown },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team_name() {
      return this.hydratedTeam(this.game.team).name;
    },
  },
};
</script>

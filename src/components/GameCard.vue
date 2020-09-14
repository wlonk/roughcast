<template>
  <div class="game-card">
    <div>
      <div>
        <img v-if="banner" :src="banner" :alt="`${name} banner`" />
        <img v-else src="../assets/no-game-image.svg" alt="No game banner" />
      </div>
      <div class="header">
        <GameCardMenu
          v-if="permissions['this:edit']"
          :slug="slug"
          :team="team_name"
        />
        <router-link :to="`/t/${team_slug}/${slug}`" class="small-card-title">
          {{ shortened_title }}
          <div v-if="name.length > 19" class="inline">
            <div class="ui pointing label">
              {{ name }}
            </div>
          </div>
        </router-link>
        <div tabindex="0" class="team">
          {{ shortened_team_name }}
          <div v-if="team_name.length > 18" class="inline">
            <div class="ui pointing label">
              {{ team_name }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="description">
      <RenderedMarkdown :body="description" />
    </div>
    <div class="footer">
      <CardStatistic :likes="likes" :comments="comments" />
      <div class="authors">
        <AuthorPreview
          v-for="author in shortened_authors"
          :key="author.id"
          v-bind="author"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';
import GameCardMenu from '@/components/GameCardMenu';
import AuthorPreview from '@/components/AuthorPreview';
import CardStatistic from '@/components/CardStatistic';

export default {
  name: 'GameCard',
  components: {
    RenderedMarkdown,
    GameCardMenu,
    AuthorPreview,
    CardStatistic,
  },
  props: {
    banner: String,
    id: String,
    name: String,
    slug: String,
    description: String,
    team: [String, Object],
    latest_version: Object,
    permissions: Object,
    likes: String,
    comments: String,
    authors: Array,
  },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team_name() {
      return typeof this.team === 'string'
        ? this.hydratedTeam(this.team).name
        : this.team.name;
    },
    team_slug() {
      return typeof this.team !== 'string' ? this.team.slug : this.team;
    },
    shortened_team_name() {
      const team = this.team_name;
      return team.length > 18 ? team.substring(0, 18) + '\u2026' : team;
    },
    shortened_title() {
      return this.name.length > 19
        ? this.name.substring(0, 19) + '\u2026'
        : this.name;
    },
    shortened_authors() {
      return this.authors && this.authors.length > 5
        ? this.authors.slice(0, 5)
        : this.authors;
    },
  },
};
</script>

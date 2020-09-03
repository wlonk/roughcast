<template>
  <div class="game-card">
    <div>
      <div>
        <img v-if="banner" :src="banner" alt="no game banner" />
        <img v-else src="../assets/no-game-image.svg" alt="no game banner" />
      </div>
      <div class="header">
        <GameCardMenu v-if="permissions['this:edit']" />
        <router-link :to="`/t/${team}/${slug}`" class="game-card-title">
          {{ shorted_title }}
          <div  v-if="name.length > 19" class="inline">
            <div class="ui pointing label">
              {{ name }}
            </div>
          </div>
        </router-link>
        <div class="team">
          {{ shorted_team_name }}
          <div  v-if="team.length > 20" class="inline">
            <div class="ui pointing label">
              {{ team_name }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="description">
      <RenderedMarkdown :body="shorted_description" />
    </div>
    <div class="footer">
      <CardStatistic :likes="likes" :comments="comments" />
      <div class="authors">
        <AuthorPreview
          v-for="(author, index) in shorted_authors"
          :key="index"
          :username="author.username"
          :avatar="author.avatar"
        />
        <!-- Hardcoded -->
        <AuthorPreview
          username="mayzee"
          :avatar="null"
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
    CardStatistic
  },
  props: {
    banner: String,
    id: String,
    name: String,
    slug: String,
    description: String,
    team: String,
    latest_version: Object,
    permissions: Object,
    likes: Number,
    comments: Number,
    authors: Array
  },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team_name() {
      return this.hydratedTeam(this.team).name
    },
    shorted_team_name() {
      const team = this.team_name;
      return (team.length > 20)
        ? team.substring(0, 20) + '...'
        : team;
    },
    shorted_title() {
      return (this.name.length > 19)
        ? this.name.substring(0, 19) + '...'
        : this.name;
    },
    shorted_description() {
      return (this.description.length > 82)
        ? this.description.substring(0, 82) + '...'
        : this.description;
    },
    shorted_authors() {
      return (this.authors && this.authors.length > 5)
        ? this.authors.slice(0, 5)
        : this.authors;
    },
  },
};
</script>

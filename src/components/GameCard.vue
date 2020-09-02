<template>
  <div class="game-card">
    <div>
      <div>
        <img v-if="banner" :src="banner" alt="no game banner" />
        <img v-else src="../assets/no-game-image.svg" alt="no game banner" />
      </div>
      <div class="header">
        <GameCardMenu v-if="permissions['this:edit']" />
        <router-link :to="`/t/${team.slug}/${slug}`" class="game-card-title">
          {{ name }}
        </router-link>
        <div class="team">
          <p>{{ team_name }}</p>
        </div>
      </div>
    </div>
    <div class="description">
      <RenderedMarkdown :body="description" />
    </div>
    <div class="footer">
      <div class="states">
        <i class="heart icon"></i>
        <p class="likes">{{ likes || 0 }}</p>
        <i class="comment icon"></i>
        <p class="comments">{{ comments || 0 }}</p>
      </div>
      <div class="authors">
        <!-- <router-link
          v-for="(author, index) in authors"
          :key="index"
          :to="`/u/${author.username}`">
          <img
            :src="item.avatar"
            alt="author avatar">
        </router-link> -->
        <img src="../assets/no-avatar.svg" alt="author avatar">
        <img src="../assets/no-avatar.svg" alt="author avatar">
        <img src="../assets/no-avatar.svg" alt="author avatar">
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';
import GameCardMenu from '@/components/GameCardMenu';

export default {
  name: 'GameCard',
  components: { RenderedMarkdown, GameCardMenu },
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
      return this.hydratedTeam(this.team).name;
    },
  },
};
</script>

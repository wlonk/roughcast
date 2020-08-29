<template>
  <div class="game-card">
    <div>
      <img v-if="avatar" :src="avatar" alt="no game avatar">
      <img v-else src="../assets/no-game-image.svg" alt="no game avatar">
      <div class="header">
        <div class="states">
          <i class="heart icon"></i>
          <p class="likes">{{ likes || 0 }}</p>
          <i class="comment icon"></i>
          <p class="comments">{{ comments || 0 }}</p>
          <GameCardMenu v-if="permissions['this:edit']" />
        </div>
        <div class="team">
          <p>{{ team.name }}</p>
        </div>
      </div>
    </div>
    <div class="content">
      <div>
        <router-link :to="`/t/${team.slug}/${slug}`" class="game-card-title">
          {{ name }}
        </router-link>
        <span>@{{ latest_version.name }}</span>
      </div>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';
import GameCardMenu from '@/components/GameCardMenu';

export default {
  name: 'GameCard',
  components: { RenderedMarkdown, GameCardMenu },
  props: {
    avatar: String,
    id: String,
    name: String,
    slug: String,
    description: String,
    team: Object,
    latest_version: Object,
    permissions: Object,
    likes: Number,
    comments: Number
  },
};
</script>

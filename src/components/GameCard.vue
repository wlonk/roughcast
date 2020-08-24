<template>
  <div class="game-card">
    <div>
      <img v-if="avatar" :src="avatar" alt="no game avatar">
      <img v-else src="../assets/no-game-image.svg" alt="no game avatar">
      <div class="states">
        <div>
          <i class="heart icon"></i>
          <p class="likes">{{ likes || 0 }}</p>
        </div>
        <div>
          <i class="comment icon"></i>
          <p class="comments">{{ comments || 0 }}</p>
        </div>
      </div>
    </div>
    <div>
      <!-- <i
        class="right floated trash alternate icon"
        v-if="permissions['this:delete']"
      ></i> -->
      <!-- card menu here -->
      <div>
        <router-link :to="`/t/${team.slug}/${slug}`" class="header">
          {{ name }}
        </router-link>
        <span>@{{ latest_version.name }}</span>
      </div>
      <div class="team">
        <p>{{ team.name }}</p>
      </div>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'GameCard',
  components: { RenderedMarkdown },
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

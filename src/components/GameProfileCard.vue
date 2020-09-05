<template>
  <div class="game-profile-card">
    <img v-if="banner" :src="banner" alt="banner" />
    <img v-else src="../assets/no-game-image.svg" alt="no game banner" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <div class="team">
          <router-link :to="`/t/${team.slug}`" class="link">
            {{ team.name }}
          </router-link>
        </div>
      </div>
      <div>
        <div>
          <h5>Description</h5>
          <RenderedMarkdown
            v-if="description"
            :body="description" />
          <p v-else class="no-bio">There is no game description yet...</p>
        </div>
        <div class="controls">
          <button
            v-if="!permissions['this:edit'] && !is_subscribed"
            class="small submit-btn">Subscribe</button>
          <button
            v-if="is_subscribed"
            class="subscribed-label">Subscribed</button>
          <router-link
            :to="`/t/${team.slug}/${slug}/edit`"
            v-if="permissions['this:edit']"
            class="accent-link">
            Edit game
          </router-link>
          <router-link
            :to="`/t/${team.slug}/${slug}/edit#add-version`"
            v-if="permissions['version:add']"
            class="accent-link">
            Add version
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'GameProfileCard',
  components: { RenderedMarkdown },
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
};
</script>

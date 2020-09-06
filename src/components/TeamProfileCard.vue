<template>
  <div class="team-profile-card">
    <img v-if="logo" :src="logo" alt="team logo" />
    <img v-else src="../assets/no-team-logo.svg" alt="no team logo" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <a v-if="url" :href="url" class="round-link"></a>
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
            v-if="!permissions['this:edit'] && !is_subscribed && !is_invited"
            class="small submit-btn">Subscribe</button>
          <button
            v-if="is_subscribed"
            class="subscribed-label">Subscribed</button>
          <router-link
            :to="`/t/${slug}/edit`"
            v-if="permissions['this:edit']"
            class="accent-link">
            Edit Team
          </router-link>
          <router-link
            :to="`/g/add`"
            v-if="permissions['game:add']"
            class="accent-link">
            Add Game
          </router-link>
          <div v-if="is_invited" class="invitation">
            <p>You've been invited</p>
            <button class="small submit-btn">Join team</button>
            <button class="small submit-btn">
              <i class="ban icon"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'TeamProfileCard',
  components: { RenderedMarkdown },
  props: {
    id: String,
    name: String,
    permissions: Object,
    slug: String,
    url: String,
    description: String,
    user_is_owner: Boolean,
    is_subscribed: Boolean,
    // is_subscribed: {
    //   default: true
    // },
    is_invited: Boolean,
    // is_invited: {
    //   default: true
    // },
    logo: String,
  },
};
</script>

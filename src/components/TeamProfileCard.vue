<template>
  <div class="team-profile-card">
    <img v-if="logo" :src="logo" :alt="`${name} team logo`" />
    <img v-else src="../assets/no-team-logo.svg" alt="No team logo" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <a v-if="url" :href="url" class="round-link"></a>
      </div>
      <div>
        <div>
          <h5>Description</h5>
          <RenderedMarkdown v-if="description" :body="description" />
          <p v-else class="no-bio">There is no game description yet&hellip;</p>
        </div>
        <TeamCardControlPanel
          :permissions="permissions"
          :slug="slug"
          :is_subscribed="is_subscribed"
          :is_invited="is_invited"
        />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';
import TeamCardControlPanel from '@/components/TeamCardControlPanel';

export default {
  name: 'TeamProfileCard',
  components: {
    RenderedMarkdown,
    TeamCardControlPanel,
  },
  props: {
    id: String,
    name: String,
    permissions: Object,
    slug: String,
    url: String,
    description: String,
    user_is_owner: Boolean,
    logo: String,
    is_subscribed: Boolean,
    is_invited: Boolean,
  },
};
</script>

<template>
  <div class="team-profile-card profile-card">
    <img v-if="logo" :src="logo" :alt="`${name} team logo`" />
    <img v-else src="../assets/no-team-logo.svg" alt="No team logo" />
    <div>
      <div class="header">
        <h4 class="card-title">{{ name }}</h4>
        <a v-if="url" :href="url" class="round-link"></a>
      </div>
      <div>
        <div>
          <h6 class="section-title">Description</h6>
          <RenderedMarkdown v-if="description" :body="description" />
          <p v-else class="no-bio">There is no team description yet&hellip;</p>
        </div>
        <div class="small-card">
          <div class="footer">
            <div class="authors">
              <AuthorPreview
                v-for="member in members"
                :key="member.id"
                :username="member.username"
                :avatar="member.avatar"
              />
            </div>
          </div>
        </div>
        <TeamCardControlPanel
          :permissions="permissions"
          :slug="slug"
          :teamId="id"
          :is_invited="is_invited"
        />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';
import TeamCardControlPanel from '@/components/TeamCardControlPanel';
import AuthorPreview from '@/components/AuthorPreview';

export default {
  name: 'TeamProfileCard',
  components: {
    RenderedMarkdown,
    TeamCardControlPanel,
    AuthorPreview,
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
    is_invited: Boolean,
    members: Array,
  },
};
</script>

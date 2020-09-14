<template>
  <div class="team-card">
    <div>
      <div>
        <img v-if="logo" :src="logo" :alt="`${name} team logo`" />
        <img v-else src="../assets/no-team-logo.svg" alt="No team logo" />
      </div>
      <div class="header">
        <TeamCardMenu v-if="user_is_owner" :slug="slug" />
        <router-link :to="`/t/${slug}`" class="small-card-title">
          {{ name }}
          <div v-if="name.length > 30" class="inline">
            <div class="ui pointing label">
              {{ name }}
            </div>
          </div>
        </router-link>
      </div>
    </div>
    <div class="description">
      <RenderedMarkdown :body="description" />
    </div>
    <div class="footer">
      <CardStatistic :games="games" :subscribers="subscribers" />
      <div class="owners">
        <AuthorPreview
          v-for="(owner, index) in shortened_owners"
          :key="index"
          :username="owner.username"
          :avatar="owner.avatar"
        />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';
import TeamCardMenu from '@/components/TeamCardMenu';
import AuthorPreview from '@/components/AuthorPreview';
import CardStatistic from '@/components/CardStatistic';

export default {
  name: 'TeamCard',
  components: {
    RenderedMarkdown,
    TeamCardMenu,
    AuthorPreview,
    CardStatistic,
  },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    url: String,
    permissions: Object,
    user_is_owner: Boolean,
    user_is_member: Boolean,
    logo: String,
    owners: Array,
    games: String,
    subscribers: String,
  },
  computed: {
    shortened_owners() {
      return this.owners && this.owners.length > 5
        ? this.owners.slice(0, 5)
        : this.owners;
    },
  },
};
</script>

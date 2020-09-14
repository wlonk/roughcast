<template>
  <div class="version-card">
    <div class="header">
      <router-link :to="`/t/${team}/${game}/${slug}`" class="small-card-title">
        {{ name }}
      </router-link>
      <div>
        <div v-if="added">
          <h5>Added</h5>
          <p>{{ added }}</p>
        </div>
        <a :href="archive_link" class="round-link"></a>
      </div>
    </div>
    <div class="content">
      <h5>Changes</h5>
      <span>{{ changelog_short }}</span>
    </div>
    <div class="footer">
      <CardStatistic :comments="comments" />
      <div class="authors">
        <AuthorPreview
          :username="created_by"
          :avatar="author.avatar"
          :user_name="author.first_name"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import AuthorPreview from '@/components/AuthorPreview';
import CardStatistic from '@/components/CardStatistic';

export default {
  name: 'VersionCard',
  components: {
    AuthorPreview,
    CardStatistic,
  },
  props: {
    id: String,
    name: String,
    version: String,
    team: String,
    changelog: String,
    changelog_short: String,
    game: String,
    slug: String,
    archive_link: String,
    permissions: Object,
    added: String,
    comments: String,
    created_by: String,
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    author() {
      return this.hydratedUser(this.created_by);
    },
  },
};
</script>

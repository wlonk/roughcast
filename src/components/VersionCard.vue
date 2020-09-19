<template>
  <div class="version-card small-card">
    <div class="header">
      <router-link :to="`/t/${team}/${game}/${slug}`" class="small-card-title">
        {{ name }}
      </router-link>
      <div>
        <div v-if="added">
          <h6 class="section-title">Added</h6>
          <p>{{ added }}</p>
        </div>
        <a :href="archive_link" class="round-link"></a>
        <i v-if="!extended" class="sort up icon" @click="toggleContent"></i>
        <i v-else class="sort down icon" @click="toggleContent"></i>
      </div>
    </div>
    <div v-if="extended" class="content">
      <div>
        <h6 class="section-title">Changes</h6>
        <span>{{ changelog_short }}</span>
      </div>
      <div class="footer">
        <div>
          <CardStatistic v-if="comments" :comments="comments" />
        </div>
        <div class="authors">
          <AuthorPreview
            :username="created_by"
            :avatar="author.avatar"
            :user_name="author.first_name"
          />
        </div>
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
  data() {
    return {
      extended: false,
    };
  },
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
  methods: {
    toggleContent() {
      this.extended = !this.extended;
    },
  },
};
</script>

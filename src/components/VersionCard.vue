<template>
  <div class="version-card">
    <div class="header">
      <router-link :to="`/t/${team}/${game}/${slug}`" class="small-card-title">
        {{ name }}
      </router-link>
      <div>
        <h5>Added</h5>
        <p>{{ added }}</p>
        <a :href="archive_link" class="round-link"></a>
        <i v-if="!extended" class="sort up icon" @click="toggleContent"></i>
        <i v-else class="sort down icon" @click="toggleContent"></i>
      </div>
    </div>
    <div v-if="extended" class="content">
      <div>
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
    added: {
      default: '11/12/2020',
    },
    comments: {
      default: '0',
    },
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

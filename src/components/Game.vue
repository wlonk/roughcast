<template>
  <div class="ui card">
    <div class="content">
      <router-link :to="`/p/${publisher}/${slug}`" class="header">
        {{ name }}
      </router-link>
      <div class="meta">
        <span>{{ publisherName }}, @ {{ latest_version }}</span>
      </div>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>

      <div v-if="isDetail">
        <Version v-for="(version, id) in versions" v-bind="version" :key="id" />
        <div v-if="user_can_add_versions">
          <h3 class="ui header">Add a version</h3>
          <VersionForm :forGame="slug" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import Version from '@/components/Version';
import VersionForm from '@/forms/VersionForm';
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'Game',
  components: { Version, VersionForm, RenderedMarkdown },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    publisher: String,
    latest_version: String,
    user_can_add_versions: Boolean,
    isDetail: {
      type: Boolean,
      default: false,
    },
  },
  created() {
    this.$store.dispatch('retrieveVersions');
  },
  computed: {
    ...mapState(['Version', 'Publisher']),
    versions() {
      return _.pickBy(this.Version.all, v => v.game === this.slug);
    },
    publisherName() {
      return _.find(this.Publisher.all, p => p.slug === this.publisher).name || 'unknown publisher';
    }
  },
};
</script>

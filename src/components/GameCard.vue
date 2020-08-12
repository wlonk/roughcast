<template>
  <div class="ui card">
    <div class="content">
      <i
        class="right floated trash alternate icon"
        v-if="permissions['this:delete']"
      ></i>
      <router-link :to="`/p/${publisher}/${slug}`" class="header">
        {{ name }}
      </router-link>
      <div class="meta">
        <span>{{ publisherName }}, @ {{ latest_version.name }}</span>
      </div>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'GameCard',
  components: { RenderedMarkdown },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    publisher: String,
    latest_version: Object,
    permissions: Object,
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
      return (
        _.find(this.Publisher.all, p => p.slug === this.publisher).name ||
        'unknown publisher'
      );
    },
  },
};
</script>

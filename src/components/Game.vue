<template>
  <div class="game">
    <h3>
      <router-link :to="`/p/${publisher}/${slug}`">
        {{ name }}
      </router-link>
    </h3>
    <RenderedMarkdown :body="description" />
    <div v-if="isDetail">
      <Version v-for="(version, id) in versions" v-bind="version" :key="id" />
      <VersionForm v-if="user_can_add_versions" :forGame="slug" />
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import Version from '@/components/Version';
import VersionForm from '@/components/VersionForm';
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
    ...mapState(['Version']),
    versions() {
      return _.pickBy(this.Version.all, v => v.game === this.slug);
    },
  },
};
</script>

<style>
.game {
  max-width: 900px;
  margin: 0 auto 1rem;
  border: 2px solid grey;
  border-radius: 5px;
  -webkit-box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
  box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
}
</style>

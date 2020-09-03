<template>
  <router-link
    :to="`/u/${username}`">
    <div class="inline">
      <img v-if="avatar"
        :src="avatar"
        alt="author avatar">
      <img v-else src="../assets/no-avatar.svg" alt="author avatar">
      <div class="ui right pointing label">
        Author Name
      </div>
    </div>
  </router-link>
</template>

<script>
import { mapGetters } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';
import GameCardMenu from '@/components/GameCardMenu';

export default {
  name: 'AuthorPreview',
  props: {
    username: String,
    avatar: String,
  },
};
</script>

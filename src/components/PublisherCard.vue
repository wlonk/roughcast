<template>
  <div class="ui card">
    <div class="content">
      <i class="right floated pencil alternate icon" v-if="permissions['this:edit']"></i>
      <i class="right floated chess queen icon" v-if="user_is_owner"></i>
      <a v-if="url" :href="url"><i class="right floated linkify icon"></i></a>
      <router-link :to="`/p/${slug}`" class="header">{{ name }}</router-link>
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
  name: 'PublisherCard',
  props: {
    id: String,
    name: String,
    permissions: Object,
    slug: String,
    url: String,
    description: String,
    user_is_owner: Boolean,
  },
  components: { RenderedMarkdown }
};
</script>

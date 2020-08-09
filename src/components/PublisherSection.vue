<template>
  <div class="ui grid">
    <div class="twelve wide column">
      <i class="small sun icon rc-left-gutter" v-if="user_is_owner"></i>
      <router-link :to="`/p/${slug}`" class="ui header">
        {{ name }}
      </router-link>
      <RenderedMarkdown :body="description" />
    </div>
    <div class="four wide column right aligned">
      <a v-if="url" :href="url"><i class="linkify icon"></i></a>
      <i class="pencil alternate icon" v-if="permissions['this:edit']"></i>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'PublisherSection',
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

<style scoped>
i.rc-left-gutter {
  margin-left: -1.4rem;
  margin-top: 0.6rem;
  vertical-align: top;
}
</style>

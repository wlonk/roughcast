<template>
  <div class="ui card">
    <div class="content">
      <i
        class="right floated trash alternate icon"
        v-if="permissions['this:delete']"
      ></i>
      <router-link :to="`/p/${publisher.slug}/${slug}`" class="header">
        {{ name }}
      </router-link>
      <div class="meta">
        <span>{{ publisher.name }}, @ {{ latest_version.name }}</span>
      </div>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'GameCard',
  components: { RenderedMarkdown },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    publisher: Object,
    latest_version: Object,
    permissions: Object,
  },
};
</script>

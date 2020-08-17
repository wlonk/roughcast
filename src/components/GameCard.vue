<template>
  <div class="ui card">
    <div class="content">
      <i
        class="right floated trash alternate icon"
        v-if="permissions['this:delete']"
      ></i>
      <router-link :to="`/t/${team.slug}/${slug}`" class="header">
        {{ name }}
      </router-link>
      <div class="meta">
        <span>{{ team.name }}, @ {{ latest_version.name }}</span>
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
    team: Object,
    latest_version: Object,
    permissions: Object,
  },
};
</script>

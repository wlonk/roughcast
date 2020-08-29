<template>
  <div>
    <div class="ui grid">
      <div class="four wide column">
        <img
          class="ui small rounded image"
          title="placeholder"
          alt="placeholder"
          src="/static/images/placeholder.png"
        />
      </div>
      <div class="ten wide column">
        <router-link :to="`/t/${team.slug}/${slug}`" class="ui header">
          {{ name }}
          <span class="ui sub header">from {{ team.name }}</span>
        </router-link>
        <div class="meta">
          Latest:
          <router-link :to="`/t/${team.slug}/${slug}/${latest_version.slug}`">{{
            latest_version.name
          }}</router-link>
        </div>
        <div class="description">
          <RenderedMarkdown :body="description" />
        </div>
      </div>
      <div class="two wide column right aligned">
        <i
          title="delete"
          class="trash alternate icon"
          v-if="permissions['this:delete']"
        ></i>
        <i
          title="edit"
          class="pencil alternate icon"
          v-if="permissions['this:edit']"
        ></i>
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'GameSection',
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

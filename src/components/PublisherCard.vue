<template>
  <div class="ui card">
    <div class="content">
      <i
        v-if="user_is_member && !user_is_owner"
        class="right floated card outline icon"
      ></i>
      <i v-if="user_is_owner" class="right floated sun outline icon"></i>
      <router-link :to="`/p/${slug}`" class="header">
        {{ name }}
      </router-link>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
    </div>
  </div>
</template>

<script>
import RenderedMarkdown from '@/components/RenderedMarkdown';

export default {
  name: 'PublisherCard',
  components: { RenderedMarkdown },
  props: {
    id: String,
    name: String,
    slug: String,
    description: String,
    url: String,
    permissions: Object,
    user_is_owner: Boolean,
    user_is_member: Boolean,
  },
};
</script>

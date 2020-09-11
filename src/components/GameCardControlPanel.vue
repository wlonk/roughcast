<template>
  <div class="controls">
    <button v-if="checkPermisions" class="small submit-btn">
      Subscribe
    </button>
    <button v-if="is_subscribed" class="subscribed-label">Subscribed</button>
    <router-link
      :to="`/t/${team_slug}/${slug}/edit`"
      v-if="permissions['this:edit']"
      class="accent-link"
    >
      Edit game
    </router-link>
    <router-link
      :to="`/t/${team_slug}/${slug}/edit#add-version`"
      v-if="permissions['version:add']"
      class="accent-link"
    >
      Add version
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'GameCardControlPanel',
  props: {
    permissions: Object,
    slug: String,
    team_slug: String,
    is_subscribed: Boolean,
  },
  computed: {
    checkPermisions() {
      return !permissions['this:edit'] && !is_subscribed;
    },
  },
};
</script>

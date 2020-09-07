<template>
  <div class="controls">
    <button
      v-if="!permissions['this:edit'] && !is_subscribed && !is_invited"
      class="small submit-btn"
    >
      Subscribe
    </button>
    <button v-if="is_subscribed" class="subscribed-label">Subscribed</button>
    <router-link
      :to="`/t/${slug}/edit`"
      v-if="permissions['this:edit']"
      class="accent-link"
    >
      Edit Team
    </router-link>
    <router-link
      :to="`/g/add`"
      v-if="permissions['game:add']"
      class="accent-link"
    >
      Add Game
    </router-link>
    <div v-if="is_invited" class="invitation">
      <p>You've been invited</p>
      <button class="small submit-btn">Join team</button>
      <button class="small submit-btn">
        <i class="ban icon"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TeamCardControlPanel',
  props: {
    permissions: Object,
    slug: String,
    is_subscribed: Boolean,
    is_invited: Boolean,
  },
};
</script>

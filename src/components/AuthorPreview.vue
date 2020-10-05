<template>
  <router-link :to="`/u/${username}`">
    <div class="inline">
      <img v-if="avatar" :src="avatar" :alt="`${username} avatar`" />
      <img v-else src="../assets/no-avatar.svg" alt="Mo author avatar" />
      <div class="ui right pointing label">
        {{ username || 'Author Name' }}
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'AuthorPreview',
  props: {
    username: String,
    avatar: String,
  },
};
</script>

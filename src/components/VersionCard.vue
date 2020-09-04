<template>
  <div class="version-card">
    <a :href="archive_link">
      <i class="right floated file archive outline icon"></i>
    </a>
    <router-link :to="`/t/${team}/${game}/${slug}`">
      {{ name }}
    </router-link>
    <span>{{ changelog_short }}</span>
  </div>
</template>

<script>
export default {
  name: 'VersionCard',
  props: {
    id: String,
    name: String,
    version: String,
    team: String,
    changelog: String,
    changelog_short: String,
    game: String,
    slug: String,
    archive_link: String,
    permissions: Object,
  },
};
</script>

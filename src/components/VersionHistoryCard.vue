<template>
  <div class="version-card small-card">
    <div>
      <router-link :to="`/t/${team}/${game}/${slug}`" class="smallest-title">
        {{ name }}
      </router-link>
      <router-link :to="`/t/${team}/${game}/${slug}/edit`" class="link">
        ( edit )
      </router-link>
    </div>
    <div>
      <div v-if="added">
        <h6 class="section-title">Added</h6>
        <p>{{ added }}</p>
      </div>
      <a :href="archive_link" class="round-link"></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VersionHistoryCard',
  props: {
    id: String,
    name: String,
    team: String,
    game: String,
    slug: String,
    archive_link: String,
    added: String,
  },
};
</script>

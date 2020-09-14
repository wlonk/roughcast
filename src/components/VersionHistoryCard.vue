<template>
  <div class="version-card">
    <div>
      <router-link :to="`/t/${team}/${game}/${slug}`" class="small-card-title">
        {{ name }}
      </router-link>
      <router-link :to="`/t/${team}/${game}/${slug}/edit`" class="link">
        ( edit )
      </router-link>
    </div>
    <div>
      <div v-if="added">
        <h5>Added</h5>
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

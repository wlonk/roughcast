<template>
  <div v-if="versions" class="edit-box" id="history">
    <div>
      <div class="box-title">
        <h5>Version history</h5>
      </div>
      <VersionHistoryCard
        v-for="version in versions"
        v-bind="version"
        :key="version.id"
      />
      <div v-if="!versions.length" class="version-card">
        <h6 class="section-title">No attached files</h6>
      </div>
    </div>
  </div>
</template>

<script>
import VersionHistoryCard from '@/components/VersionHistoryCard';

export default {
  name: 'VersionHistory',
  components: { VersionHistoryCard },
  props: {
    versions: Array,
  },
};
</script>

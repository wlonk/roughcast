<template>
  <div v-if="versions.length" class="versions-list">
    <div>
      <div class="box-title">
        <h5>Newest version</h5>
      </div>
      <RecentVersionCard v-bind="recent_version" />
    </div>
    <div>
      <div class="box-title">
        <h5>Previous versions</h5>
      </div>
      <VersionCard
        v-for="(version, i) in old_versions"
        :key="version.id"
        v-bind="version" />
    </div>
  </div>
</template>

<script>
import RecentVersionCard from '@/components/RecentVersionCard';
import VersionCard from '@/components/VersionCard';

export default {
  name: 'VersionList',
  props: {
    team: String,
    game: String,
    versions: Array,
    userCanAddVersions: Boolean,
    defaultVisibleTo: Array,
  },
  components: {
    RecentVersionCard,
    VersionCard,
  },
  computed: {
    recent_version() {
      return this.versions[0];
    },
    old_versions() {
      return this.versions.slice(1);
    },
  }
};
</script>

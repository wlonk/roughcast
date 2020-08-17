<template>
  <div>
    <VersionCard
      v-for="version in versions"
      :key="version.id"
      v-bind="version"
    />
    <div v-if="userCanAddVersions">
      <h4 class="ui horizontal divider">
        add a version
      </h4>
      <VersionForm
        :forPublisher="publisher"
        :forGame="game"
        :visibleTo="defaultVisibleTo"
      />
    </div>
  </div>
</template>

<script>
import VersionCard from '@/components/VersionCard';
import VersionForm from '@/forms/VersionForm';

export default {
  name: 'VersionList',
  props: {
    publisher: String,
    game: String,
    versions: Array,
    userCanAddVersions: Boolean,
    defaultVisibleTo: Array,
  },
  components: {
    VersionCard,
    VersionForm,
  },
};
</script>

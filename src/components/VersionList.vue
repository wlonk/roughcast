<template>
  <div>
    <VersionCard v-for="version in versions" :key="version.id" v-bind="version" />
    <div v-if="userCanAddVersions">
      <h4 class="ui horizontal divider">
        add a version
      </h4>
      <VersionForm :forGame="game" />
    </div>
  </div>
</template>

<script>
import VersionCard from '@/components/VersionCard';
import VersionForm from '@/forms/VersionForm';

export default {
  name: 'VersionList',
  props: {
    game: String,
    versions: Array,
    userCanAddVersions: Boolean,
  },
  components: {
    VersionCard,
    VersionForm,
  },
}
</script>

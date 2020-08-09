<template>
  <div>
    <VersionCard v-for="version in versions" :key="version.id" v-bind="version" />
    <VersionForm v-if="userCanAddVersions" />
  </div>
</template>

<script>
import VersionCard from '@/components/VersionCard';
import VersionForm from '@/forms/VersionForm';

export default {
  name: 'VersionList',
  props: {
    versions: Array,
    userCanAddVersions: Boolean,
  },
  components: {
    VersionCard,
    VersionForm,
  },
}
</script>

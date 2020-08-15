<template>
  <div>
    <DashBoard v-if="currentUser" />
    <div v-else>
      <h1>Welcome to Roughcast</h1>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import DashBoard from '@/components/DashBoard';

export default {
  name: 'RootPage',
  components: { DashBoard },
  computed: mapGetters(['currentUser']),
};
</script>

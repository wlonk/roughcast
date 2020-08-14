<template>
  <div>
    <DashBoard v-if="User.current" />
    <div v-else>
      <h1>Welcome to Roughcast</h1>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

import DashBoard from '@/components/DashBoard';

export default {
  name: 'RootPage',
  components: { DashBoard },
  computed: mapState(['User']),
};
</script>

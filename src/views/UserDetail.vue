<template>
  <div>
    <User v-bind="user" :isDetail="true" />
  </div>
</template>

<script>
import { mapState } from 'vuex';

import User from '@/components/User';

export default {
  name: 'UserDetail',
  components: { User },
  computed: {
    ...mapState(['User']),
    user() {
      return this.User.all[this.$route.params.id];
    },
  },
  created() {
    this.$store.dispatch('getUserById', this.$route.params.id);
  },
};
</script>

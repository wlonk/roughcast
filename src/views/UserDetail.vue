<template>
  <div>
    <UserCard v-bind="user" :isDetail="true" />
  </div>
</template>

<script>
import { mapState } from 'vuex';

import UserCard from '@/components/UserCard';

export default {
  name: 'UserDetail',
  components: { UserCard },
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

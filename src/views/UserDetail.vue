<template>
  <div>
    <UserCard v-bind="user" />
    <div class="user-elements">
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import UserCard from '@/components/UserCard';

export default {
  name: 'UserDetail',
  components: {
    UserCard
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
  created() {
    this.$store.dispatch('getUserById', this.$route.params.username);
  },
};
</script>

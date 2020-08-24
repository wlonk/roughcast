<template>
  <div>
    <UserCard v-bind="user" />
    <div class="user-elements">
      <GroupTabs :groups="groups" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import UserCard from '@/components/UserCard';
import GroupTabs from '@/components/GroupTabs';

export default {
  name: 'UserDetail',
  data() {
    return {
      groups: [
        'First group',
        'Second group',
        'Another group',
        'One more group',
        'Best group',
      ]
    }
  },
  components: {
    UserCard,
    GroupTabs,
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

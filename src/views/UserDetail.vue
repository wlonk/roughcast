<template>
  <div>
    <UserCard v-bind="user" />
    <div class="user-elements">
      <GroupTabs :groups="groups" />
      <UserGames />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import UserCard from '@/components/UserCard';
import GroupTabs from '@/components/GroupTabs';
import UserGames from '@/components/UserGames';

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
    UserGames
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

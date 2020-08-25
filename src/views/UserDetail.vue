<template>
  <div>
    <UserCard v-bind="user" />
    <div class="user-elements">
      <GroupTabs
        @chooseGroup="changeActiveGroup"
        :groups="groups"
        :chosen="chosenGroup"  />
      <UserGames :group="chosenGroup" />
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
  components: {
    UserCard,
    GroupTabs,
    UserGames
  },
  data() {
    return {
      chosenGroup: "All games",
      groups: [
        'All games',
        'First group',
        'Second group',
        'Another group',
        'One more group',
        'Best group',
        'more group',
        'One one more group',
        'one Best group',
      ],
    }
  },
  methods: {
    changeActiveGroup(group)  {
      return this.chosenGroup = group;
    }
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
  created() {
    this.$store.dispatch('getUserById', this.$route.params.username);
    this.$on('chooseGroup');
  },
};
</script>

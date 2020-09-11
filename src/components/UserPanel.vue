<template>
  <div class="user-panel">
    <router-link :to="`/u/${currentUser.username}`" class="ui link item">
      <img
        v-if="currentUser.avatar"
        :src="currentUser.avatar"
        alt="Your avatar"
      />
      <img v-else src="../assets/no-avatar.svg" alt="No avatar" />
      {{
        currentUser.first_name ? currentUser.first_name : currentUser.username
      }}
    </router-link>
    <UserControlMenu />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import UserControlMenu from '@/components/UserControlMenu';

export default {
  name: 'MainMenu',
  components: {
    UserControlMenu,
  },
  computed: mapGetters(['currentUser']),
};
</script>

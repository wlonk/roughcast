<template>
  <div class="page-header" id="page-header">
    <div class="header item">
      <img src="../assets/logo.svg" alt="logo">
      <router-link to="/" class="ui link item logo-title">
        Roughcast
      </router-link>
    </div>
    <div v-if="currentUser" class="ui right item">
      <NotificationList />
      <router-link :to="`/u/${currentUser.username}`" class="ui link item">
        @{{ currentUser.username }}
      </router-link>
      <LogOut />
    </div>
    <div v-else class="ui right item">
      <router-link to="/login" class="ui link item header-link">
        Login
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import LogIn from '@/components/LogIn';
import LogOut from '@/components/LogOut';
import NotificationList from '@/components/NotificationList';

export default {
  name: 'MainMenu',
  components: {
    LogIn,
    LogOut,
    NotificationList,
  },
  computed: mapGetters(['currentUser']),
};
</script>

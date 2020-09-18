<template>
  <div class="page-header" id="page-header">
    <div class="header item">
      <img src="../assets/logo.svg" alt="Logo" />
      <router-link to="/" class="logo-title">
        Roughcast
      </router-link>
    </div>
    <div v-if="currentUser" class="ui right item">
      <NotificationList />
      <UserPanel />
    </div>
    <div v-else class="user-preview">
      <router-link to="/login" class="ui link item header-link">
        Log In
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import NotificationList from '@/components/NotificationList';
import UserPanel from '@/components/UserPanel';

export default {
  name: 'MainMenu',
  components: {
    NotificationList,
    UserPanel,
  },
  computed: mapGetters(['currentUser']),
};
</script>

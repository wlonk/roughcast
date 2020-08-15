<template>
  <div class="ui borderless main menu">
    <div class="header item">
      <router-link to="/" class="ui link item">
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
      <LogIn />
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

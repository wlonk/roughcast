<template>
  <div id="app" class="ui raised very padded text container segment">
    <div v-if="User.current">
      Logged in as
      <router-link :to="`/u/${User.current.username}`">{{
        User.current.username
      }}</router-link>
    </div>
    <div>
      <LogIn v-if="!User.current" />
      <LogOut v-else />
    </div>
    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex';

import LogIn from '@/components/LogIn';
import LogOut from '@/components/LogOut';

export default {
  name: 'App',
  components: {
    LogIn,
    LogOut,
  },
  computed: mapState(['User']),
};
</script>

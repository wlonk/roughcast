<template>
  <div id="app" class="ui raised very padded text container segment">
    <div id="nav">
      <Breadcrumbs />
    </div>
    <div v-if="User.current">
      Logged in as
      <router-link :to="`/u/${User.current.username}`">{{
        User.current.username
      }}</router-link>
    </div>
    <div>
      <Login v-if="!User.current" />
      <Logout v-else />
    </div>
    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex';

import Login from '@/components/Login';
import Logout from '@/components/Logout';

export default {
  name: 'Home',
  components: {
    Login,
    Logout,
  },
  computed: mapState(['User']),
};
</script>

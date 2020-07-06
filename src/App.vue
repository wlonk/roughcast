<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Dashboard</router-link>
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

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

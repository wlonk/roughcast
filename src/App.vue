<template>
  <div id="app">
    <div class="ui borderless main menu">
      <div class="header item">
        <router-link to="/" class="ui link item">
          Roughcast
        </router-link>
      </div>
      <div v-if="User.current" class="ui right item">
        <router-link :to="`/u/${User.current.username}`" class="ui link item">
          @{{ User.current.username }}
        </router-link>
        <LogOut />
      </div>
      <div v-if="!User.current" class="ui right item">
        <LogIn />
      </div>
    </div>
    <div class="ui raised very padded text container segment">
      <router-view />
    </div>
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

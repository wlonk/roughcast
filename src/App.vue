<template>
  <div id="app">
    <MainMenu />
    <div class="ui text container">
      <BreadCrumbs />
    </div>
    <div class="ui raised very padded text container segment">
      <router-view />
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import BreadCrumbs from '@/components/BreadCrumbs';
import MainMenu from '@/components/MainMenu';
import { mapGetters } from 'vuex';

export default {
  name: 'App',
  components: {
    BreadCrumbs,
    MainMenu,
  },
  computed: mapGetters(['currentUser']),
  created() {
    if (this.currentUser) {
      const user = this.currentUser;
      Vue.axios.defaults.headers.common[
        'Authorization'
      ] = `Token ${user.token}`;
    }
  }
};
</script>

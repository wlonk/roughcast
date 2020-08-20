<template>
  <div id="app" data-theme="dark">
    <MainMenu />
    <div class="ui container">
      <BreadCrumbs />
    </div>
    <div class="ui container">
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
  },
};
</script>

<style lang="scss">
@import "@/styles/index.scss";
</style>

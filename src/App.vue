<template>
  <div id="app" data-theme="dark">
    <MainMenu />
    <!-- @TODO remove this when out of alpha! -->
    <AlphaWarningBanner />
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
import AlphaWarningBanner from '@/components/AlphaWarningBanner';
import { mapGetters } from 'vuex';

export default {
  name: 'App',
  components: {
    BreadCrumbs,
    MainMenu,
    AlphaWarningBanner,
  },
  computed: mapGetters(['currentUser']),
  created() {
    if (this.currentUser && this.currentUser.token) {
      const { token } = this.currentUser;
      Vue.axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    }
  },
};
</script>

<style lang="scss">
@import '@/styles/index.scss';
</style>

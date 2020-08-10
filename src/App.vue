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
import BreadCrumbs from '@/components/BreadCrumbs';
import MainMenu from '@/components/MainMenu';

export default {
  name: 'App',
  components: {
    BreadCrumbs,
    MainMenu,
  },
};
</script>

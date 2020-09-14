<template>
  <scrollactive active-class="active" class="scrolling-menu">
    <router-link to="#public" class="link scrollactive-item">
      Public information
    </router-link>
    <router-link to="#visibility" class="link scrollactive-item">
      Visibility settings
    </router-link>
    <router-link to="#history" class="link scrollactive-item">
      Versions history
    </router-link>
    <router-link to="#new-version" class="link scrollactive-item">
      Add new version
    </router-link>
    <router-link to="#delete" class="link scrollactive-item">
      Delete game
    </router-link>
  </scrollactive>
</template>

<script>
export default {
  name: 'ScrollingEditGameMenu',
};
</script>

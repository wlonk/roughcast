<template>
  <scrollactive active-class="active" class="scrolling-menu">
    <router-link to="#public" class="scrollactive-item">
      Public information
    </router-link>
    <router-link to="#visibility" class="scrollactive-item">
      Visibility settings
    </router-link>
    <router-link to="#history" class="scrollactive-item">
      Versions history
    </router-link>
    <router-link to="#new-version" class="scrollactive-item">
      Add new version
    </router-link>
    <router-link to="#delete" class="scrollactive-item">
      Delete game
    </router-link>
  </scrollactive>
</template>

<script>
export default {
  name: 'ScrollingEditGameMenu',
};
</script>

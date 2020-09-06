<template>
  <scrollactive active-class="active" class="scrolling-menu">
    <router-link to="#public" class="link scrollactive-item">
      Public information
    </router-link>
    <router-link to="#invite" class="link scrollactive-item">
      Invite user
    </router-link>
    <router-link to="#users" class="link scrollactive-item">
      Managing users
    </router-link>
    <router-link to="#new-game" class="link scrollactive-item">
      Add new game
    </router-link>
    <router-link to="#delete" class="link scrollactive-item">
      Delete team
    </router-link>
  </scrollactive>
</template>

<script>
export default {
  name: 'ScrollingEditMenu',
};
</script>

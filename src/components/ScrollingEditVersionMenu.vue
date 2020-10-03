<template>
  <scrollactive active-class="active" class="scrolling-menu">
    <router-link to="#public" class="link scrollactive-item">
      Public information
    </router-link>
    <router-link to="#delete" class="link scrollactive-item">
      Delete version
    </router-link>
  </scrollactive>
</template>

<script>
export default {
  name: 'ScrollingEditVersionMenu',
};
</script>

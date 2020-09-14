<template>
  <scrollactive active-class="active" class="scrolling-menu">
    <router-link to="#public" class="link scrollactive-item">
      Public profile
    </router-link>
    <router-link to="#account" class="link scrollactive-item">
      Account settings
    </router-link>
    <router-link to="#password-change" class="link scrollactive-item">
      Change password
    </router-link>
    <router-link to="#notifications" class="link scrollactive-item">
      Notification preferences
    </router-link>
    <router-link to="#invitations" class="link scrollactive-item">
      Invitations
    </router-link>
  </scrollactive>
</template>

<script>
export default {
  name: 'ScrollingEditUserMenu',
};
</script>

<template>
  <form @submit.stop.prevent="logout">
    <input type="submit" value="Log Out" class="accent-link" />
  </form>
</template>

<script>
export default {
  name: 'LogOut',
  methods: {
    logout() {
      this.$store.dispatch('logOut');
    },
  },
};
</script>

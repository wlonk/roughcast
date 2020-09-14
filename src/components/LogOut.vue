<template>
  <form @submit.stop.prevent="logout">
    <sui-dropdown-item>
      <input type="submit" value="Log Out" />
    </sui-dropdown-item>
  </form>
</template>

<script>
export default {
  name: 'LogOut',
  methods: {
    logout() {
      this.$store.dispatch('logOut');
      this.$router.push('/');
    },
  },
};
</script>

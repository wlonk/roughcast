<template>
  <form @submit.stop.prevent="logout" class="ui mini form">
    <input type="submit" value="log out" class="ui primary button" />
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

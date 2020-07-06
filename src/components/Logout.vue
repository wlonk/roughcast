<template>
  <form @submit.stop.prevent="logout">
    <input type="submit" value="log out" />
    <ul v-if="User.errors.non_field_errors" class="errors">
      <li v-for="(error, i) in User.errors.non_field_errors" :key="i">
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Logout',
  computed: mapState(['User']),
  methods: {
    logout() {
      this.$store.dispatch('logOut');
    },
  },
};
</script>

<style scoped>
form {
  width: 200px;
  margin: 0 auto 1rem;
  border: 2px solid grey;
  border-radius: 5px;
  -webkit-box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
  box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
}
</style>

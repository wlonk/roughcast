<template>
  <form @submit.stop.prevent="logout" class="ui mini form">
    <input type="submit" value="log out" class="ui primary button" />
    <ul v-if="User.errors.non_field_errors">
      <li v-for="(error, i) in User.errors.non_field_errors" :key="i" class="ui error message">
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'LogOut',
  computed: mapState(['User']),
  methods: {
    logout() {
      this.$store.dispatch('logOut');
    },
  },
};
</script>

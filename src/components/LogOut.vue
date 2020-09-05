<template>
  <form @submit.stop.prevent="logout">
    <input type="submit" value="Log Out" class="accent-link" />
    <ul v-if="errors.non_field_errors">
      <li
        v-for="(error, i) in errors.non_field_errors"
        :key="i"
        class="ui error message"
        >
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
export default {
  name: 'LogOut',
  data() {
    return { errors: {} };
  },
  methods: {
    async logout() {
      try {
        await api.post('/logout/');
        this.$store.dispatch('logOut');
      } catch (error) {
        this.errors = {
          non_field_errors: [
            'There was an error logging out. Please try again in a moment.',
          ],
        };
      }
    },
  },
};
</script>

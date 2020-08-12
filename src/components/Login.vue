<template>
  <form @submit.stop.prevent="login" class="ui mini form">
    <div class="ui input">
      <input name="username" placeholder="username" />
      <ul v-if="User.errors.username">
        <li
          v-for="(error, i) in User.errors.username"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="ui input">
      <input
        name="password"
        type="password"
        placeholder="password"
        class="ui input"
      />
      <ul v-if="User.errors.password">
        <li
          v-for="(error, i) in User.errors.password"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <input type="submit" value="log in" class="ui mini primary button" />
    <ul v-if="User.errors.non_field_errors">
      <li
        v-for="(error, i) in User.errors.non_field_errors"
        :key="i"
        class="ui error message"
      >
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
// TODO: This component does not display errors right if it's in the header
// bar. Maybe make it pop up as a modal, to allow better error reporting?

import { mapState } from 'vuex';

export default {
  name: 'LogIn',
  computed: mapState(['User']),
  methods: {
    async login(e) {
      const username = e.target.elements['username'].value;
      const password = e.target.elements['password'].value;
      const data = { username, password };
      await this.$store.dispatch('logIn', data);
      this.$store.dispatch('retrievePublishers');
      this.$store.dispatch('retrieveGames');
      this.$store.dispatch('retrieveVersions');
      this.$store.dispatch('retrieveAttachedFiles');
    },
  },
};
</script>

<template>
  <form @submit.stop.prevent="login" class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" name="username" placeholder="Username" id="username" />
      <ul v-if="loginErrors.username">
        <li
          v-for="(error, i) in loginErrors.username"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div>
      <label for="password">Password</label>
      <input
        name="password"
        type="password"
        id="password"
        placeholder="Password"
        class="ui input"
      />
      <ul v-if="loginErrors.password">
        <li
          v-for="(error, i) in loginErrors.password"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="check-row row">
      <label for="checkbox" class="checkbox-label">
        <input type="checkbox" id="checkbox" checked="true"/>
        <p>Remember me</p>
      </label>
      <router-link to="/auth/reset" class="accent-link link">
        Forgot password?
      </router-link>
    </div>
    <div class="submit-row row">
      <input type="submit" value="Log In" class="submit-btn" />
      <p> Don’t have an account?
        <router-link to="/auth/signup" class="accent-link link">
          Sign Up!
        </router-link>
      </p>
      <ul v-if="loginErrors.non_field_errors">
        <li
          v-for="(error, i) in loginErrors.non_field_errors"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
  </form>
</template>

<script>
// TODO: This component does not display errors right if it's in the header
// bar. Maybe make it pop up as a modal, to allow better error reporting?

import { mapGetters } from 'vuex';

export default {
  name: 'LogIn',
  computed: mapGetters(['loginErrors']),
  methods: {
    async login(e) {
      const username = e.target.elements['username'].value;
      const password = e.target.elements['password'].value;
      const data = { username, password };
      try {
        await this.$store.dispatch('logIn', data);
      } catch {
        return;
      }
      this.$store.dispatch('retrievePublishers');
      this.$store.dispatch('retrieveGames');
      this.$store.dispatch('retrieveVersions');
      this.$store.dispatch('retrieveAttachedFiles');
    },
  },
};
</script>

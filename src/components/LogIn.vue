<template>
  <form @submit.stop.prevent="login" class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" name="username" placeholder="Username" id="username" />
      <ul v-if="errors.username">
        <li
          v-for="(error, i) in errors.username"
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
      <ul v-if="errors.password">
        <li
          v-for="(error, i) in errors.password"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="check-row">
      <label for="checkbox" class="checkbox-label inline">
        <input
          type="checkbox"
          id="checkbox"
          checked="true"
          disabled="disabled"
        />
        <p>Remember me</p>
      </label>
      <router-link to="/reset" class="accent-link link">
        Forgot password?
      </router-link>
    </div>
    <div class="submit-row">
      <input
        :disabled="submitting"
        type="submit"
        value="Log In"
        class="submit-btn"
      />
      <p>
        Don’t have an account?
        <router-link to="/signup" class="accent-link link">
          Sign Up!
        </router-link>
      </p>
      <ul v-if="errors.non_field_errors">
        <li
          v-for="(error, i) in errors.non_field_errors"
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
export default {
  name: 'LogIn',
  data() {
    return { errors: {}, submitting: false };
  },
  methods: {
    async login(e) {
      this.submitting = true;
      this.errors = {};
      const username = e.target.elements['username'].value;
      const password = e.target.elements['password'].value;
      const data = { username, password };
      try {
        const response = await this.$http.post('accounts/login/', data);
        await this.$store.dispatch('setCurrentUser', response.data);
      } catch (error) {
        this.submitting = false;
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {
            non_field_errors: ['There was error communicating with the server'],
          };
        }
        return;
      }
      this.submitting = false;
      this.$router.push('/');
      this.$store.dispatch('retrieveTeams');
      this.$store.dispatch('retrieveGames');
      this.$store.dispatch('retrieveVersions');
      this.$store.dispatch('retrieveAttachedFiles');
    },
  },
};
</script>

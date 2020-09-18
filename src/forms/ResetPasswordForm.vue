<template>
  <form @submit.stop.prevent="requestPasswordReset" class="page-form">
    <div>
      <label for="email">Enter your mail</label>
      <input
        type="email"
        name="email"
        placeholder="example@mail.com"
        id="email"
      />
      <ul v-if="errors.email">
        <li
          v-for="(error, i) in errors.email"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div v-if="successMessage" class="accent-link">{{ successMessage }}</div>
    <div class="submit-row">
      <input type="submit" value="Reset password" class="submit-btn" />
      <p>
        Back to
        <router-link to="/login" class="accent-link">
          Log In
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
  name: 'ResetPasswordForm',
  data() {
    return {
      errors: {},
      successMessage: null,
    };
  },
  methods: {
    async requestPasswordReset(e) {
      const email = e.target.elements['email'].value;
      const data = { email };
      try {
        await this.$http.post('accounts/reset_password/', data);
        this.successMessage = 'Email sent!';
      } catch (error) {
        // TODO: Actually display errors in the form!
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {
            non_field_errors: [
              'There was an error communicating with the server',
            ],
          };
        }
      }
    },
  },
};
</script>

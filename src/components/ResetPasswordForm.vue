<template>
  <form @submit.stop.prevent="requestPasswordReset" class="page-form">
    <div>
      <label for="email">Enter your mail</label>
      <input type="email" name="email" placeholder="example@mail.com" id="email" />
    </div>
    <div class="submit-row row">
      <input type="submit" value="Reset password" class="submit-btn" />
      <p> Back to
        <router-link to="/login" class="accent-link">
          Log In
        </router-link>
      </p>
    </div>
  </form>
</template>

<script>
export default {
  name: 'ResetPasswordForm',
  data() {
    return {errors: {}};
  },
  methods: {
    async requestPasswordReset(e) {
      const email = e.target.elements['email'].value;
      const data = { email };
      try {
        const response = await this.$http.post('user/reset_password/', data);
        // TODO: show "thanks, we sent it!"
      } catch (error) {
        // TODO: Actually display errors in the form!
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {non_field_errors: ['There was an error communicating with the server']};
        }
      }
    },
  },
};
</script>

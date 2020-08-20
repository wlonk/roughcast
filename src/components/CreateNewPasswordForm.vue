<template>
  <form @submit.stop.prevent="setNewPassword" class="page-form">
    <div>
      <label for="password1">Password</label>
      <input
        name="password1"
        type="password"
        id="password1"
        placeholder="Password"
        class="ui input"
      />
    </div>
    <div>
      <label for="password2">Repeat Password</label>
      <input
        name="password2"
        type="password"
        id="password2"
        placeholder="Password"
        class="ui input"
      />
    </div>
    <div class="submit-row row">
      <input type="submit" value="Reset password" class="submit-btn" />
    </div>
  </form>
</template>

<script>
export default {
  name: 'CreateNewPasswordForm',
  data() {
    return {errors: {}};
  },
  methods: {
    async setNewPassword(e) {
      const { uid, token } = this.$route.params;
      const password1 = e.target.elements['password1'].value;
      const password2 = e.target.elements['password2'].value;
      const data = { uid, token, password1, password2 };
      try {
        const response = await this.$http.post('user/reset_password_confirm/', data);
        // TODO: show "thanks, you can log in now!"
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

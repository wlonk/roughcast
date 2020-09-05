<template>
  <div class="edit-box" id="password-change">
    <form @submit.stop.prevent="submit" class="page-form">
      <div class="box-title">
        <h5>Change password</h5>
      </div>
      <input
        type="button"
        @click="requestResetLink"
        value="Request reset link"
        class="submit-btn"
      />
      <div v-if="successMessage" class="accent-link">{{ successMessage }}</div>
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
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'ChangePasswordForm',
  props: {
    edited: Boolean,
  },
  data() {
    return {
      errors: {},
      successMessage: null,
    };
  },
  computed: mapGetters(['currentUser']),
  methods: {
    async requestResetLink() {
      const email = this.currentUser.email;
      const data = { email };
      try {
        await this.$http.post('user/reset_password/', data);
        this.successMessage = 'Reset email sent.';
      } catch (error) {
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

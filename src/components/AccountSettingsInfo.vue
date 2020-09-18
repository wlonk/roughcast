<template>
  <div class="info-block">
    <div>
      <h6>Username</h6>
      <p>@{{ username }}</p>
    </div>
    <div>
      <h6>Email</h6>
      <div class="mail">
        <p>{{ email }}</p>
        <p v-if="is_email_verified">
          <i class="check circle outline icon"></i>
        </p>
        <p v-else class="verfc">(not verified)</p>
      </div>
      <a
        v-if="!is_email_verified"
        class="accent-link"
        @click.stop.prevent="requestConfirmation"
        >Request confirmation link.</a
      >
      <p v-if="sentMessage" class="accent-link">{{ sentMessage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccountSettingsInfo',
  props: {
    email: String,
    username: String,
    is_email_verified: Boolean,
  },
  data() {
    return {
      sentMessage: '',
    };
  },
  methods: {
    async requestConfirmation() {
      this.sentMessage = '';
      try {
        await this.$http.post('accounts/request_verify_email/');
      } catch (error) {
        this.sentMessage =
          'There was an error communicating with the server. Please try again later.';
      }
      this.sentMessage = 'Verification email sent.';
    },
  },
};
</script>

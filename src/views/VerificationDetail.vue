<template>
  <div class="verification-block">
    <div v-if="!shouldSendVerification">
      <h2>Welcome to Roughcast</h2>
      <img src="../assets/mailbox.svg" alt="mailbox">
      <div class="text-block">
        <p>
          <router-link :to="`/u/${currentUser.username}`" class="accent-link link">
            @{{ currentUser.username }}
          </router-link>
          , to start using Roughcast, we need to verify your email. <br>
          We’ve sent an email with a confirmation link to<br>
        </p>
        <p class="accent-link">{{currentUser.email}}</p>
      </div>
    </div>
    <div v-else-if="verificationPending">
      <h2>Verifing&hellip;</h2>
      <img src="../assets/mailbox-open.svg" alt="mailbox">
      <p>Hold on, we're verifying your email&hellip;</p>
    </div>
    <div v-else-if="errors">
      <h2>Uh oh</h2>
      <img src="../assets/mailbox-open.svg" alt="mailbox">
      <p>Something went wrong verifying your email.</p>
    </div>
    <div v-else>
      <h2>Verified!</h2>
      <img src="../assets/mailbox-open.svg" alt="mailbox">
      <p>Great! You have successfully verified your email.</p>
      <router-link to="/" class="submit-btn">
        Go to Dashboard!
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'VerificationDetail',
  computed: mapGetters(['currentUser']),
  created() {
    this.verifyKey();
  },
  data() {
    return {
      errors: null,
      shouldSendVerification: this.$route.params.key,
      verificationPending: Boolean(this.$route.params.key),
    };
  },
  methods: {
    async verifyKey() {
      const key = this.$route.params.key;
      const data = { key };
      if (!key) {
        return;
      }
      try {
        const response = await this.$http.post('user/verify_email/', data);
        this.verificationPending = false;
      } catch (error) {
        // TODO: Actually display errors in the form!
        this.verificationPending = false;
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {non_field_errors: ['There was an error communicating with the server']};
        }
      }
    }
  },
};
</script>

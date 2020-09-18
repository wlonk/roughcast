<template>
  <div class="verification-block">
    <div v-if="!shouldSendVerification">
      <h2>Welcome to Roughcast</h2>
      <img src="../assets/mailbox.svg" alt="Mailbox" />
      <div class="text-block">
        <p>
          <router-link
            :to="`/u/${currentUser.username}`"
            class="accent-link link"
          >
            @{{ currentUser.username }}
          </router-link>
          , to really start using Roughcast, we need to verify your email.
          <br />
          We’ve sent an email with a confirmation link to
        </p>
        <p class="accent-link">{{ currentUser.email }}</p>
        <p>
          Meanwhile, why not start by
        </p>
        <p>
          <br />
          <router-link
            :to="`/t/${myTeam.slug}/edit#new-game`"
            class="submit-btn"
            >adding a game?</router-link
          >
        </p>
      </div>
    </div>
    <div v-else-if="verificationPending">
      <h2>Verifing&hellip;</h2>
      <img src="../assets/mailbox-open.svg" alt="Mailbox" />
      <p>Hold on, we're verifying your email&hellip;</p>
    </div>
    <div v-else-if="errors">
      <h2>Uh oh</h2>
      <img src="../assets/mailbox-open.svg" alt="Mailbox" />
      <p>Something went wrong verifying your email.</p>
    </div>
    <div v-else>
      <h2>Verified!</h2>
      <img src="../assets/mailbox-open.svg" alt="Mailbox" />
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
  computed: {
    ...mapGetters(['currentUser', 'myTeams']),
    myTeam() {
      return this.myTeams[0];
    },
  },
  created() {
    this.verifyKey();
  },
  data() {
    return {
      // Hey Kit, don't change this to an empty object, that evaluates to true
      // in JS.
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
        await this.$http.post('accounts/verify_email/', data);
        this.verificationPending = false;
      } catch (error) {
        // TODO: Actually display errors in the form!
        this.verificationPending = false;
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

<template>
  <div class="verification-block">
    <div v-if="!currentUser.is_active">
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
    <div v-else>
      <h2>Verified!</h2>
      <img src="../assets/mailbox-open.svg" alt="mailbox">
      <p> Great! You have successfully verified your email.</p>
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
};
</script>

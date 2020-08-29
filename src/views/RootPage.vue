<template>
  <div>
    <DashBoard v-if="currentUser" />
    <div v-else class="welcome-block">
      <div>
        <h1>Welcome to Roughcast</h1>
        <p>Get the playtests you want, to make the game you envision.</p>
        <router-link to="/signup" class="submit-btn">
          Get started!
        </router-link>
      </div>
      <img src="../assets/player.svg" alt="player" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import DashBoard from '@/components/DashBoard';

export default {
  name: 'RootPage',
  components: { DashBoard },
  computed: mapGetters(['currentUser']),
};
</script>

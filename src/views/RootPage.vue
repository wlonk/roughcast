<template>
  <div>
    <DashBoard v-if="currentUser" />
    <div v-else class="initial-page">
      <div>
        <h1 class="welcome-title">Welcome to Roughcast</h1>
        <p>Get the playtests you want, to make the game you envision.</p>
        <router-link to="/signup" class="submit-btn">
          Get started!
        </router-link>
      </div>
      <img src="../assets/player.svg" alt="Player" />
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

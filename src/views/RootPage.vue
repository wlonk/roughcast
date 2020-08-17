<template>
  <div>
    <DashBoard v-if="currentUser" />
    <div v-else class="welcome-block">
      <div>
        <h1>Welcome to Roughcast</h1>
        <p>Roughcast is a tool to help tabletop game designers disseminate playtest documents, and manage conversations around those documents.</p>
        <router-link to="/auth/signup" class="submit-btn">
          Get Started!
        </router-link>
      </div>
      <img src="../assets/player.svg" alt="player">
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

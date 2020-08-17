<template>
  <div>
    <div v-if="$route.params.type==='signup'" class="welcome-block">
      <div>
        <h2>Create account</h2>
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
    <div v-if="$route.params.type==='login'" class="welcome-block">
      <div>
        <h2>Welcome back</h2>
        <LogIn />
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/LogIn';

export default {
  name: 'AuthorizationPage',
  components: { LogIn }
};
</script>

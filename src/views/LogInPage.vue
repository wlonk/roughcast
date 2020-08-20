<template>
  <div>
    <div class="auth-block">
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
  name: 'LogInPage',
  components: { LogIn }
};
</script>

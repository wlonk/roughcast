<template>
  <div>
    <div class="auth-block">
      <div>
        <h2 class="page-title">Welcome back</h2>
        <LogIn />
      </div>
      <img src="../assets/player.svg" alt="Player" />
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/LogIn';

export default {
  name: 'LogInPage',
  components: { LogIn },
};
</script>

<template>
  <div>
    <div class="auth-block">
      <div>
        <h2>Forgot password?</h2>
        <ResetPsw />
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
  </div>
</template>

<script>
import ResetPsw from '@/components/ResetPsw';

export default {
  name: 'ResetPasswordPage',
  components: { ResetPsw }
};
</script>

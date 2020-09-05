<template>
  <div>
    <div class="auth-block">
      <div>
        <h2>Forgot password?</h2>
        <ResetPasswordForm />
      </div>
      <img src="../assets/player.svg" alt="player" />
    </div>
  </div>
</template>

<script>
import ResetPasswordForm from '@/forms/ResetPasswordForm';

export default {
  name: 'ResetPasswordPage',
  components: { ResetPasswordForm },
};
</script>

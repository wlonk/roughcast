<template>
  <div>
    <div class="auth-block">
      <div>
        <h2 class="page-title">Forgot password?</h2>
        <ResetPasswordForm />
      </div>
      <img src="../assets/player.svg" alt="Player" />
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

<template>
  <div>
    <div class="auth-block">
      <div>
        <h2>Create new password</h2>
        <CreateNewPasswordForm />
      </div>
      <img src="../assets/player.svg" alt="player" />
    </div>
  </div>
</template>

<script>
import CreateNewPasswordForm from '@/components/CreateNewPasswordForm';

export default {
  name: 'SetNewPasswordPage',
  components: { CreateNewPasswordForm },
};
</script>

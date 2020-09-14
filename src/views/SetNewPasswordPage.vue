<template>
  <div>
    <div class="auth-block">
      <div>
        <h2>Create new password</h2>
        <CreateNewPasswordForm />
      </div>
      <img src="../assets/player.svg" alt="Player" />
    </div>
  </div>
</template>

<script>
import CreateNewPasswordForm from '@/forms/CreateNewPasswordForm';

export default {
  name: 'SetNewPasswordPage',
  components: { CreateNewPasswordForm },
};
</script>

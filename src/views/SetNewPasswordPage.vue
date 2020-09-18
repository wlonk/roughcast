<template>
  <div class="initial-page">
    <div>
      <h2 class="page-title">Create new password</h2>
      <CreateNewPasswordForm />
    </div>
    <img src="../assets/player.svg" alt="Player" />
  </div>
</template>

<script>
import CreateNewPasswordForm from '@/forms/CreateNewPasswordForm';

export default {
  name: 'SetNewPasswordPage',
  components: { CreateNewPasswordForm },
};
</script>

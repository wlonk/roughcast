<template>
  <div>
    <div class="auth-block">
      <div>
        <h2>Create new password</h2>
        <NewPsw />
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
  </div>
</template>

<script>
import NewPsw from '@/components/NewPsw';

export default {
  name: 'SetNewPasswordPage',
  components: { NewPsw }
};
</script>

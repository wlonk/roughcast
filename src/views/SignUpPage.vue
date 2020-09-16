<template>
  <div>
    <div class="auth-block">
      <div>
        <h2 class="page-title">Create account</h2>
        <SignUp />
      </div>
      <img src="../assets/player.svg" alt="Player" />
    </div>
  </div>
</template>

<script>
import SignUp from '@/components/SignUp';

export default {
  name: 'SignUpPage',
  components: { SignUp },
};
</script>

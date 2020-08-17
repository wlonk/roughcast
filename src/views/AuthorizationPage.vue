<template>
  <div>
    <div class="welcome-block">
      <div v-if="$route.params.type==='signup'">
        <h2>Create account</h2>
        <SignUp />
      </div>
      <div v-if="$route.params.type==='login'">
        <h2>Welcome back</h2>
        <LogIn />
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/LogIn';
import SignUp from '@/components/SignUp';

export default {
  name: 'AuthorizationPage',
  components: { LogIn, SignUp }
};
</script>

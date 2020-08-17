<template>
  <div>
    <div class="auth-block">
      <div v-if="$route.params.type==='signup'">
        <h2>Create account</h2>
        <SignUp />
      </div>
      <div v-if="$route.params.type==='login'">
        <h2>Welcome back</h2>
        <LogIn />
      </div>
      <div v-if="$route.params.type==='reset'">
        <h2>Forgot password?</h2>
        <ResetPsw />
      </div>
      <div v-if="$route.params.type==='new'">
        <h2>Create new password</h2>
        <NewPsw />
      </div>
      <img src="../assets/player.svg" alt="player">
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/LogIn';
import SignUp from '@/components/SignUp';
import ResetPsw from '@/components/ResetPsw';
import NewPsw from '@/components/NewPsw';

export default {
  name: 'AuthorizationPage',
  components: { LogIn, SignUp, ResetPsw, NewPsw }
};
</script>

<template>
  <div class="welcome-block">
    <div>
      <h1 class="welcome-title">Oooooops!</h1>
      <p>
        The page you’re looking for was not found or you don’t have access to
        it.
      </p>
      <router-link to="/" class="submit-btn">
        Go to homepage!
      </router-link>
    </div>
    <img src="../assets/404.svg" alt="Sleep dragon" />
  </div>
</template>

<script>
export default {
  name: 'NoPageNotification',
};
</script>

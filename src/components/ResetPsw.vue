<template>
  <form class="page-form">
    <div>
      <label for="email">Enter your mail</label>
      <input type="email" name="email" placeholder="example@mail.com" id="email" />
    </div>
    <div class="submit-row row">
      <input type="submit" value="Reset password" class="submit-btn" />
      <p> Back to
        <router-link to="/auth/login" class="accent-link">
          Log In
        </router-link>
      </p>
    </div>
  </form>
</template>

<script>
export default {
  name: 'ResetPsw'
};
</script>

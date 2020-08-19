<template>
  <form class="page-form">
    <div>
      <label for="password">Password</label>
      <input
        name="password"
        type="password"
        id="password"
        placeholder="Password"
        class="ui input"
      />
    </div>
    <div>
      <label for="rep-password">Repeat Password</label>
      <input
        name="password"
        type="password"
        id="rep-password"
        placeholder="Password"
        class="ui input"
      />
    </div>
    <div class="submit-row row">
      <input type="submit" value="Reset password" class="submit-btn" />
    </div>
  </form>
</template>

<script>
export default {
  name: 'CreateNewPasswordForm'
};
</script>

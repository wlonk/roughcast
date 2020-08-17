<template>
  <form class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" name="username" placeholder="Username" id="username" />
    </div>
    <div>
      <label for="email">Email</label>
      <input type="email" name="email" placeholder="example@mail.com" id="email" />
    </div>
    <div class="psw-row row">
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
    </div>
    <div class="check-row row">
      <label for="checkbox" class="checkbox-label">
        <input type="checkbox" id="checkbox" />
        <p>I agree to </p>
        <router-link to="/tos" class="accent-link">
          Terms of Service
        </router-link>
      </label>
    </div>
    <div class="submit-row row">
      <input type="submit" value="Sign Up" class="submit-btn" />
      <p> Already have an account?
        <router-link to="/auth/login" class="accent-link">
          Log In!
        </router-link>
      </p>
    </div>
  </form>
</template>

<script>
export default {
  name: 'SignUp'
};
</script>

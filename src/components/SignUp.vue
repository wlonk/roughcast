<template>
  <form @submit.stop.prevent="signup" class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" name="username" placeholder="Username" id="username" />
      <ul v-if="errors.username">
        <li
          v-for="(error, i) in errors.username"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div>
      <label for="email">Email</label>
      <input
        type="email"
        name="email"
        placeholder="example@mail.com"
        id="email"
      />
      <ul v-if="errors.email">
        <li
          v-for="(error, i) in errors.email"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="psw-row row">
      <div>
        <label for="password1">Password</label>
        <input
          name="password1"
          type="password"
          id="password1"
          placeholder="Password"
          class="ui input"
        />
        <ul v-if="errors.password1">
          <li
            v-for="(error, i) in errors.password1"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div>
        <label for="password2">Repeat Password</label>
        <input
          name="password2"
          type="password"
          id="password2"
          placeholder="Password"
          class="ui input"
        />
        <ul v-if="errors.password2">
          <li
            v-for="(error, i) in errors.password2"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
    </div>
    <div class="check-row row">
      <label for="tos" class="checkbox-label inline">
        <input type="checkbox" id="tos" name="tos" />
        <p>
          I agree to
          <router-link to="/tos" class="accent-link">
            Terms of Service
          </router-link>
        </p>
      </label>
      <ul v-if="errors.tos">
        <li v-for="(error, i) in errors.tos" :key="i" class="ui error message">
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="submit-row row">
      <input type="submit" value="Sign Up" class="submit-btn" />
      <p>
        Already have an account?
        <router-link to="/login" class="accent-link"> Log In! </router-link>
      </p>
      <ul v-if="errors.non_field_errors">
        <li
          v-for="(error, i) in errors.non_field_errors"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
    </div>
  </form>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return { errors: {} };
  },
  methods: {
    async signup(e) {
      this.errors = {};
      const username = e.target.elements['username'].value;
      const email = e.target.elements['email'].value;
      const password1 = e.target.elements['password1'].value;
      const password2 = e.target.elements['password2'].value;
      const tos = e.target.elements['tos'].checked;
      const data = { username, email, password1, password2, tos };
      // @@@ The reason I like doing this here is that it makes form error
      // handling easier; errors don't have to be kept in the store, like they
      // are for user login. But this also means that API calls leak up into
      // components, which I don't like. So I'll need to decide how to resolve
      // this conflict.
      try {
        const response = await this.$http.post('accounts/register/', data);
        await this.$store.dispatch('setCurrentUser', response.data);
        this.$router.push('/verification');
      } catch (error) {
        // TODO: Actually display errors in the form!
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {
            non_field_errors: [
              'There was an error communicating with the server',
            ],
          };
        }
      }
    },
  },
};
</script>

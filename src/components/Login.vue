<template>
  <form @submit.stop.prevent="login">
    <input name="username" placeholder="username" />
    <ul v-if="User.errors.username" class="errors">
      <li v-for="(error, i) in User.errors.username" :key="i">
        {{ error }}
      </li>
    </ul>
    <input name="password" type="password" placeholder="password" />
    <ul v-if="User.errors.password" class="errors">
      <li v-for="(error, i) in User.errors.password" :key="i">
        {{ error }}
      </li>
    </ul>
    <input type="submit" value="log in" />
    <ul v-if="User.errors.non_field_errors" class="errors">
      <li v-for="(error, i) in User.errors.non_field_errors" :key="i">
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Login',
  computed: mapState(['User']),
  methods: {
    login(e) {
      const username = e.target.elements['username'].value;
      const password = e.target.elements['password'].value;
      const data = { username, password };
      this.$store.dispatch('logIn', data);
    },
  },
};
</script>

<style scoped>
form {
  width: 200px;
  margin: 0 auto 1rem;
  border: 2px solid grey;
  border-radius: 5px;
  -webkit-box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
  box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
}
.errors {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}
</style>

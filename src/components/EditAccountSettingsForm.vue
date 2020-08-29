<template>
  <form @submit.stop.prevent="submit" class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" :value="username" placeholder="Username" id="username" disabled />
    </div>
    <div>
      <label for="email">Email</label>
      <input type="email" :value="email" placeholder="Email" id="email" disabled />
    </div>
    <div class="buttons">
      <input type="submit" class="submit-btn" value="Update settings" />
      <button class="remove" @click="cancel">Cancel</button>
    </div>
  </form>

</template>

<script>
export default {
  name: 'EditPublicProfileForm',
  props: {
    email: String,
    username: String
  },
  methods: {
    submit() {
      console.log("This should change your email or username, and set your email to unverified.");
      this.$emit('close-edit');
    },
    cancel() {
      this.$emit('close-edit');
    }
  }
};
</script>

<template>
  <form class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" :value="username" placeholder="Username" id="username" />
    </div>
    <div>
      <label for="email">Email</label>
      <input type="email" :value="email" placeholder="Email" id="email" />
    </div>
    <div class="buttons">
      <input type="submit" class="submit-btn" value="Update settings" />
      <button class="remove" v-if="edited" @click="changeParentState">Cancel</button>
    </div>
  </form>

</template>

<script>
export default {
  name: 'EditPublicProfileForm',
  props: {
    edited: Boolean,
    email: String,
    username: String
  },
  methods: {
    changeParentState: function() {
      this.$emit('created');
    }
  }
};
</script>

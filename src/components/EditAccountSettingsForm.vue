<template>
  <form class="page-form">
    <div>
      <label for="username">Username</label>
      <input type="text" value="Username" placeholder="Username" id="username" />
    </div>
    <div>
      <label for="email">Email</label>
      <input type="email" value="Email" placeholder="Email" id="email" />
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
    edited: Boolean
  },
  methods: {
    changeParentState: function() {
      this.$emit('created');
    }
  }
};
</script>

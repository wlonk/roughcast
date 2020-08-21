<template>
  <form class="page-form public">
    <div>
      <label for="first-name">First name</label>
      <input type="text" value="First Name" placeholder="First Name" id="first-name" />
    </div>
    <div>
      <label for="last-name">Last name</label>
      <input type="text" value="Last Name" placeholder="Last Name" id="last-name" />
    </div>
    <div class="bio">
      <label for="bio-info">Bio</label>
      <textarea placeholder="Bio" id="bio-info">Bio</textarea>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img src="../assets/no-avatar.svg" alt="avatar">
      <div>
        <input class="custom-file-upload" type="file" id="file-loader">
        <label  for="file-loader" class="file-loader-label"> Upload </label>
        <button class="remove">Remove</button>
      </div>
    </div>
    <div class="buttons">
      <input type="submit" class="submit-btn" value="Update profile" />
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

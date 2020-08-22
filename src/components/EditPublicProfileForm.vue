<template>
  <form class="page-form public">
    <div>
      <label for="name">Displayed name</label>
      <input v-if="name" type="text" :value="name" placeholder="Displayed Name" id="name" />
      <input v-else type="text" placeholder="Displayed Name" id="name" />
    </div>
    <div class="bio">
      <label for="bio-info">Bio</label>
      <textarea v-if="bio" placeholder="Add your bio" id="bio-info">{{ bio }}</textarea>
      <textarea v-else placeholder="Add your bio" id="bio-info" rows="5"></textarea>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img v-if="avatar" :src="avatar" alt="avatar">
      <img v-else src="../assets/no-avatar.svg" alt="avatar">
      <div>
        <input class="custom-file-upload" type="file" id="file-loader">
        <label  for="file-loader" class="file-loader-label"> Upload </label>
        <button v-if="avatar" class="remove">Remove</button>
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
    edited: Boolean,
    avatar: String,
    bio: String,
    name: String
  },
  methods: {
    changeParentState: function() {
      this.$emit('created');
    }
  },
};
</script>

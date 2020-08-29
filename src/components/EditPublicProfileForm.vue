<template>
  <form @submit.stop.prevent="submit" class="page-form public">
    <div>
      <label for="name">Display name</label>
      <input type="text" :value="name" placeholder="Display name" id="name" />
    </div>
    <div class="bio">
      <label for="bio-info">Bio</label>
      <textarea placeholder="Add your bio" id="bio-info" rows="5">{{ bio }}</textarea>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img v-if="avatar" :src="avatar" alt="avatar">
      <img v-else src="../assets/no-avatar.svg" alt="avatar">
      <div>
        <input class="custom-file-upload" type="file" id="file-loader">
        <label for="file-loader" class="file-loader-label">Upload</label>
        <button v-if="avatar" class="remove">Remove</button>
      </div>
    </div>
    <div class="buttons">
      <input type="submit" class="submit-btn" value="Update profile" />
      <button class="remove" @click="cancel">Cancel</button>
    </div>
  </form>

</template>

<script>
export default {
  name: 'EditPublicProfileForm',
  props: {
    avatar: String,
    bio: String,
    name: String,
  },
  data() {
    return { errors: null };
  },
  methods: {
    async submit(e) {
      const first_name = e.target.elements['name'].value;
      const bio = e.target.elements['bio-info'].value;
      const data = { first_name, bio };
      try {
        const response = await this.$http.patch('user/me/', data);
        this.$store.dispatch('updateDisplayName', response.data.first_name);
        this.$store.dispatch('updateBio', response.data.bio);
        this.$emit('close-edit');
      } catch (error) {
        if (error.response) {
          this.errors = error.response.data;
        } else {
          this.errors = {non_field_errors: ['There was an error communicating with the server']};
        }
      }
    },
    cancel() {
      this.$emit('close-edit');
    },
  },
};
</script>

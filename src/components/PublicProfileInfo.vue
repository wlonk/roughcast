<template>
  <div class="info-block public">
    <div>
      <h6>Display name</h6>
      <p v-if="first_name">{{ first_name }}</p>
      <p v-else class="no-data">We'll just use your username!</p>
    </div>
    <div class="bio">
      <h6>Bio</h6>
      <p v-if="bio">{{ bio }}</p>
      <p v-else class="no-data">
        Mysterious! No one knows where you come from.
      </p>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img v-if="avatar" :src="avatar" alt="avatar" />
      <img v-else src="../assets/no-avatar.svg" alt="avatar" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'PublicProfileInfo',
  props: {
    first_name: String,
    bio: String,
    avatar: String,
  },
};
</script>

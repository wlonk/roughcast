<template>
  <div class="info-block public">
    <div>
      <h6 class="section-title">Display name</h6>
      <p v-if="first_name">{{ first_name }}</p>
      <p v-else class="no-data">We'll just use your username!</p>
    </div>
    <div class="bio">
      <h6 class="section-title">Bio</h6>
      <p v-if="bio">{{ bio }}</p>
      <p v-else class="no-data">
        Mysterious! No one knows where you come from.
      </p>
    </div>
    <div class="avatar">
      <h6 class="section-title">Avatar</h6>
      <img v-if="avatar" :src="avatar" alt="Your avatar" />
      <img v-else src="../assets/no-avatar.svg" alt="No avatar" />
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

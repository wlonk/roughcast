<template>
  <div class="info-block public">
    <div>
      <h6>Displayed name</h6>
      <p v-if="get_full_name">{{ get_full_name }}</p>
      <p v-else class="no-data">There is no name.</p>
    </div>
    <div class="bio">
      <h6>Bio</h6>
      <p v-if="bio">{{ bio }}</p>
      <p v-else class="no-data">There is no bio.</p>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img v-if="avatar" :src="avatar" alt="avatar">
      <img v-else src="../assets/no-avatar.svg" alt="avatar">
    </div>
  </div>

</template>

<script>
export default {
  name: 'PublicProfileInfo',
  props: {
    get_full_name: String,
    bio: String,
    avatar: String,
  },
};
</script>

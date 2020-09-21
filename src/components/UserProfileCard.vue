<template>
  <div class="user-profile-card profile-card">
    <img v-if="avatar" :src="avatar" :alt="`${username} avatar`" />
    <img v-else src="../assets/no-avatar.svg" alt="No avatar" />
    <div>
      <div>
        <h4 class="card-title">{{ first_name }}</h4>
        <p>@{{ username }}</p>
      </div>
      <div>
        <h6 class="section-title">Bio</h6>
        <p v-if="bio">{{ bio }}</p>
        <p v-else class="no-bio">There is no user's bio yet&hellip;</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserProfileCard',
  props: {
    id: Number,
    username: String,
    avatar: String,
    first_name: String,
    bio: String,
  },
};
</script>

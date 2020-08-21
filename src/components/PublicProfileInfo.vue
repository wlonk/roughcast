<template>
  <div class="info-block public">
    <div>
      <h6>Displayed name</h6>
      <p>Name</p>
    </div>
    <div class="bio">
      <h6>Bio</h6>
      <p>Bio</p>
    </div>
    <div class="avatar">
      <h6>Avatar</h6>
      <img src="../assets/no-avatar.svg" alt="avatar">
    </div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'PublicProfileInfo',
};
</script>

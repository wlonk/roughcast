<template>
  <div>
    <div class="edit-block">
      <h2 >Edit Profile</h2>
      <div>
        <ScrollingEditMenu />
        <div>
          <div class="edit-box" id="public"></div>
          <div class="edit-box" id="account"></div>
          <div class="edit-box" id="password-change"></div>
          <div class="edit-box" id="notifications"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditMenu from '@/components/ScrollingEditMenu';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditMenu,
  },
  computed: mapGetters(['currentUser']),
};
</script>

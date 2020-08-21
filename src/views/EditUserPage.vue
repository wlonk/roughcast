<template>
  <div v-if="user">
    <div class="edit-block">
      <h2 >Edit Profile</h2>
      <div>
        <ScrollingEditMenu />
        <div>
          <PublicProfileBlock />
          <AccountSettingsBlock />
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
import PublicProfileBlock from '@/components/PublicProfileBlock';
import AccountSettingsBlock from '@/components/AccountSettingsBlock';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditMenu,
    PublicProfileBlock,
    AccountSettingsBlock,
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
};
</script>

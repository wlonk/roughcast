<template>
  <div v-if="user">
    <div class="edit-block">
      <h2 >Edit Profile</h2>
      <div>
        <ScrollingEditMenu />
        <div>
          <PublicProfileBlock />
          <AccountSettingsBlock />
          <ChangePasswordForm />
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
import ChangePasswordForm from '@/components/ChangePasswordForm';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditMenu,
    PublicProfileBlock,
    AccountSettingsBlock,
    ChangePasswordForm,
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
};
</script>

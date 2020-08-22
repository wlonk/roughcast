<template>
  <div>
    <div v-if="user" class="edit-block">
      <h2>Edit Profile</h2>
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
    <NoPageNotification v-else />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditMenu from '@/components/ScrollingEditMenu';
import PublicProfileBlock from '@/components/PublicProfileBlock';
import AccountSettingsBlock from '@/components/AccountSettingsBlock';
import ChangePasswordForm from '@/components/ChangePasswordForm';
import NoPageNotification from '@/components/NoPageNotification';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditMenu,
    PublicProfileBlock,
    AccountSettingsBlock,
    ChangePasswordForm,
    NoPageNotification
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
};
</script>

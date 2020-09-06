<template>
  <div>
    <div v-if="user" class="edit-block">
      <h2>Edit Profile</h2>
      <div>
        <ScrollingEditUserMenu />
        <div>
          <PublicProfileBlock />
          <AccountSettingsBlock />
          <ChangePasswordForm />
          <NotificationPreferences />
          <Invitations />
        </div>
      </div>
    </div>
    <NoPageNotification v-else />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditUserMenu from '@/components/ScrollingEditUserMenu';
import PublicProfileBlock from '@/components/PublicProfileBlock';
import AccountSettingsBlock from '@/components/AccountSettingsBlock';
import ChangePasswordForm from '@/forms/ChangePasswordForm';
import NotificationPreferences from '@/components/NotificationPreferences';
import Invitations from '@/components/Invitations';
import NoPageNotification from '@/components/NoPageNotification';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditUserMenu,
    PublicProfileBlock,
    AccountSettingsBlock,
    ChangePasswordForm,
    NotificationPreferences,
    NoPageNotification,
    Invitations
  },
  computed: {
    ...mapGetters(['hydratedUser']),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
  },
};
</script>

<template>
  <div>
    <div v-if="currentUser" class="edit-block">
      <h2 class="page-title">Edit Profile</h2>
      <div>
        <ScrollingEditUserMenu />
        <div>
          <PublicProfileBlock />
          <AccountSettingsBlock />
          <ChangePasswordForm />
          <NotificationPreferences />
          <InvitationList />
          <AddNewGroupForm />
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
import InvitationList from '@/components/InvitationList';
import NoPageNotification from '@/components/NoPageNotification';
import AddNewGroupForm from '@/forms/AddNewGroupForm';

export default {
  name: 'EditUserPage',
  components: {
    ScrollingEditUserMenu,
    PublicProfileBlock,
    AccountSettingsBlock,
    ChangePasswordForm,
    NotificationPreferences,
    NoPageNotification,
    InvitationList,
    AddNewGroupForm,
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
};
</script>

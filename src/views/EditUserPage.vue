<template>
  <div>
    <div v-if="user" class="edit-block">
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
    <NoPageNotification v-else />
  </div>
<<<<<<< HEAD

=======
  <div v-else class="welcome-block">
    <div>
      <h1>Oooooops!</h1>
      <p>The page you’re looking for was not found or you don’t have access to it.</p>
      <router-link to="/" class="submit-btn">
        Go to homepage!
      </router-link>
    </div>
    <img src="../assets/404.svg" alt="sleep dragon">
  </div>
>>>>>>> 1c24708b7b3f918abba1825f09202feba09e7226
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

<template>
  <div class="edit-box" id="account">
    <div class="box-title">
      <h5>Account Settings</h5>
      <i
        v-if="!edited"
        class="pencil alternate icon"
        @click="handleState"></i>
    </div>
    <AccountSettingsInfo v-if="!edited" v-bind="currentUser" />
    <EditAccountSettingsForm v-else
      @created="handleState"
      :edited="edited"
      :username="currentUser.username"
      :email="currentUser.email" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import AccountSettingsInfo from '@/components/AccountSettingsInfo';
import EditAccountSettingsForm from '@/components/EditAccountSettingsForm';

export default {
  name: 'AccountSettingsBlock',
  components: {
    AccountSettingsInfo,
    EditAccountSettingsForm
  },
  data () {
    return {
      edited: false
    }
  },
  methods: {
    handleState () {
      this.edited = !this.edited;
    }
  },
  computed: mapGetters(['currentUser']),
  created() {
    this.$on('created');
  }
};
</script>

<template>
  <div class="edit-box" id="account">
    <div class="box-title">
      <h5>Account Settings</h5>
      <i
        v-if="!editFormOpen"
        class="pencil alternate icon"
        @click="toggleEditState"
      ></i>
    </div>
    <AccountSettingsInfo v-if="!editFormOpen" v-bind="currentUser" />
    <EditAccountSettingsForm
      v-else
      @close-edit="toggleEditState"
      :username="currentUser.username"
      :email="currentUser.email"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import AccountSettingsInfo from '@/components/AccountSettingsInfo';
import EditAccountSettingsForm from '@/forms/EditAccountSettingsForm';

export default {
  name: 'AccountSettingsBlock',
  components: {
    AccountSettingsInfo,
    EditAccountSettingsForm,
  },
  data() {
    return {
      editFormOpen: false,
    };
  },
  methods: {
    toggleEditState() {
      this.editFormOpen = !this.editFormOpen;
    },
  },
  computed: mapGetters(['currentUser']),
};
</script>

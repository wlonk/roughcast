<template>
  <div class="edit-box" id="account">
    <div class="box-title">
      <h5>Account Settings</h5>
      <i
        v-if="!edited"
        class="pencil alternate icon"
        @click="handleState"></i>
    </div>
    <AccountSettingsInfo v-if="!edited" />
    <EditAccountSettingsForm v-else
      @created="handleState"
      :edited="edited" />
  </div>
</template>

<script>
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
  created() {
    this.$on('created');
  }
};
</script>

<template>
  <div class="edit-box" id="password-change">
    <form class="page-form">
      <div class="box-title">
        <h5>Change password</h5>
      </div>
      <div>
        <label for="old-psw">Old password</label>
        <input type="password" placeholder="Old password" id="old-psw" />
      </div>
      <div>
        <label for="new-psw">New password</label>
        <input type="password" placeholder="New password" id="new-psw" />
      </div>
      <div>
        <label for="cf-new-psw">Repeat new password</label>
        <input type="password" placeholder="New password" id="cf-new-psw" />
      </div>
      <input type="submit" class="submit-btn" value="Change password" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'ChangePasswordForm',
  props: {
    edited: Boolean
  },
  methods: {
    changeParentState: function() {
      this.$emit('created');
    }
  }
};
</script>

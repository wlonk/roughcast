<template>
  <div class="edit-box" id="invite">
    <div class="box-title">
      <h5>Invite user</h5>
    </div>
    <form class="page-form">
      <div>
        <label for="name">Username</label>
        <input type="text" placeholder="Enter username" id="name" />
        <ul v-if="errors.name">
          <li v-for="(error, i) in errors.name" :key="i" class="ui error message">
            {{ error }}
          </li>
        </ul>
      </div>
      <div class="buttons">
        <input type="submit" class="submit-btn no-top" value="Invite user" />
        <ul v-if="errors.non_field_errors">
          <li
            v-for="(error, i) in errors.non_field_errors"
            :key="i"
            class="ui error message">
            {{ error }}
          </li>
        </ul>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'InviteUserToTeamForm',
  data() {
    return {
      errors: {}
    }
  }
};
</script>

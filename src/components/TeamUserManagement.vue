<template>
  <div v-if="users" class="edit-box" id="users">
    <div class="box-title">
      <h5>Managing users</h5>
    </div>
    <UserManagingCard
      v-for="user in users"
      :key="user.id"
      v-bind="user" />
  </div>
</template>

<script>
import UserManagingCard from '@/components/UserManagingCard';

export default {
  name: 'TeamUserManagement',
  components: {
    UserManagingCard,
  },
  props: {
    users: Array,
  },
};
</script>

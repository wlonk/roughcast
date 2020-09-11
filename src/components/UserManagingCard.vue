<template>
  <div>
    <div class="user-manage-card">
      <img v-if="avatar" :src="avatar" :alt="`${username} avatar`" />
      <img v-else src="../assets/no-avatar.svg" alt="No avatar" />
      <div class="names">
        <h4 class="card-title">{{ first_name }}</h4>
        <p>@{{ username }}</p>
      </div>
      <div class="controls">
        <h5>{{ type || 'member' }}</h5>
        <i v-if="checkAction" class="chevron up icon active" @click="removeAction"></i>
        <i v-else class="chevron up icon" @click="changeUserType"></i>
        <i v-if="action === 'delete'" class="trash icon active" @click="removeAction"></i>
        <i v-else class="trash icon" @click="changeToDelete"></i>
      </div>
    </div>
    <div v-if="action" class="confirmation">
      <p>Are you sure you want to {{ action }}
        <span class="accent-link">@{{ username }}</span>
        ?
      </p>
      <div>
        <i class="check icon"></i>
        <i class="ban icon" @click="removeAction"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserManagingCard',
  props: {
    id: Number,
    username: String,
    avatar: String,
    first_name: String,
    type: String,
  },
  data() {
    return {
      action: null
    }
  },
  methods: {
    changeUserType() {
      return (this.type === 'owner')
        ? this.action = 'demote'
        : this.action = 'promote';
    },
    changeToDelete() {
      this.action = 'delete';
    },
    removeAction() {
      this.action = null;
    },
  },
  computed: {
    checkAction() {
      return this.action === 'promote' || this.action === 'demote'
    },
  }
};
</script>

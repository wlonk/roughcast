<template>
  <div class="invitation-card small-card">
    <span>
      Waiting for
      <span class="accent-link">
        {{ to_email }}
      </span>
      to respond
    </span>
    <div class="actions">
      <i class="ban icon" @click="rescindInvite"></i>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'PendingInvitationCard',
  props: {
    id: String,
    to_email: String,
  },
  methods: {
    ...mapActions(['deleteInvite']),
    rescindInvite() {
      this.deleteInvite(this.id);
    },
  },
};
</script>

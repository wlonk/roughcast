<template>
  <div class="invitation-card small-card">
    <span>
      <router-link :to="`/u/${sender}`" class="accent-link">
        @{{ sender }}
      </router-link>
      invites you to join
      <router-link :to="`/t/${team.slug}`" class="accent-link">
        {{ team.name }}
      </router-link>
    </span>
    <div class="actions">
      <i class="check icon" @click="doAcceptInvite"></i>
      <i class="ban icon" @click="rejectInvite"></i>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'InvitationCard',
  props: {
    id: String,
    sender: String,
    team: Object,
  },
  methods: {
    ...mapActions(['acceptInvite', 'deleteInvite']),
    doAcceptInvite() {
      this.acceptInvite(this.id);
    },
    rejectInvite() {
      this.deleteInvite(this.id);
    },
  },
};
</script>

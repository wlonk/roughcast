<template>
  <div class="edit-box" id="invitations">
    <div class="box-title">
      <h5>Invitations</h5>
    </div>
    <div v-if="invitations">
      <InvitationCard
        v-for="(invite, index) in invitations"
        :key="index"
        :sender="invite.sender_username"
        :team="invite.team"
        :team_slug="invite.team_slug"
      />
    </div>
    <div v-else>
      <h6 class="section-title">There are no pending invitations yet.</h6>
      <p>When somebody invites you, you'll see it here.</p>
    </div>
  </div>
</template>

<script>
import InvitationCard from '@/components/InvitationCard';

export default {
  name: 'Invitations',
  components: {
    InvitationCard,
  },
};
</script>

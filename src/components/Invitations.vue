<template>
  <div class="edit-box" id="invitations">
    <div class="box-title">
      <h5>Invitations</h5>
    </div>
    <div v-if="invitations.length">
      <InvitationCard
        v-for="(invite, index) in invitations"
        :key="index"
        :sender="invite.sender_username"
        :team="invite.team"
        :team_slug="invite.team_slug"
      />
    </div>
    <div v-else>
      <h6>There is no pending invitation yet.</h6>
      <p>When somebody invites you, you'll see it here.</p>
    </div>
  </div>
</template>

<script>
import InvitationCard from '@/components/InvitationCard';

export default {
  name: 'Invitations',
  data() {
    return {
      invitations: [
        {
          sender_username: 'mayzee',
          team: 'Funny Bunnies',
          team_slug: 'funny-bunny',
        },
      ],
    };
  },
  components: {
    InvitationCard,
  },
};
</script>

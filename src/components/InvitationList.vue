<template>
  <div class="edit-box" id="invitations">
    <div class="box-title">
      <h5>Invitations</h5>
    </div>
    <div v-if="myPendingInvites.length > 0">
      <InvitationCard
        v-for="invite in myPendingInvites"
        :key="invite.id"
        v-bind="invite"
      />
    </div>
    <div v-else>
      <h6 class="section-title">There are no pending invitations yet.</h6>
      <p>When somebody invites you, you'll see it here.</p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import InvitationCard from '@/components/InvitationCard';

export default {
  name: 'InvitationList',
  created() {
    this.retrieveInvites();
  },
  components: {
    InvitationCard,
  },
  computed: mapGetters(['myPendingInvites']),
  methods: mapActions(['retrieveInvites']),
};
</script>

<template>
  <div class="edit-box" id="invitations">
    <div class="box-title">
      <h5>Invitations</h5>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import InvitationCard from '@/components/InvitationCard';

export default {
  name: 'Invitations',
  components: {
    InvitationCard,
  },
};
</script>

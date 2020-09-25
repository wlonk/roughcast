<template>
  <div class="edit-box" id="invite">
    <div class="box-title">
      <h5>Invite user</h5>
    </div>
    <form class="page-form" @submit.stop.prevent="inviteUser">
      <div>
        <label for="name">Email</label>
        <input type="text" placeholder="Enter email" id="email" />
        <ul v-if="errors.email">
          <li
            v-for="(error, i) in errors.email"
            :key="i"
            class="ui error message"
          >
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
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
    </form>
    <div class="offered-invites">
      <PendingInvitationCard
        v-for="invite in myOfferedInvites"
        :key="invite.id"
        v-bind="invite"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import PendingInvitationCard from '@/components/PendingInvitationCard';

export default {
  name: 'InviteUserToTeamForm',
  components: {
    PendingInvitationCard,
  },
  props: {
    team: String,
  },
  data() {
    return {
      errors: {},
    };
  },
  created() {
    this.retrieveInvites();
  },
  computed: mapGetters(['myOfferedInvites']),
  methods: {
    ...mapActions(['retrieveInvites', 'createNewInvite']),
    async inviteUser(e) {
      this.errors = {};
      const to_email = e.target.elements['email'].value;
      const team = this.team;
      const data = { to_email, team };
      this.errors = await this.$store.dispatch('createNewInvite', data);
    },
  },
};
</script>

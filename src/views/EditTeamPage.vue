<template>
  <div>
    <div v-if="team" class="edit-block">
      <h2>Edit Team</h2>
      <div>
        <ScrollingEditTeamMenu />
        <div>
          <EditPublicTeamInfoForm
            :logo="team.logo"
            :description="team.description"
            :name="team.name"
            :slug="team.slug"
          />
          <InviteUserToTeamForm />
          <!-- User Management WIP -->
          <AddNewGameForm :forTeam="team.slug"/>
          <div class="edit-box" id="delete">
            <div class="box-title">
              <h5>Delete team</h5>
            </div>
            <!-- Delete Confirmation message WIP -->
            <button class="submit-btn single">Delete team</button>
          </div>
        </div>
      </div>
    </div>
    <NoPageNotification v-else />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditTeamMenu from '@/components/ScrollingEditTeamMenu';
import EditPublicTeamInfoForm from '@/forms/EditPublicTeamInfoForm';
import InviteUserToTeamForm from '@/forms/InviteUserToTeamForm';
import AddNewGameForm from '@/forms/AddNewGameForm';

export default {
  name: 'EditTeamPage',
  components: {
    ScrollingEditTeamMenu,
    EditPublicTeamInfoForm,
    InviteUserToTeamForm,
    AddNewGameForm
  },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team() {
      return this.hydratedTeam(this.$route.params.team);
    },
  },
};
</script>

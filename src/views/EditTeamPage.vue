<template>
  <div>
    <div v-if="team" class="edit-block">
      <h2>
        Edit
        <router-link :to="`/t/${team.slug}`" class="accent-link">
          "{{ team.name }}"
        </router-link>
      </h2>
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
          <TeamUserManagement :users="team.users"/>
          <AddNewGameForm :forTeam="team.slug" />
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
import AddNewGameForm from '@/forms/AddNewGameForm';
import InviteUserToTeamForm from '@/forms/InviteUserToTeamForm';
import TeamUserManagement from '@/components/TeamUserManagement';
import NoPageNotification from '@/components/NoPageNotification';

export default {
  name: 'EditTeamPage',
  components: {
    ScrollingEditTeamMenu,
    EditPublicTeamInfoForm,
    InviteUserToTeamForm,
    TeamUserManagement,
    AddNewGameForm,
    NoPageNotification,
  },
  computed: {
    ...mapGetters(['hydratedTeam']),
    team() {
      return this.hydratedTeam(this.$route.params.team);
    },
  },
};
</script>

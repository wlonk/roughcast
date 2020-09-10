<template>
  <div>
    <div v-if="game" class="edit-block">
      <h2>
        Edit
        <router-link :to="`/t/${teamSlug}/${game.slug}`" class="accent-link">
          "{{ game.name }}"
        </router-link>
      </h2>
      <div>
        <ScrollingEditGameMenu />
        <div>
          <EditPublicGameInfoForm
            :banner="game.banner"
            :description="game.description"
            :name="game.name"
            :slug="game.slug"
          />
          <div class="edit-box" id="visibility">
            <div class="box-title">
              <h5>Visibility settings</h5>
            </div>
            <p>
              <span class="accent-link">{{ game.name }}</span>
              is visible for
              <span class="accent-link">{{ game.visibility || 'All' }}</span>
            </p>
            <button class="submit-btn no-top">Make game team-only</button>
          </div>
          <VersionHistory :versions="game.versions" />
          <AddNewVersionForm :forTeam="teamSlug" :forGame="game.slug" />
          <div class="edit-box" id="delete">
            <div class="box-title">
              <h5>Delete game</h5>
            </div>
            <div class="confirmation">
              <p>Are you sure you want to delete
                <span class="accent-link">{{ game.name }}</span>
                ?
              </p>
              <p>You can't cancel this action.</p>
            </div>
            <button class="submit-btn single">Delete game</button>
          </div>
        </div>
      </div>
    </div>
    <NoPageNotification v-else />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditGameMenu from '@/components/ScrollingEditGameMenu';
import EditPublicGameInfoForm from '@/forms/EditPublicGameInfoForm';
import AddNewVersionForm from '@/forms/AddNewVersionForm';
import NoPageNotification from '@/components/NoPageNotification';
import VersionHistory from '@/components/VersionHistory';

export default {
  name: 'EditTeamPage',
  components: {
    ScrollingEditGameMenu,
    EditPublicGameInfoForm,
    AddNewVersionForm,
    NoPageNotification,
    VersionHistory,
  },
  computed: {
    ...mapGetters(['hydratedGame']),
    teamSlug() {
      return this.$route.params.team;
    },
    game() {
      return this.hydratedGame(this.$route.params.game);
    },
  },
};
</script>

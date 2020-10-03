<template>
  <div>
    <div v-if="game" class="edit-block">
      <h2 class="page-title">
        Edit
        <router-link :to="`/t/${teamSlug}/${game.slug}`" class="accent-link">
          "{{ game.name }}"
        </router-link>
      </h2>
      <div>
        <ScrollingEditGameMenu />
        <div>
          <EditPublicGameInfoForm v-bind="game" />
          <VersionHistory :versions="game.versions" />
          <AddNewVersionForm :forTeam="teamSlug" :forGame="game" />
          <div class="edit-box" id="delete">
            <div class="box-title">
              <h5>Delete game</h5>
            </div>
            <div class="confirmation">
              <p>
                Are you sure you want to delete
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
  name: 'EditGamePage',
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

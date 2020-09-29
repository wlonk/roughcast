<template>
  <div>
    <div v-if="version" class="edit-block">
      <h2 class="page-title">
        Edit
        <router-link :to="`/t/${teamSlug}/${game.slug}`" class="accent-link">
          "{{ game.name }}
        </router-link>
        <router-link
          :to="`/t/${teamSlug}/${game.slug}/${version.slug}`"
          class="accent-link"
        >
          @{{ version.name }}"
        </router-link>
      </h2>
      <div>
        <ScrollingEditVersionMenu />
        <div>
          <EditPublicVersionInfoForm v-bind="version" />
          <div class="edit-box" id="delete">
            <div class="box-title">
              <h5>Delete version</h5>
            </div>
            <div class="confirmation">
              <p>
                Are you sure you want to delete
                <span class="accent-link">{{ version.name }}</span>
                ?
              </p>
              <p>You can't cancel this action.</p>
            </div>
            <button class="submit-btn single">Delete version</button>
          </div>
        </div>
      </div>
    </div>
    <NoPageNotification v-else />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import ScrollingEditVersionMenu from '@/components/ScrollingEditVersionMenu';
import EditPublicVersionInfoForm from '@/forms/EditPublicVersionInfoForm';
import NoPageNotification from '@/components/NoPageNotification';

export default {
  name: 'EditTeamPage',
  components: {
    ScrollingEditVersionMenu,
    EditPublicVersionInfoForm,
    NoPageNotification,
  },
  computed: {
    ...mapGetters(['hydratedGame', 'hydratedVersion']),
    teamSlug() {
      return this.$route.params.team;
    },
    game() {
      return this.hydratedGame(this.$route.params.game);
    },
    version() {
      return this.hydratedVersion(this.$route.params.version);
    },
  },
};
</script>

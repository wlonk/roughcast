<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Profile</h5>
      <i
        v-if="!editFormOpen"
        class="pencil alternate icon"
        @click="toggleEditState"
      ></i>
    </div>
    <PublicProfileInfo v-if="!editFormOpen" v-bind="currentUser" />
    <EditPublicProfileForm
      v-else
      @close-edit="toggleEditState"
      :avatar="currentUser.avatar"
      :bio="currentUser.bio"
      :name="currentUser.first_name"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import PublicProfileInfo from '@/components/PublicProfileInfo';
import EditPublicProfileForm from '@/components/EditPublicProfileForm';

export default {
  name: 'PublicProfileBlock',
  components: {
    PublicProfileInfo,
    EditPublicProfileForm,
  },
  data() {
    return {
      editFormOpen: false,
    };
  },
  methods: {
    toggleEditState() {
      this.editFormOpen = !this.editFormOpen;
    },
  },
  computed: mapGetters(['currentUser']),
};
</script>

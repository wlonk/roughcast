<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Profile</h5>
      <i
        v-if="!edited"
        class="pencil alternate icon"
        @click="handleState"></i>
    </div>
    <PublicProfileInfo v-if="!edited" v-bind="currentUser" />
    <EditPublicProfileForm v-else
      @created="handleState"
      :edited="edited"
      :avatar="currentUser.avatar"
      :bio="currentUser.bio"
      :name="currentUser.get_full_name" />
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
    EditPublicProfileForm
  },
  data () {
    return {
      edited: false,
    }
  },
  methods: {
    handleState () {
      this.edited = !this.edited;
    },
  },
  computed: mapGetters(['currentUser']),
  created() {
    this.$on('created');
  }
};
</script>

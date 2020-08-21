<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Profile</h5>
      <i
        v-if="!edited"
        class="pencil alternate icon"
        @click="handleState"></i>
    </div>
    <PublicProfileInfo v-if="!edited" />
    <EditPublicProfileForm v-else
      @created="handleState"
      :edited="edited" />
  </div>
</template>

<script>
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
      edited: false
    }
  },
  methods: {
    handleState () {
      this.edited = !this.edited;
    }
  },
  created() {
    this.$on('created');
  }
};
</script>

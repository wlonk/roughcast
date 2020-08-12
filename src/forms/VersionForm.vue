<template>
  <form @submit.stop.prevent="createVersion" class="ui form">
    <input type="hidden" name="game" :value="game" />
    <div class="field">
      <label for="name">name</label>
      <input name="name" v-model="name" />
    </div>
    <div class="field">
      <label for="slug">slug</label>
      <input name="slug" v-model="slug" />
    </div>
    <div class="field">
      <label for="changelog">changes</label>
      <textarea name="changelog" v-model="changelog" />
    </div>
    <div class="ui checkbox field">
      <input
        type="checkbox"
        name="is_public"
        id="is_public"
        v-model="is_public"
      />
      <label for="is_public">public</label>
    </div>
    <div v-if="!is_public" class="field">
      <label for="visible_to">visible to</label>
      <sui-dropdown
        :options="users"
        v-model="visible_to"
        placeholder="Visible to"
        multiple
        search
        selection
      />
    </div>
    <div class="field">
      <input type="file" multiple name="files" />
    </div>
    <input type="submit" value="create" />
  </form>
</template>

<script>
import _ from 'lodash';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'VersionForm',
  props: {
    forGame: String,
  },
  data() {
    return {
      game: this.forGame,
      name: '',
      slug: '',
      changelog: '',
      is_public: false,
      visible_to: [],
    };
  },
  created() {
    this.$store.dispatch('retrieveUsers');
  },
  computed: {
    ...mapState(['User']),
    users() {
      return _.map(this.User.all, u => ({
        key: u.id,
        value: u.username,
        text: `${u.get_full_name} (@${u.username})`,
      }));
    },
  },
  methods: {
    ...mapActions(['createNewVersion', 'createNewAttachedFile']),
    async createVersion(e) {
      const elements = e.target.elements;
      const data = {
        game: elements['game'].value,
        name: elements['name'].value,
        slug: elements['slug'].value,
        changelog: elements['changelog'].value,
        is_public: elements['is_public'].value,
        visible_to: elements['visible_to']?.value || [],
      };
      const newVersion = await this.createNewVersion(data);
      e.target.elements['files'].files.forEach(async file => {
        const data = {
          version_id: newVersion.id,
          attached_file: file,
        };
        await this.createNewAttachedFile(data);
      });
    },
  },
};
</script>

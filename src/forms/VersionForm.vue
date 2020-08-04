<template>
  <form @submit.stop.prevent="createVersion">
    <input type="hidden" name="game" :value="game" />
    <div>
      <label for="name">name</label>
      <input name="name" v-model="name" />
    </div>
    <div>
      <label for="slug">slug</label>
      <input name="slug" v-model="slug" />
    </div>
    <div>
      <label for="changelog">changes</label>
      <textarea name="changelog" v-model="changelog" />
    </div>
    <div>
      <input type="checkbox" name="is_public" v-model="is_public">
      <label for="is_public">public</label>
    </div>
    <div v-if="!is_public">
      <label for="visible_to">visible to</label>
      <input name="visible_to" v-model="visible_to" />
    </div>
    <div>
      <input type="file" multiple name="files" />
    </div>
    <input type="submit" value="create" />
  </form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "VersionForm",
  props: {
    forGame: String,
  },
  data() {
    return {
      game: this.forGame,
      name: '',
      slug: '',
      changelog: '',
      is_public: true,
      visible_to: [],
    };
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
      e.target.elements["files"].files.forEach(async (file) => {
        const data = {
          version_id: newVersion.id,
          attached_file: file,
        };
        await this.createNewAttachedFile(data);
      });
    },
  }
}
</script>

<template>
  <form @submit.stop.prevent="createVersion" class="ui form">
    <input type="hidden" name="game" :value="game" />
    <div class="field">
      <label for="name">name</label>
      <input name="name" v-model="name" @change="updateSlug" />
    </div>
    <div class="field">
      <label for="slug">slug</label>
      <div :class="['ui', 'labeled', 'input', slugError ? 'error' : '']">
        <div class="ui label">
          roughcast.app/p/{{ forPublisher }}/{{ forGame }}/
        </div>
        <input name="slug" v-model="slug" @change="markSlugEdited" />
        <div v-if="slugError" class="ui corner label">
          <i class="asterisk icon"></i>
        </div>
      </div>
    </div>
    <div class="field">
      <label for="changelog">changes</label>
      <textarea name="changelog" v-model="changelog" />
      <div class="hint">
        You can use
        <a href="https://www.markdownguide.org/cheat-sheet/">Markdown</a>
        here.
      </div>
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
        :options="dryUserOptionList"
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
    <input class="ui button" type="submit" value="create" />
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import slugify from './slugify';

export default {
  name: 'VersionForm',
  props: {
    forPublisher: String,
    forGame: String,
    visibleTo: Array,
  },
  data() {
    return {
      game: this.forGame,
      name: '',
      slug: '',
      slugEdited: false,
      changelog: '',
      is_public: false,
      visible_to: this.visibleTo,
    };
  },
  created() {
    this.$store.dispatch('retrieveUsers');
  },
  computed: {
    ...mapGetters(['dryUserOptionList']),
  },
  asyncComputed: {
    async slugError() {
      if (!this.slug) {
        return false;
      }
      try {
        const params = {
          slug: this.slug,
          game__slug: this.forGame,
        };
        const response = await this.axios.get('/version/', { params });
        return response.ok && response.data.length > 0;
      } catch {
        return false;
      }
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
    updateSlug() {
      if (!this.slugEdited) {
        this.slug = slugify(this.name);
      }
    },
    markSlugEdited() {
      this.slugEdited = true;
    },
  },
};
</script>

<style scoped>
.ui.input.error > input,
.ui.input.error > div.ui.label {
  background-color: #fff6f6;
  border-color: #e0b4b4;
  color: #9f3a38;
  box-shadow: none;
}
.ui.input.error > div.ui.label:not(.corner) {
  border-width: 1px;
}
.hint {
  font-size: smaller;
  color: #555;
}
</style>

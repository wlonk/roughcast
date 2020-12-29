<template>
  <div class="edit-box" id="new-version">
    <div class="box-title">
      <h5>Add new version</h5>
    </div>
    <form @submit.stop.prevent="createVersion" class="page-form">
      <div>
        <label for="name">Version name</label>
        <input
          type="text"
          placeholder="Version name"
          id="name"
          v-model="name"
        />
        <ul v-if="errors.name">
          <li
            v-for="(error, i) in errors.name"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div class="bio">
        <label for="changelog">Changes</label>
        <textarea
          placeholder="Add version changes"
          id="changelog"
          v-model="changelog"
        >
        </textarea>
        <ul v-if="errors.changelog">
          <li
            v-for="(error, i) in errors.changelog"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div :class="slugError ? 'error' : ''">
        <label for="slug">Short link (slug)</label>
        <input
          type="text"
          placeholder="Enter short link"
          id="slug"
          v-model="slug"
        />
        <ul v-if="errors.slug || slugError">
          <li v-if="slugError" class="ui error message">
            This slug is in use.
          </li>
          <li
            v-for="(error, i) in errors.slug"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div>
        <label>Upload files</label>
        <div class="file-upload">
          <p>{{ fileNames }}</p>
          <input
            class="custom-file-upload"
            type="file"
            id="version-file-loader"
            ref="files"
            @change="updateFiles"
            multiple
          />
          <label for="version-file-loader" class="file-loader-label"
            >Choose files</label
          >
        </div>
        <ul v-if="errors.files">
          <li
            v-for="(error, i) in errors.files"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div class="custom-toggle">
        <input
          type="radio"
          name="visibility-new-version"
          id="private-new-version"
          class="private-input"
          :value="false"
          @click="togglePublic"
          v-model="is_public"
        />
        <label for="private-new-version">Team-only</label>
        <div class="selector" @click="togglePublic"></div>
        <input
          type="radio"
          name="visibility-new-version"
          id="public-new-version"
          class="public-input"
          :value="true"
          @click="togglePublic"
          v-model="is_public"
        />
        <label for="public-new-version">Public</label>
      </div>
      <div class="buttons">
        <input type="submit" class="submit-btn no-top" value="Add version" />
        <ul v-if="errors.non_field_errors">
          <li
            v-for="(error, i) in errors.non_field_errors"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
    </form>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapGetters, mapActions } from 'vuex';
import slugify from './slugify';

export default {
  name: 'AddNewVersionForm',
  props: {
    forTeam: String,
    forGame: Object,
  },
  data() {
    return {
      game: this.forGame.slug,
      name: '',
      slug: '',
      slugEdited: false,
      changelog: '',
      is_public: this.forGame.default_is_public,
      files: [],
      errors: {},
    };
  },
  created() {
    this.$store.dispatch('retrieveUsers');
  },
  computed: {
    ...mapGetters(['dryUserOptionList']),
    fileNames() {
      const noFiles = 'No files chosen';
      return this.files.map((f) => f.name).join(', ') || noFiles;
    },
  },
  asyncComputed: {
    async slugError() {
      if (!this.slug) {
        return false;
      }
      try {
        const params = {
          slug: this.slug,
          game__slug: this.forGame.slug,
        };
        const response = await this.$http.get('versions/', { params });
        return response.ok && response.data.length > 0;
      } catch {
        return false;
      }
    },
  },
  methods: {
    ...mapActions(['createNewVersion', 'createNewAttachedFile']),
    updateFiles() {
      this.files = Array.from(this.$refs.files.files);
    },
    async createVersion() {
      this.errors = this.checkFileUploads();
      if (!_.isEmpty(this.errors)) {
        return;
      }

      const data = {
        game: this.game,
        name: this.name,
        slug: this.slug,
        changelog: this.changelog,
        is_public: this.is_public,
      };
      const [newVersion, errors] = await this.createNewVersion(data);
      if (!_.isEmpty(errors)) {
        this.errors = errors;
        return;
      }

      this.files.forEach(async (file) => {
        const data = {
          version_id: newVersion.id,
          attached_file: file,
        };
        await this.createNewAttachedFile(data);
      });
      this.$router.push(`/t/${this.forTeam}/${this.game}/${this.slug}`);
    },
    checkFileUploads() {
      if (this.files.length < 1) {
        return { files: ['You must upload at least one file.'] };
      }
      return {};
    },
    updateSlug() {
      if (!this.slugEdited) {
        this.slug = slugify(this.name);
      }
    },
    markSlugEdited() {
      this.slugEdited = true;
    },
    togglePublic(e) {
      const id = e.target.id;
      return id
        ? (this.is_public = id === 'public-new-version')
        : (this.is_public = !this.is_public);
    },
  },
};
</script>

<template>
  <div class="edit-box" id="new-version">
    <div class="box-title">
      <h5>Add new version</h5>
    </div>
    <form @submit.stop.prevent="createVersion" class="page-form">
      <div>
        <label for="name">Version name</label>
        <input type="text" placeholder="Version name" id="name" />
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
        <textarea placeholder="Add version changes" id="changelog" rows="5">
        </textarea>
        <ul v-if="errors.desc">
          <li
            v-for="(error, i) in errors.desc"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <div>
        <label for="slug">Short link (slug)</label>
        <input type="text" placeholder="Enter short link" id="slug" />
        <ul v-if="errors.slug">
          <li
            v-for="(error, i) in errors.slug"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div>
      <!-- Custom visibility toggle WIP -->
      <div>
        <!-- <h6>Version file</h6> -->
        <!-- File upload -->
        <!-- <div>
          <input class="custom-file-upload" type="file" id="game-image-file-loader" />
          <label for="game-image-file-loader" class="file-loader-label">Upload</label>
        </div> -->
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
import { mapGetters, mapActions } from 'vuex';
import slugify from './slugify';

export default {
  name: 'AddNewVersionForm',
  props: {
    forTeam: String,
    forGame: String,
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
      errors: {},
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
        const response = await this.$http.get('versions/', { params });
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

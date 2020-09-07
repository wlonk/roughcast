<template>
  <div class="edit-box" id="new-game">
    <div class="box-title">
      <h5>Add game</h5>
    </div>
    <form @submit.stop.prevent="createGame" class="page-form public">
      <div>
        <label for="name">Team name</label>
        <input type="text" v-model="name" placeholder="Team name" id="name" />
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
      <div class="bio">
        <label for="bio-info">Description</label>
        <textarea
          placeholder="Add game description"
          id="bio-info"
          rows="5"
          v-model="description"
        >
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
      <div class="avatar">
        <h6>Game image</h6>
        <img src="../assets/no-game-image.svg" alt="no image" />
        <div>
          <input
            class="custom-file-upload"
            type="file"
            id="game-image-file-loader"
          />
          <label for="game-image-file-loader" class="file-loader-label"
            >Upload</label
          >
        </div>
      </div>
      <!-- Visibility toggle WIP -->
      <!-- <div class="field">
        <label for="default_visible_to">visible to</label>
        <sui-dropdown
          :options="dryUserOptionList"
          v-model="default_visible_to"
          placeholder="Visible to"
          multiple
          search
          selection
        />
        <ul v-if="errors.default_visible_to">
          <li
            v-for="(error, i) in errors.default_visible_to"
            :key="i"
            class="ui error message"
          >
            {{ error }}
          </li>
        </ul>
      </div> -->
      <div class="buttons">
        <input type="submit" class="submit-btn no-top" value="Create game" />
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
  name: 'AddNewGameForm',
  props: {
    forTeam: String,
  },
  data() {
    return {
      errors: {},
      team: this.forTeam,
      name: '',
      slug: '',
      slugEdited: false,
      description: '',
      default_visible_to: [],
    };
  },
  asyncComputed: {
    async slugError() {
      if (!this.slug) {
        return false;
      }
      try {
        const response = await this.$http.get(`games/${this.slug}/`);
        return response.status !== 404;
      } catch {
        return false;
      }
    },
  },
  computed: mapGetters(['dryUserOptionList']),
  methods: {
    ...mapActions(['createNewGame']),
    async createGame(e) {
      this.errors = {};
      const elements = e.target.elements;
      const data = {
        team: elements['team'].value,
        name: elements['name'].value,
        slug: elements['slug'].value,
        description: elements['description'].value,
      };
      const errors = await this.createNewGame(data);
      this.errors = errors;
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

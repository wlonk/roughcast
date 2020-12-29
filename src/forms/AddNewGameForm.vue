<template>
  <div class="edit-box" id="new-game">
    <div class="box-title">
      <h5>Add game</h5>
      <p>
        Once you've added a game, you can start adding versions to it. Each time
        you add a version, everyone subscribed to the game will get a
        notification, and be able to get the files you share with them!
      </p>
    </div>
    <form @submit.stop.prevent="createGame" class="page-form adding">
      <div>
        <label for="name">Game name</label>
        <input type="text" v-model="name" placeholder="Game name" id="name" />
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
        <label for="bio-info">Description</label>
        <textarea
          placeholder="Add game description"
          id="bio-info"
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
      <div>
        <label for="slug">Short link (slug)</label>
        <input
          type="text"
          placeholder="Enter short link"
          id="slug"
          v-model="slug"
        />
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
      <div class="custom-toggle">
        <input
          type="radio"
          name="visibility-new-version"
          id="private-new-version"
          class="private-input"
          :value="false"
          @click="togglePublic"
          v-model="default_is_public"
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
          v-model="default_is_public"
        />
        <label for="public-new-version">Public</label>
      </div>
      <div class="avatar">
        <!-- Remove until we enable this:
        <h6 class="section-title">Team image</h6>
        <img src="../assets/no-game-image.svg" alt="No image" />
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
        -->
      </div>
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
import _ from 'lodash';
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
      default_is_public: true,
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
    async createGame() {
      this.errors = {};
      const data = {
        team: this.team,
        name: this.name,
        slug: this.slug,
        description: this.description,
        default_is_public: this.default_is_public,
      };
      const errors = await this.createNewGame(data);
      this.errors = errors;
      if (_.isEmpty(errors)) {
        this.$router.push(`/t/${this.team}/${this.slug}`);
      }
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
        ? (this.default_is_public = id === 'public-new-version')
        : (this.default_is_public = !this.default_is_public);
    },
  },
};
</script>

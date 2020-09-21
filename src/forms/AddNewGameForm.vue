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
      <div class="avatar">
        <h6 class="section-title">Group image</h6>
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
      </div>
      <!-- Visibility toggle needs functionality -->
      <div class="custom-toggle">
        <input
          type="radio"
          name="visibility-new-game"
          id="private-new-game"
          class="private-input"
          value="private"
          :checked="!isChecked"
          @click="toggleCheck"
        />
        <label for="private-new-game">Team-only</label>
        <div class="selector" @click="toggleCheck"></div>
        <input
          type="radio"
          name="visibility-new-game"
          id="public-new-game"
          class="public-input"
          value="public"
          :checked="isChecked"
          @click="toggleCheck"
        />
        <label for="public-new-game">Public</label>
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
      isChecked: true,
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
    toggleCheck(e) {
      const id = e.target.id;
      return id
        ? (this.isChecked = id === 'public-new-version')
        : (this.isChecked = !this.isChecked);
    },
  },
};
</script>

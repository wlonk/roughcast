<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Information</h5>
    </div>
    <form class="page-form public" @submit.stop.prevent="edit">
      <div>
        <label for="name">Game name</label>
        <input
          type="text"
          v-model="theName"
          placeholder="Game name"
          id="name"
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
        <label for="bio-info">Description</label>
        <textarea
          placeholder="Add game description"
          id="bio-info"
          v-model="theDescription"
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
          v-model="theSlug"
          placeholder="Enter short link"
          id="slug"
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
          v-model="theDefault_is_public"
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
          v-model="theDefault_is_public"
        />
        <label for="public-new-version">Public</label>
      </div>
      <div class="avatar">
        <h6 class="section-title">Game image</h6>
        <img v-if="banner" :src="banner" :alt="`${name} banner`" />
        <img v-else src="../assets/no-game-image.svg" alt="No banner" />
        <div>
          <input class="custom-file-upload" type="file" id="file-loader" />
          <label for="file-loader" class="file-loader-label">Upload</label>
          <button v-if="banner" class="remove">Remove</button>
        </div>
      </div>
      <div class="buttons">
        <input type="submit" class="submit-btn no-top" value="Update Info" />
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
import { mapActions } from 'vuex';

export default {
  name: 'EditPublicGameInfoForm',
  props: {
    banner: String,
    description: String,
    name: String,
    slug: String,
    team: Object,
    default_is_public: Boolean,
  },
  data() {
    return {
      errors: {},
      theDescription: this.description,
      theName: this.name,
      theSlug: this.slug,
      theDefault_is_public: this.default_is_public,
    };
  },
  methods: {
    ...mapActions(['editGame']),
    async edit() {
      this.errors = {};
      const data = {
        name: this.theName,
        slug: this.theSlug,
        description: this.theDescription,
        default_is_public: this.theDefault_is_public,
      };
      const errors = await this.editGame({ slug: this.slug, data });
      this.errors = errors;
      if (_.isEmpty(errors)) {
        this.$router.push(`/t/${this.team.slug}/${this.slug}`);
      }
    },
    togglePublic(e) {
      const id = e.target.id;
      return id
        ? (this.theDefault_is_public = id === 'public-new-version')
        : (this.theDefault_is_public = !this.theDefault_is_public);
    },
  },
};
</script>

<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Information</h5>
    </div>
    <form class="page-form" @submit.stop.prevent="edit">
      <div>
        <label for="name">Version name</label>
        <input
          type="text"
          v-model="theName"
          placeholder="Version name"
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
        <label for="bio-info">Changes</label>
        <textarea
          placeholder="Add changes"
          id="bio-info"
          v-model="theChangelog"
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
          v-model="theIs_public"
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
          v-model="theIs_public"
        />
        <label for="public-new-version">Public</label>
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
  name: 'EditPublicVersionInfoForm',
  props: {
    id: String,
    changelog: String,
    name: String,
    slug: String,
    is_public: Boolean,
    game: Object,
  },
  data() {
    return {
      errors: {},
      theChangelog: this.changelog,
      theName: this.name,
      theSlug: this.slug,
      theIs_public: this.is_public,
    };
  },
  methods: {
    ...mapActions(['editVersion']),
    async edit() {
      this.errors = {};
      const data = {
        name: this.theName,
        slug: this.theSlug,
        changelog: this.theChangelog,
        is_public: this.theIs_public,
      };
      const errors = await this.editVersion({ id: this.id, data });
      this.errors = errors;
      if (_.isEmpty(errors)) {
        this.$router.push(
          `/t/${this.game.team}/${this.game.slug}/${this.slug}`,
        );
      }
    },
    togglePublic(e) {
      const id = e.target.id;
      return id
        ? (this.theIs_public = id === 'public-new-version')
        : (this.theIs_public = !this.theIs_public);
    },
  },
};
</script>

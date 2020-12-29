<template>
  <div class="edit-box" id="new-team">
    <div class="box-title">
      <h5>Create team</h5>
    </div>
    <form class="page-form adding" @submit.stop.prevent="createTeam">
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
      <div class="bio">
        <label for="bio-info">Description</label>
        <textarea
          placeholder="Add team description"
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
      <div class="avatar">
        <!-- Commented out until we enable this:
        <h6 class="section-title">Team logo</h6>
        <img src="../assets/no-team-logo.svg" alt="No team logo" />
        <div>
          <input
            class="custom-file-upload"
            type="file"
            id="team-image-file-loader"
          />
          <label for="team-image-file-loader" class="file-loader-label"
            >Upload</label
          >
        </div>
        -->
      </div>
      <div class="buttons">
        <input type="submit" class="submit-btn no-top" value="Create team" />
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
  name: 'AddNewTeamForm',
  data() {
    return {
      errors: {},
      name: '',
      slug: '',
      description: '',
    };
  },
  methods: {
    ...mapActions(['createNewTeam']),
    async createTeam() {
      this.errors = {};
      const data = {
        name: this.name,
        slug: this.slug,
        description: this.description,
      };
      const errors = await this.createNewTeam(data);
      this.errors = errors;
      if (_.isEmpty(errors)) {
        this.$router.push(`/t/${this.slug}`);
      }
    },
  },
};
</script>

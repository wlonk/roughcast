<template>
  <div class="edit-box" id="new-team">
    <div class="box-title">
      <h5>Create group</h5>
    </div>
    <form class="page-form adding">
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
        <h6 class="section-title">Group logo</h6>
        <img src="../assets/no-team-logo.svg" alt="No team logo" />
        <div>
          <input
            class="custom-file-upload"
            type="file"
            id="group-image-file-loader"
          />
          <label for="group-image-file-loader" class="file-loader-label"
            >Upload</label
          >
        </div>
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
  name: 'AddNewGroupForm',
  data() {
    return {
      errors: {},
      name: '',
      slug: '',
      description: '',
    };
  },
};
</script>

<template>
  <div class="edit-box" id="public">
    <div class="box-title">
      <h5>Public Information</h5>
    </div>
    <form class="page-form">
      <div>
        <label for="name">Version name</label>
        <input
          type="text"
          v-model="name"
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
          rows="5"
          v-model="changelog"
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
          v-model="slug"
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
export default {
  name: 'EditPublicVersionInfoForm',
  props: {
    changelog: String,
    name: String,
    slug: String,
  },
  data() {
    return {
      errors: {},
    };
  },
};
</script>

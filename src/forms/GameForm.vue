<template>
  <form @submit.stop.prevent="createGame" class="ui form">
    <input type="hidden" name="team" :value="team" />
    <div class="field">
      <label for="name">name</label>
      <input name="name" v-model="name" @change="updateSlug" />
      <ul v-if="errors.name">
        <li v-for="(error, i) in errors.name" :key="i" class="ui error message">
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="field">
      <label for="slug">slug</label>
      <div :class="['ui', 'labeled', 'input', slugError ? 'error' : '']">
        <div class="ui label">roughcast.app/t/{{ forTeam }}/</div>
        <input name="slug" v-model="slug" @change="markSlugEdited" />
        <div v-if="slugError" class="ui corner label">
          <i class="asterisk icon"></i>
        </div>
      </div>
      <ul v-if="errors.slug">
        <li v-for="(error, i) in errors.slug" :key="i" class="ui error message">
          {{ error }}
        </li>
      </ul>
    </div>
    <div class="field">
      <label for="description">description</label>
      <textarea name="description" v-model="description" />
      <ul v-if="errors.description">
        <li
          v-for="(error, i) in errors.description"
          :key="i"
          class="ui error message"
        >
          {{ error }}
        </li>
      </ul>
      <div class="hint">
        You can use
        <a href="https://www.markdownguide.org/cheat-sheet/">Markdown</a> here.
      </div>
    </div>
    <div class="field">
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
    </div>
    <input class="ui button" type="submit" value="create" />
    <ul v-if="errors.non_field_errors">
      <li
        v-for="(error, i) in errors.non_field_errors"
        :key="i"
        class="ui error message"
      >
        {{ error }}
      </li>
    </ul>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import slugify from './slugify';

export default {
  name: 'GameForm',
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
        const response = await this.$http.get(`/game/${this.slug}/`);
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

<style scoped>
.ui.input.error > input,
.ui.input.error > div.ui.label {
  background-color: #fff6f6;
  border-color: #e0b4b4;
  color: #9f3a38;
  box-shadow: none;
}
.ui.input.error > div.ui.label:not(.corner) {
  border-width: 1px;
}
.hint {
  font-size: smaller;
  color: #555;
}
</style>

<template>
  <form @submit.stop.prevent="createGame" class="ui form">
    <input type="hidden" name="publisher" :value="publisher" />
    <div>
      <label for="name">name</label>
      <input name="name" v-model="name" />
    </div>
    <div>
      <label for="slug">slug</label>
      <input name="slug" v-model="slug" />
    </div>
    <div>
      <label for="description">description</label>
      <textarea name="description" v-model="description" />
    </div>
    <input type="submit" value="create" />
  </form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'GameForm',
  props: {
    forPublisher: String,
  },
  data() {
    return {
      publisher: this.forPublisher,
      name: '',
      slug: '',
      description: '',
    };
  },
  methods: {
    ...mapActions(['createNewGame']),
    async createGame(e) {
      const elements = e.target.elements;
      const data = {
        publisher: elements['publisher'].value,
        name: elements['name'].value,
        slug: elements['slug'].value,
        description: elements['description'].value,
      };
      await this.createNewGame(data);
    },
  },
};
</script>

<template>
  <form @submit.stop.prevent="createPublisher" class="ui form">
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
    <div>
      <label for="url">url</label>
      <input name="url" v-model="url" />
    </div>
    <input type="submit" value="create" />
  </form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "PublisherForm",
  props: {
    forPublisher: String,
  },
  data() {
    return {
      name: '',
      slug: '',
      description: '',
      url: '',
    };
  },
  methods: {
    ...mapActions(['createNewPublisher']),
    async createPublisher(e) {
      const elements = e.target.elements;
      const data = {
        name: elements['name'].value,
        slug: elements['slug'].value,
        description: elements['description'].value,
        url: elements['url'].value,
      };
      await this.createNewPublisher(data);
    },
  }
}
</script>

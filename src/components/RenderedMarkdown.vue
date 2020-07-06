<template>
  <div class="body" v-html="renderedBody"></div>
</template>

<script>
import marked from 'marked';
import DOMPurify from 'dompurify';

export default {
  name: 'RenderedMarkdown',
  props: { body: String },
  computed: {
    renderedBody() {
      const dirty = marked(this.body || '');
      const clean = DOMPurify.sanitize(dirty);
      return clean;
    },
  },
};
</script>

<style scoped>
.body {
  background-color: #f0f0f0;
}
</style>

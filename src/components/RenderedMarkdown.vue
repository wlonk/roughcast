<template>
  <div class="rendered" v-html="renderedBody"></div>
</template>

<script>
import marked from 'marked';
import DOMPurify from 'dompurify';

export default {
  name: 'RenderedMarkdown',
  props: {
    body: {
      type: String,
      default: '',
    },
  },
  computed: {
    renderedBody() {
      const dirty = marked(this.body);
      const clean = DOMPurify.sanitize(dirty);
      return clean;
    },
  },
};
</script>

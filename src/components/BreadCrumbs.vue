<template>
  <div class="ui breadcrumb">
    <a class="section" to="/">home</a>
    <component
      v-for="(crumb, i) in crumbs"
      :href="crumb.path"
      :key="i"
      :is="crumb.tag"
      :class="crumb.classes"
    >{{ crumb.name }}</component>
  </div>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'BreadCrumbs',
  computed: {
    crumbs() {
      const divider = {
        path: null,
        name: ' / ',
        classes: 'divider',
        tag: 'div',
      };
      const segments = _.flatMap(this.$route.matched, (rr) => {
        const matches = rr.regex.exec(rr.path);
        const names = matches.slice(1).map((n) => n.slice(1));
        // TODO: Generate a path based on previous path components. 
        return _.flatMap(names, (n) => ([
          divider,
          {
            path: this.$route.params[n],
            name: this.$route.params[n],  // TODO: get a real name here
            classes: 'section',
            tag: 'a',
          }
        ]));
      });
      return segments;
    }
  }
}
</script>

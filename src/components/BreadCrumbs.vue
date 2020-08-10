<template>
  <div class="ui breadcrumb">
    <component
      v-for="(crumb, i) in crumbs"
      :to="crumb.path"
      :key="i"
      :is="crumb.tag"
      :class="crumb.classes"
    >{{ crumb.name }}</component>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

export default {
  name: 'BreadCrumbs',
  computed: {
    ...mapState(['User', 'Publisher', 'Game', 'Version']),
    crumbs() {
      const divider = {
        path: null,
        name: ' / ',
        classes: 'divider',
        tag: 'div',
      };
      const home = {
        path: '/',
        name: 'Home',
        classes: 'section',
        tag: 'router-link',
      };

      const segments = _.flatMap(this.$route.matched, (rr) => {
        const matches = rr.regex.exec(rr.path);
        const names = matches.slice(1).map((n) => n.slice(1));
        return _.flatMap(names, (n) => ([
          divider,
          {
            path: this.nameToPath(n, this.$route.params[n]),
            name: this.nameToObjectName(n, this.$route.params[n]),
            classes: 'section',
            tag: 'router-link',
          }
        ]));
      });
      return segments.length > 0 ? [home, ...segments] : [];
    }
  },
  methods: {
    nameToPath(name, value) {
      let game;
      switch (name) {
        case 'publisher':
          return `/p/${value}`;
        case 'game':
          game = _.find(
            this.Game.all,
            (g) => g.slug === value,
          );
          return `/p/${game.publisher}/${value}`;
        case 'version':
          const version = _.find(
            this.Version.all,
            (v) => v.slug === value,
          );
          game = _.find(
            this.Game.all,
            (g) => g.slug === version.game,
          );
          return `/p/${game.publisher}/${version.game}/${value}`;
        case 'user':
          return `/u/${value}`;
        default:
          return value;
      }
    },
    nameToObjectName(name, value) {
      switch (name) {
        case 'publisher':
          return _.find(
            this.Publisher.all,
            (p) => p.slug === value,
          ).name;
        case 'game':
          return _.find(
            this.Game.all,
            (g) => g.slug === value,
          ).name;
        case 'version':
          return _.find(
            this.Version.all,
            (v) => v.slug === value,
          ).name;
        case 'user':
          return this.User.all[value].username;
        default:
          return value;
      }
    },
  },
}
</script>

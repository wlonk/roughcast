<template>
  <div class="ui breadcrumb">
    <component
      v-for="(crumb, i) in crumbs"
      :to="crumb.path"
      :key="i"
      :is="crumb.tag"
      :class="crumb.classes"
      >{{ crumb.name }}</component
    >
  </div>
</template>

<script>
import _ from 'lodash';
import { mapGetters } from 'vuex';

export default {
  name: 'BreadCrumbs',
  computed: {
    ...mapGetters(['dryUser', 'dryTeam', 'dryGame', 'dryVersion']),
    crumbs() {
      if (!/^\/(t|u)\//.test(this.$route.path)) {
        return [];
      }
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

      const segments = _.flatMap(this.$route.matched, rr => {
        const matches = rr.regex.exec(rr.path);
        const names = matches.slice(1).map(n => n.slice(1));
        return _.flatMap(names, n => [
          divider,
          {
            path: this.nameToPath(n, this.$route.params[n]),
            name: this.nameToObjectName(n, this.$route.params[n]),
            classes: 'section',
            tag: 'router-link',
          },
        ]);
      });
      return segments.length > 0 ? [home, ...segments] : [];
    },
  },
  methods: {
    nameToPath(name, value) {
      let game;
      let version;
      switch (name) {
        case 'team':
          return `/t/${value}`;
        case 'game':
          game = this.dryGame(value);
          return `/t/${game.team}/${value}`;
        case 'version':
          version = this.dryVersion(value);
          game = this.dryGame(version.game);
          return `/t/${game.team}/${version.game}/${value}`;
        case 'username':
          return `/u/${value}`;
        default:
          return value;
      }
    },
    nameToObjectName(name, value) {
      switch (name) {
        case 'team':
          return this.dryTeam(value).name;
        case 'game':
          return this.dryGame(value).name;
        case 'version':
          return this.dryVersion(value).name;
        case 'username':
          return this.dryUser(value).username;
        default:
          return value;
      }
    },
  },
};
</script>

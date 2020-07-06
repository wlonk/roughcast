<template>
  <div class="publisher">
    <h4>
      <IconCrown v-if="isOwner" />
      <router-link :to="`/p/${slug}`">{{ name }}</router-link>
      <a v-if="url" :href="url"><IconLink /></a>
    </h4>
    <RenderedMarkdown :body="description" />
    <div v-if="isDetail">
      <Game v-for="(game, id) in games" :key="id" v-bind="game" />
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';
import IconCrown from '@/icons/Crown';
import IconLink from '@/icons/Link';
import Game from '@/components/Game';

export default {
  name: 'Publisher',
  props: {
    id: String,
    name: String,
    slug: String,
    url: String,
    description: String,
    isOwner: Boolean,
    isDetail: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    IconCrown,
    IconLink,
    RenderedMarkdown,
    Game,
  },
  computed: {
    ...mapState(['Game']),
    games() {
      return _.pickBy(this.Game.all, g => g.publisher == this.slug);
    },
  },
};
</script>

<style>
.publisher {
  max-width: 900px;
  margin: 0 auto 1rem;
  border: 2px solid grey;
  border-radius: 5px;
  -webkit-box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
  box-shadow: 0px 2px 2px 1px rgba(0, 0, 0, 0.1);
}
</style>

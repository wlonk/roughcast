<template>
  <div class="ui card">
    <div class="content">
      <i class="right floated star icon" v-if="isOwner"></i>
      <a v-if="url" :href="url"><i class="right floated linkify icon"></i></a>
      <router-link :to="`/p/${slug}`" class="header">{{ name }}</router-link>
      <div class="description">
        <RenderedMarkdown :body="description" />
      </div>
      <div v-if="isDetail">
        <Game v-for="(game, id) in games" :key="id" v-bind="game" />
        <div v-if="user_can_add_games">
          <h3 class="ui header">Add game</h3>
          <GameForm v-if="user_can_add_games" :forPublisher="slug" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import { mapState } from 'vuex';

import RenderedMarkdown from '@/components/RenderedMarkdown';
import Game from '@/components/Game';
import GameForm from '@/forms/GameForm';

export default {
  name: 'Publisher',
  props: {
    id: String,
    name: String,
    slug: String,
    url: String,
    description: String,
    user_can_add_games: Boolean,
    isOwner: Boolean,
    isDetail: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    RenderedMarkdown,
    Game,
    GameForm,
  },
  computed: {
    ...mapState(['Game']),
    games() {
      return _.pickBy(this.Game.all, g => g.publisher == this.slug);
    },
  },
};
</script>

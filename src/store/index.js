import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import User from './User';
import PublisherMembership from './PublisherMembership';
import Publisher from './Publisher';
import Game from './Game';
import Version from './Version';
import AttachedFile from './AttachedFile';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    User,
    PublisherMembership,
    Publisher,
    Game,
    Version,
    AttachedFile,
  },
  // plugins: [createPersistedState()],
});

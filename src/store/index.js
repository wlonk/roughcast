import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import User from './User';
import TeamMembership from './TeamMembership';
import Invite from './Invite';
import Team from './Team';
import Game from './Game';
import Subscription from './Subscription';
import Version from './Version';
import AttachedFile from './AttachedFile';
import Notification from './Notification';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    User,
    TeamMembership,
    Invite,
    Team,
    Game,
    Subscription,
    Version,
    AttachedFile,
    Notification,
  },
  plugins: [createPersistedState()],
});

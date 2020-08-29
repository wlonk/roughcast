import _ from 'lodash';
import Vue from 'vue';
import api from '../api';

const state = () => ({
  current: null,
  profile: null,
  loggingIn: false,
  errors: {},
  all: {},
});

const mutations = {
  logIn(state, user) {
    state.current = user;
  },
  logOut(state) {
    state.current = null;
    state.profile = null;
  },
  loggingIn(state) {
    state.loggingIn = true;
  },
  doneLoggingIn(state) {
    state.loggingIn = false;
  },
  setErrors(state, errors) {
    state.errors = errors;
  },
  setProfile(state, profile) {
    state.profile = profile;
  },
  setUsers(state, users) {
    state.all = users;
  },
  getUserById(state, user) {
    state.all = {
      ...state.all,
      [user.id]: user,
    };
  },
  updateDisplayName(state, displayName) {
    const currentUserId = state.current.id;
    state.current = {
      ...state.current,
      first_name: displayName,
    };
    state.all = {
      ...state.all,
      [currentUserId]: {
        ...state.all[currentUserId],
        first_name: displayName,
      },
    };
  },
  updateBio(state, bio) {
    const currentUserId = state.current.id;
    state.current = {
      ...state.current,
      bio,
    };
    state.all = {
      ...state.all,
      [currentUserId]: {
        ...state.all[currentUserId],
        bio,
      },
    };
  },
};

const actions = {
  async setCurrentUser({ commit }, user) {
    Vue.axios.defaults.headers.common['Authorization'] = `Token ${user.token}`;
    const response = await api.get('/user/profile/');
    commit('logIn', user);
    commit('setProfile', response.data);
  },
  async logIn({ commit }, data) {
    commit('setErrors', {});
    commit('loggingIn');
    const response = await api.post('/login/', data);
    if (response.ok) {
      const user = response.data;
      Vue.axios.defaults.headers.common[
        'Authorization'
      ] = `Token ${user.token}`;
      const profileResponse = await api.get('/user/profile/');
      commit('logIn', user);
      commit('setProfile', profileResponse.data);
    } else {
      const errors = response.data;
      console.log(errors);
      commit('setErrors', errors);
      commit('logOut');
    }
    commit('doneLoggingIn');
  },
  async logOut({ commit }) {
    const response = await api.post('/logout/');
    commit('logOut');
    if (!response.ok) {
      const errors = {
        non_field_errors: [
          'There was an error logging out. Please try again in a moment.',
        ],
      };
      commit('setErrors', errors);
    }
  },
  async retrieveUsers({ commit }) {
    const resp = await api.get('/user/');
    if (resp.ok) {
      const users = resp.data;
      const usersObj = users.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      commit('setUsers', usersObj);
    } else {
      // TODO display error
    }
  },
  async getUserById({ commit, state }, id) {
    if (state.all[id] !== undefined) {
      return;
    }
    const response = await api.get(`/user/${id}/`);
    if (response.ok) {
      const user = response.data;
      commit('getUserById', user);
    } else {
      // TODO: Display lookup error toast?
    }
  },
  updateDisplayName({ commit }, displayName) {
    commit('updateDisplayName', displayName);
  },
  updateBio({ commit }, bio) {
    commit('updateBio', bio);
  },
};

const getters = {
  currentUser: state => {
    return state.current;
  },
  profile: state => {
    return state.profile;
  },
  dryUser: state => username => {
    return _.find(state.all, u => u.username === username);
  },
  hydratedUser: state => username => {
    const user = _.find(state.all, u => u.username === username);
    return user;
  },
  loginErrors: state => {
    return state.errors;
  },
  dryUserOptionList: state => {
    return _.map(state.all, u => ({
      key: u.id,
      value: u.username,
      text: `${u.first_name} (@${u.username})`,
    }));
  },
};

const User = {
  state,
  mutations,
  actions,
  getters,
};

export default User;

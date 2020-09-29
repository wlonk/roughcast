import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setVersions(state, versions) {
    state.all = versions;
  },
  setVersionById(state, version) {
    state.all = {
      ...state.all,
      [version.id]: version,
    };
  },
};

const actions = {
  async retrieveVersions({ commit }) {
    const resp = await api.get('versions/');
    if (resp.ok) {
      const versions = resp.data;
      const versionsObj = versions.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      commit('setVersions', versionsObj);
    } else {
      // TODO display error
    }
  },
  async getVersionBySlugs({ commit }, { game, version }) {
    const params = new URLSearchParams({
      slug: version,
      game__slug: game,
    });
    const response = await api.get(`versions/?${params.toString()}`);
    if (response.ok) {
      const versions = response.data;
      if (versions.length !== 1) {
        // TODO: Display lookup error toast?
      } else {
        const version = versions[0];
        commit('setVersionById', version);
      }
    } else {
      // TODO: Display lookup error toast?
    }
  },
  async createNewVersion({ commit }, data) {
    const response = await api.post('versions/', data);
    if (response.ok) {
      const newVersion = response.data;
      commit('setVersionById', newVersion);
      return newVersion;
    } else {
      // TODO: Display lookup error toast?
    }
  },
  async editVersion({ commit }, { id, data }) {
    try {
      const response = await api.patch(`versions/${id}/`, data);
      const newVersion = response.data;
      commit('setVersionById', newVersion);
      return {};
    } catch (error) {
      if (error.response) {
        return error.response;
      } else {
        return {
          non_field_errors: ['There was error communicating with the server'],
        };
      }
    }
  },
};

const getters = {
  dryVersion: (state) => (slug) => {
    return _.find(state.all, (v) => v.slug === slug);
  },
  hydratedVersion: (state, getters, rootState) => (slug) => {
    const version = _.find(state.all, (v) => v.slug === slug);
    const game = _.find(rootState.Game.all, (g) => g.slug === version.game);
    const attachedFiles = _.filter(
      rootState.AttachedFile.all,
      (af) => af.version_id === version.id,
    );
    return {
      ...version,
      gameSlug: version.game,
      attachedFiles,
      game,
    };
  },
};

const Version = {
  state,
  mutations,
  actions,
  getters,
};

export default Version;

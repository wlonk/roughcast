import Vue from 'vue';

const Version = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setVersions(state, versions) {
      state.all = versions;
    },
    getVersionById(state, version) {
      state.all = {
        ...state.all,
        [version.id]: version,
      }
    },
  },
  actions: {
    async retrieveVersions({ commit }) {
      const resp = await fetch('/api/version/');
      if (resp.ok) {
        const versions = await resp.json();
        const versionsObj = versions.reduce((acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        }, {});
        commit('setVersions', versionsObj);
      } else {
        // TODO display error
      }
    },
    async getVersionBySlugs({ commit, state }, { game, version }) {
      const params = new URLSearchParams({
        slug: version,
        game__slug: game,
      });
      const response = await fetch(`/api/version/?${params.toString()}`);
      if (response.ok) {
        const versions = await response.json();
        if (versions.length !== 1) {
          // TODO: Display lookup error toast?
        } else {
          const version = versions[0];
          commit('getVersionById', version);
        }
      } else {
        // TODO: Display lookup error toast?
      }
    },
    async createNewVersion({ commit, state }, data) {
      const csrftoken = Vue.$cookies.get('csrftoken');
      const response = await fetch('/api/version/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const newVersion = await response.json();
        commit('getVersionById', newVersion);
        return newVersion;
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Version;

import api from '../api';

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
      };
    },
  },
  actions: {
    async retrieveVersions({ commit }) {
      const resp = await api.get('/version/');
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
      const response = await api.get(`/version/?${params.toString()}`);
      if (response.ok) {
        const versions = response.data;
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
    async createNewVersion({ commit }, data) {
      const response = await api.post('/version/', data);
      if (response.ok) {
        const newVersion = response.data;
        commit('getVersionById', newVersion);
        return newVersion;
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Version;

const Version = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setVersions(state, versions) {
      state.all = versions;
    },
    getVersionById(state, version) {
      state.all[version.id] = version;
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
    async getVersionById({ commit, state }, id) {
      if (state.all[id] !== undefined) {
        return;
      }
      const response = await fetch(`/api/version/${id}/`);
      if (response.ok) {
        const version = await response.json();
        commit('getVersionById', version);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Version;

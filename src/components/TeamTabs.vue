<template>
  <sui-dropdown
    icon="none"
    pointing="top right"
    class="dropdown-menu team-tabs"
  >
    <div class="section-title">Teams</div>
    <i class="dropdown icon"></i>
    <sui-dropdown-menu>
      <sui-dropdown-item
        v-for="team in teams"
        :key="team.slug"
        @click="() => selectTeam(team)"
      >
        {{ team.name }}
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'TeamTabs',
  data() {
    return {
      count: 0,
    };
  },
  props: {
    teams: Array,
    chosen: Object,
  },
  methods: {
    decreaseCount() {
      return (this.count = this.count - 5);
    },
    increaseCount() {
      return (this.count = this.count + 5);
    },
    selectTeam(team) {
      this.$emit('choose-team', team);
    },
  },
  computed: {
    allGames() {
      return { name: 'All games', slug: '*' };
    },
  },
};
</script>

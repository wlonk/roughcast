<template>
  <div class="team-list">
    <TeamCard v-for="team in teams" :key="team.id" v-bind="team" />
  </div>
</template>

<script>
import TeamCard from '@/components/TeamCard';

export default {
  name: 'TeamList',
  props: {
    teams: Array,
  },
  components: {
    TeamCard,
  },
};
</script>

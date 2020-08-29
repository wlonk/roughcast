<template>
  <div class="ui cards">
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

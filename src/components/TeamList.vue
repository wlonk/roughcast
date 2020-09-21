<template>
  <div class="wrapper">
    <div class="content-list">
      <TeamCard v-for="team in teams" :key="team.id" v-bind="team" />
    </div>
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

<template>
  <sui-dropdown
    icon="none"
    pointing="top right"
    class="dropdown-menu group-tabs"
  >
    <div class="section-title">Groups</div>
    <i class="dropdown icon"></i>
    <sui-dropdown-menu>
      <sui-dropdown-item
        v-for="group in groups"
        :key="group.slug"
        @click="() => selectGroup(group)"
      >
        {{ group.name }}
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'GroupTabs',
  data() {
    return {
      count: 0,
    };
  },
  props: {
    groups: Array,
    chosen: Object,
  },
  methods: {
    decreaseCount() {
      return (this.count = this.count - 5);
    },
    increaseCount() {
      return (this.count = this.count + 5);
    },
    selectGroup(group) {
      this.$emit('choose-group', group);
    },
  },
  computed: {
    allGames() {
      return { name: 'All games', slug: '*' };
    },
  },
};
</script>

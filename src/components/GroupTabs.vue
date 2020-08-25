<template>
  <div class="group-tabs">
    <div>
      <i
        v-if="count > 0"
        class="chevron left icon pagination-left"
        v-on:click="decreaseCount"></i>
    </div>
    <div class="tab-content">
      <div
        v-for="(group, index) in tabs"
        :key="index"
        v-on:click="selectGroup"
        v-bind:class="[group === chosen ? 'chosen' : '']">
         {{ group }}
      </div>
    </div>
    <div>
      <i
        v-if="rightPagination"
        class="chevron right icon pagination-right"
        v-on:click="increaseCount"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GroupTabs',
  data() {
    return {
      count: 0,
    }
  },
  props: {
    groups: Array,
    chosen: String,
  },
  methods: {
    decreaseCount() {
      return this.count = this.count - 5;
    },
    increaseCount() {
      return this.count = this.count + 5;
    },
    selectGroup(e) {
      this.$emit('chooseGroup', e.target.innerText);
    }
  },
  computed: {
    tabs() {
      return this.groups.slice(this.count, this.count + 5);
    },
    rightPagination() {
      const groupNumber = this.groups.length / 5;
      const timesNumber = this.count / 5 + 1;
      return groupNumber > timesNumber;
    },
    activeClass() {
      return (group === chosen) ? "chosen" : ""
    }
  },
};
</script>

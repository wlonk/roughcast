<template>
  <div class="group-tabs">
    <i class="chevron left icon pagination-left" v-on:click=""></i>
    <div>
      <div v-for="(group, index) in groups" :key="index">
         <p>{{ group }}</p>
      </div>
    </div>
    <i class="chevron right icon pagination-right"></i>
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
    groups: Array
  },
  methods: {
  }
};
</script>

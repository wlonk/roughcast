<template>
  <div class="states">
    <div v-if="likes">
      <i class="heart icon"></i>
      <p class="likes">{{ likes }}</p>
    </div>
    <div v-if="comments">
      <i class="comment icon"></i>
      <p class="comments">{{ comments }}</p>
    </div>
    <div v-if="subscribers">
      <i class="user icon"></i>
      <p class="subscribers">{{ subscribers }}</p>
    </div>
    <div v-if="games">
      <i class="cube icon"></i>
      <p class="games">{{ games }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardStatistic',
  props: {
    likes: String,
    comments: String,
    subscribers: String,
    games: String,
  },
};
</script>

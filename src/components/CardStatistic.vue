<template>
  <div class="states">
    <i class="heart icon"></i>
    <p class="likes">{{ likes || 0 }}</p>
    <i class="comment icon"></i>
    <p class="comments">{{ comments || 0 }}</p>
  </div>
</template>

<script>
export default {
  name: 'CardStatistic',
  props: {
    likes: Number,
    comments: Number,
  },
};
</script>

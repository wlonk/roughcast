<template>
  <div class="ui cards">
    <PublisherCard
      v-for="publisher in publishers"
      :key="publisher.id"
      v-bind="publisher"
    />
  </div>
</template>

<script>
import PublisherCard from '@/components/PublisherCard';

export default {
  name: 'PublisherList',
  props: {
    publishers: Array,
  },
  components: {
    PublisherCard,
  },
};
</script>

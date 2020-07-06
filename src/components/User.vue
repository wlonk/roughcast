<template>
  <div>
    <h4>{{ username }}</h4>
  </div>
</template>

<script>
export default {
  name: 'User',
  props: {
    id: String,
    username: String,
  },
};
</script>

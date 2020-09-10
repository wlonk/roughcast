<template>
  <div class="file-list">
    <div class="box-title">
      <h5>Attached Files</h5>
    </div>
    <div v-for="file in files" :key="file.id" class="file-card">
      <h4 class="card-title">{{ file.name }}</h4>
      <a :href="file.attached_file" class="round-link"></a>
    </div>
    <div v-if="!files.length" class="file-card">
      <h6>No attached files</h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FilesList',
  props: {
    files: Array,
  }
};
</script>

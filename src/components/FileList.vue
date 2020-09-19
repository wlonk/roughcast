<template>
  <div class="file-list">
    <div class="box-title">
      <h5>Attached Files</h5>
    </div>
    <div v-for="file in files" :key="file.id" class="file-card">
      <h6 class="smallest-title">{{ file.name }}</h6>
      <a :href="file.attached_file" class="round-link"></a>
    </div>
    <div v-if="!files.length" class="file-card">
      <h6 class="section-title">No attached files</h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FileList',
  props: {
    files: Array,
  },
};
</script>

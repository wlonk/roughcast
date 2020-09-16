<template>
  <div class="info-block">
    <div>
      <h6 class="section-title">Username</h6>
      <p>@{{ username }}</p>
    </div>
    <div>
      <h6 class="section-title">Email</h6>
      <div class="mail">
        <p>{{ email }}</p>
        <p v-if="is_verified">
          <i class="check circle outline icon"></i>
        </p>
        <p v-else class="verfc">(not verified)</p>
      </div>
      <p v-if="!is_verified" class="accent-link">Request confirmation link.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccountSettingsInfo',
  props: {
    email: String,
    username: String,
    is_verified: Boolean,
  },
};
</script>

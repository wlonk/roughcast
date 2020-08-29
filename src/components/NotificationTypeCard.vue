<template>
  <div>
    <h6>{{ name }}</h6>
    <div class="row">
      <label :for="`inapp-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`inapp-checkbox-${order}`"
          v-model="inApp"
        />
        <p>In-App</p>
      </label>
      <label
        :for="`instant-email-checkbox-${order}`"
        class="checkbox-label inline"
      >
        <input
          type="checkbox"
          :id="`instant-email-checkbox-${order}`"
          v-model="instantEmail"
        />
        <p>Instant Email</p>
      </label>
      <label
        :for="`weekly-email-checkbox-${order}`"
        class="checkbox-label inline"
      >
        <input
          type="checkbox"
          :id="`weekly-email-checkbox-${order}`"
          v-model="digestEmail"
        />
        <p>Weekly Email</p>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotificationTypeCard',
  props: {
    name: String,
    apiName: String,
    order: Number,
    notifs: Object,
  },
  data: function() {
    return {
      inApp: this.notifs.in_app,
      instantEmail: this.notifs.instant_email,
      digestEmail: this.notifs.digest_email,
    };
  },
};
</script>

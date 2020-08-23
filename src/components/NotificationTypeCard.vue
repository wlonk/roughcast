<template>
  <div>
    <h6>{{ name }}</h6>
    <div class="row">
      <label :for="`inapp-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`inapp-checkbox-${order}`"
          checked="true"/>
        <p>In-App</p>
      </label>
      <label :for="`instant-email-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`instant-email-checkbox-${order}`"
          checked="true"/>
        <p>Instant Email</p>
      </label>
      <label :for="`weekly-email-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`weekly-email-checkbox-${order}`"
          checked="true"/>
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
    order: Number
  }
};
</script>

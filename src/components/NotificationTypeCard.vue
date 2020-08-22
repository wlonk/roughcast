<template>
  <div>
    <h6>{{ name }}</h6>
    <div class="row">
      <label :for="`email-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`email-checkbox-${order}`"
          checked="true"/>
        <p>Email</p>
      </label>
      <label :for="`inapp-checkbox-${order}`" class="checkbox-label inline">
        <input
          type="checkbox"
          :id="`inapp-checkbox-${order}`"
          checked="true"/>
        <p>In-App</p>
      </label>
      <div class="custom-toggle">
        <input type="radio" class="toggle-input" :name="`frequency-${order}`" :id="`real-time-${order}`" checked>
        <label :for="`real-time-${order}`" class="toggle-label toggle-label-rt">Real-time</label>
        <input type="radio" class="toggle-input" :name="`frequency-${order}`" :id="`weekly-${order}`">
        <label :for="`weekly-${order}`" class="toggle-label toggle-label-wk">Weekly</label>
        <span class="selection-indicator"></span>
      </div>
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

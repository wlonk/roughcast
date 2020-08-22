<template>
  <div class="edit-box" id="notifications">
    <div class="box-title">
      <h5>Notification preferences</h5>
    </div>
    <NotificationTypeCard
      v-for="(item, index) in notifications"
      :name="item"
      :order="index"
      :key="index" />
  </div>
</template>

<script>
import NotificationTypeCard from '@/components/NotificationTypeCard';

export default {
  name: 'NotificationPreferences',
  data () {
    return {
      notifications: [
        "Conversation comments",
        "Mentions",
        "New versions",
        "New games",
      ]
    }
  },
  components: {
    NotificationTypeCard,
  },
};
</script>

<template>
  <div class="edit-box" id="notifications">
    <div class="box-title">
      <h5>Notification preferences</h5>
    </div>
    <NotificationTypeCard
      v-for="(item, index) in notifications"
      :name="item.name"
      :apiName="item.apiName"
      :order="index"
      :notifs="profile[`notif_${item.apiName}`]"
      :key="index"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import NotificationTypeCard from '@/components/NotificationTypeCard';

export default {
  name: 'NotificationPreferences',
  data() {
    return {
      notifications: [
        { name: 'Conversation comments', apiName: 'comments' },
        { name: 'Mentions', apiName: 'mentions' },
        { name: 'New games', apiName: 'games' },
        { name: 'New versions', apiName: 'versions' },
      ],
    };
  },
  computed: {
    ...mapGetters(['profile']),
  },
  components: {
    NotificationTypeCard,
  },
};
</script>

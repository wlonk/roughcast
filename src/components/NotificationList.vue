<template>
  <sui-dropdown
    icon="large bell"
    pointing="top right"
    labeled
    class="dropdown-menu"
  >
    <sui-label
      v-if="notificationCount > 0"
      floating
      size="mini"
      class="circular"
    >{{ notificationCount }}</sui-label>
    <sui-dropdown-menu>
      <sui-dropdown-item v-for="notification in allNotifications" :key="notification.id">
        <i v-if="notification.notification_type === 'comments'" class="comments icon"></i>
        <i v-if="notification.notification_type === 'mentions'" class="comments icon"></i>
        <i v-if="notification.notification_type === 'versions'" class="book icon"></i>
        <i v-if="notification.notification_type === 'games'" class="book icon"></i>
        <p :class="['notification-item', notification.seen_at ? '' : 'new']">
          <router-link :to="notification.path">
            {{ notification.subject }}
          </router-link>
        </p>
        <i
          class="close icon right floated"
          @click.prevent.stop="() => {markRead(notification.id)}"
        ></i>
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
import _ from 'lodash';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'NotificationList',
  created() {
    this.pollNotifications = setInterval(async () => {
      this.errors = await this.retrieveNotifications();
    }, 1000 * 60);
  },
  data() {
    return { errors: {} };
  },
  computed: {
    ...mapGetters(['allNotifications']),
    notificationCount() {
      return _.size(this.allNotifications);
    },
  },
  methods: mapActions(['retrieveNotifications', 'markRead']),
};
</script>

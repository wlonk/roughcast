<template>
  <sui-dropdown
    icon="large bell"
    pointing="top right"
    labeled
    class="dropdown-menu"
  >
    <sui-label
      v-if="unreadNotificationCount > 0"
      floating
      size="mini"
      class="circular"
      >{{ unreadNotificationCount }}</sui-label
    >
    <sui-dropdown-menu>
      <sui-dropdown-item
        v-for="notification in allNotifications"
        :key="notification.id"
      >
        <i
          v-if="notification.notification_type === 'comments'"
          class="comments icon"
        ></i>
        <i
          v-if="notification.notification_type === 'mentions'"
          class="comments icon"
        ></i>
        <i
          v-if="notification.notification_type === 'versions'"
          class="book icon"
        ></i>
        <i
          v-if="notification.notification_type === 'games'"
          class="book icon"
        ></i>
        <p :class="['notification-item', notification.seen_at ? '' : 'new']">
          <a
            @click.prevent.stop="
              () => navigateAndMarkRead(notification.id, notification.path)
            "
          >
            {{ notification.subject }}
          </a>
        </p>
        <i
          class="close icon right floated"
          @click.prevent.stop="
            () => {
              markRead(notification.id);
            }
          "
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
    unreadNotificationCount() {
      return _.filter(this.allNotifications, (n) => n.seen_at === null).length;
    },
  },
  methods: {
    ...mapActions(['retrieveNotifications', 'markRead']),
    navigateAndMarkRead(id, path) {
      this.markRead(id);
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
.notification-item.new a {
  color: rgb(251, 202, 24);
}
</style>

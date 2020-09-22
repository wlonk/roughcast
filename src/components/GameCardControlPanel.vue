<template>
  <div class="controls">
    <button
      v-if="!isSubscribed"
      class="small submit-btn"
      type="button"
      @click="doSubscribe"
    >
      follow
    </button>
    <button
      v-else
      class="subscribed-label"
      type="button"
      @click="doUnsubscribe"
    >
      unfollow
    </button>
    <router-link
      :to="`/t/${team_slug}/${slug}/edit`"
      v-if="permissions['this:edit']"
      class="accent-link"
    >
      Edit game
    </router-link>
    <router-link
      :to="`/t/${team_slug}/${slug}/edit#new-version`"
      v-if="permissions['version:add']"
      class="accent-link"
    >
      Add version
    </router-link>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'GameCardControlPanel',
  props: {
    permissions: Object,
    slug: String,
    team_slug: String,
    gameId: String,
  },
  created() {
    this.retrieveSubscriptions();
  },
  computed: {
    ...mapGetters(['getSubscriptionForInstance']),
    instance() {
      return `Game:${this.gameId}`;
    },
    subscription() {
      return this.getSubscriptionForInstance(this.instance);
    },
    isSubscribed() {
      return Boolean(this.subscription);
    },
  },
  methods: {
    ...mapActions(['retrieveSubscriptions', 'subscribe', 'unsubscribe']),
    doSubscribe() {
      this.subscribe(this.instance);
    },
    doUnsubscribe() {
      this.unsubscribe(this.subscription.id);
    },
  },
};
</script>

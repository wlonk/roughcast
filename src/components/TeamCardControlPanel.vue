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
      :to="`/t/${slug}/edit`"
      v-if="permissions['this:edit']"
      class="accent-link"
    >
      Edit Team
    </router-link>
    <router-link
      :to="`/t/${slug}/edit#new-game`"
      v-if="permissions['game:add']"
      class="accent-link"
    >
      Add Game
    </router-link>
    <div v-if="is_invited" class="invitation">
      <p>You've been invited</p>
      <button class="small submit-btn">Join team</button>
      <button class="small submit-btn">
        <i class="ban icon"></i>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'TeamCardControlPanel',
  props: {
    permissions: Object,
    slug: String,
    is_invited: Boolean,
    teamId: String,
  },
  created() {
    this.retrieveSubscriptions();
  },
  computed: {
    ...mapGetters(['getSubscriptionForInstance']),
    instance() {
      return `Team:${this.teamId}`;
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

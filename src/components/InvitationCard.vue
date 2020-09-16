<template>
  <div class="invitation-card">
    <span>
      <router-link :to="`/u/${sender}`" class="accent-link">
        @{{ sender }}
      </router-link>
      invite you to join
      <router-link :to="`/t/${team_slug}`" class="accent-link">
        {{ team }}
      </router-link>
    </span>
    <div class="actions">
      <i class="check icon"></i>
      <i class="ban icon"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InvitationCard',
  props: {
    sender: String,
    team: String,
    team_slug: String,
  },
};
</script>

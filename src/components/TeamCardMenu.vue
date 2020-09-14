<template>
  <sui-dropdown
    icon="ellipsis vertical"
    pointing="top right"
    class="dropdown-menu"
  >
    <sui-dropdown-menu>
      <router-link :to="`/t/${slug}/edit`" class="ui link item">
        <sui-dropdown-item>
          Edit team
        </sui-dropdown-item>
      </router-link>
      <router-link :to="`/t/${slug}/edit#invite`" class="ui link item">
        <sui-dropdown-item>
          Invite User
        </sui-dropdown-item>
      </router-link>
      <router-link :to="`/t/${slug}/edit#delete`" class="ui link item">
        <sui-dropdown-item>
          Delete team
        </sui-dropdown-item>
      </router-link>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'GameCardMenu',
  props: {
    slug: String,
  }
};
</script>

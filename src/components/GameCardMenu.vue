<template>
  <sui-dropdown
    icon="ellipsis vertical"
    pointing="top right"
    class="dropdown-menu"
  >
    <sui-dropdown-menu>
      <router-link :to="`/t/${team}/${slug}/edit`" class="ui link item">
        <sui-dropdown-item>
          Edit game
        </sui-dropdown-item>
      </router-link>
      <router-link :to="`/t/${team}/${slug}/edit#new-version`" class="ui link item">
        <sui-dropdown-item>
          Add New Version
        </sui-dropdown-item>
      </router-link>
      <router-link :to="`/t/${team}/${slug}/edit#delete`" class="ui link item">
        <sui-dropdown-item>
          Delete game
        </sui-dropdown-item>
      </router-link>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'GameCardMenu',
  props: {
    team: String,
    slug: String,
  }
};
</script>

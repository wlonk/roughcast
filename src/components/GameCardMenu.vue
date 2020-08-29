<template>
  <sui-dropdown
    icon="ellipsis vertical"
    pointing="top right"
    class="dropdown-menu"
  >
    <sui-dropdown-menu>
      <sui-dropdown-item>
        Edit game
      </sui-dropdown-item>
      <sui-dropdown-item>
        Add New Version
      </sui-dropdown-item>
      <sui-dropdown-item>
        Delete game
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'GameCardMenu',
};
</script>

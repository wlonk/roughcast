<template>
  <sui-dropdown
    icon="ellipsis vertical"
    pointing="top right"
    class="dropdown-menu"
  >
    <sui-dropdown-menu>
      <router-link :to="`/u/${currentUser.username}`" class="ui link item">
        <sui-dropdown-item>
          My Profile
        </sui-dropdown-item>
      </router-link>
      <router-link to="/add-new-game" class="ui link item">
        <sui-dropdown-item>
          Add New Game
        </sui-dropdown-item>
      </router-link>
      <router-link
        :to="`/u/${currentUser.username}/edit`"
        class="ui link item"
      >
        <sui-dropdown-item>
          Settings
        </sui-dropdown-item>
      </router-link>
      <LogOut />
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
import { mapGetters } from 'vuex';
import LogOut from '@/components/LogOut';

export default {
  name: 'UserControlMenu',
  components: {
    LogOut,
  },
  computed: mapGetters(['currentUser']),
};
</script>

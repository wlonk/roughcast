<template>
  <sui-dropdown
    icon="large ellipsis vertical"
    pointing="top right"
    class="dropdown-menu"
  >
    <sui-dropdown-menu>
      <sui-dropdown-item>
        <router-link :to="`/u/${currentUser.username}`" class="ui link item">
          My Profile
        </router-link>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <router-link to="/add-new-game" class="ui link item">
          Add New Game
        </router-link>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <router-link
          :to="`/u/${currentUser.username}/edit`"
          class="ui link item"
        >
          Settings
        </router-link>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <LogOut />
      </sui-dropdown-item>
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

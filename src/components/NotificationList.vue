<template>
  <sui-dropdown icon="large bell" pointing="top right" labeled class="dropdown-menu">
    <sui-label floating size="mini" class="circular">3</sui-label>
    <sui-dropdown-menu>
      <sui-dropdown-item>
        <i class="book icon"></i>
        <p class="notification-item new">Swords 'n' Blades version 2 just came out.</p>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <i class="comments icon"></i>
        <p class="notification-item">@stras just commented on Coven v0.3.6</p>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <i class="bullhorn icon"></i>
        <p class="notification-item">Roughcast will be releasing paid plans soon!</p>
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'NotificationList',
};
</script>

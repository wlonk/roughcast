<template>
  <sui-dropdown icon="large bell outline" pointing="top right" labeled>
    <sui-label color="red" floating size="mini">3</sui-label>
    <sui-dropdown-menu>
      <sui-dropdown-item>
        <strong>
          <i class="book icon"></i>
          Swords 'n' Blades version 2 just came out.
        </strong>
      </sui-dropdown-item>
      <sui-dropdown-item>
        <i class="comments icon"></i>
        @stras just commented on Coven v0.3.6
      </sui-dropdown-item>
      <sui-dropdown-item>
        <i class="bullhorn icon"></i>
        Roughcast will be releasing paid plans soon!
      </sui-dropdown-item>
    </sui-dropdown-menu>
  </sui-dropdown>
</template>

<script>
export default {
  name: 'NotificationList',
};
</script>

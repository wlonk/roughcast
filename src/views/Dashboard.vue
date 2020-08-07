<template>
  <div class="ui raised text segment">
    <h1>This is the Dashboard</h1>
    <Games />
    <Memberships />
  </div>
</template>

<script>
import Games from '@/components/Games';
import Memberships from '@/components/Memberships';

export default {
  name: 'Dashboard',
  components: {
    Games,
    Memberships,
  },
};
</script>

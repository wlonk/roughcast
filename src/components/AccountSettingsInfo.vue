<template>
  <div class="info-block">
    <div>
      <h6>Username</h6>
      <p>@Name</p>
    </div>
    <div>
      <h6>Email</h6>
      <div class="mail">
        <p>mail@mail.com</p>
        <p class="verfc">( not verified )</p>
      </div>
      <p class="accent-link">Request confirmation link.</p>
    </div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'AccountSettingsInfo',
};
</script>

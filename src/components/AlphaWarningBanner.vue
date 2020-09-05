<!-- @TODO Destroy this when out of alpha! -->
<template>
  <div class="alpha-warning-banner">
    <p>
      This is in early alpha. We're still adding features and working on design,
      and want your feedback! Please,
      <a href="mailto:kit+roughcast@transneptune.net?subject=Roughcast">
        get in touch</a
      >.
    </p>
  </div>
</template>

<script>
export default {
  name: 'AlphaWarningBanner',
};
</script>

<style lang="scss" scoped>
.alpha-warning-banner {
  background: repeating-linear-gradient(
    45deg,
    rgb(198, 102, 0),
    rgb(198, 102, 0) 10px,
    rgb(20, 20, 20) 10px,
    rgb(20, 20, 20) 20px
  );
  color: #d9ffff;
  text-shadow: 3px 0 3px #000, 0 -3px 3px #000, 0 3px 3px #000, -3px 0 3px #000;
  height: 2em;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

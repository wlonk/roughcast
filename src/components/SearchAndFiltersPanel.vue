<template>
  <div class="search-filter-panel">
    <form class="page-form">
      <input type="text" name="search" placeholder="Search" />
      <input type="submit" class="submit-btn" value="Search" />
    </form>
    <div class="filters">
      <div>
        <select id="subscription" name="subscription">
          <option value="all">All games</option>
          <option value="not-subscribed">Not subscribed</option>
          <option value="subscribed">Subscribtions</option>
          <option value="owner">Your game</option>
        </select>
      </div>
      <div>
        <select id="sort" name="sort">
          <option value="popularity-low">Most popular</option>
          <option value="popularity-high">Less popular</option>
          <option value="newest">New first</option>
          <option value="oldest">Old first</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchAndFiltersPanel',
};
</script>

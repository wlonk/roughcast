<template>
  <div class="user-elements">
    <UserProfileCard v-bind="user" />
    <div class="wrapper">
      <div>
        <div class="box-title">
          <h5>{{ chosenGroup.name }}</h5>
        </div>
        <GroupTabs
          @choose-group="changeActiveGroup"
          :groups="groups"
          :chosen="chosenGroup"
        />
      </div>
      <UserGames :games="filteredGames" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import UserProfileCard from "@/components/UserProfileCard";
import UserGames from "@/components/UserGames";
import GroupTabs from "@/components/GroupTabs";

const allGames = { name: "All games", slug: "*" };

export default {
  name: "UserDetail",
  components: {
    UserProfileCard,
    GroupTabs,
    UserGames
  },
  data() {
    return {
      chosenGroup: allGames
    };
  },
  methods: {
    changeActiveGroup(group) {
      this.chosenGroup = group;
    }
  },
  computed: {
    ...mapGetters(["hydratedUser", "myTeams", "listGames", "gamesForTeam"]),
    user() {
      return this.hydratedUser(this.$route.params.username);
    },
    groups() {
      return [
        allGames,
        ...this.myTeams.map(t => ({ name: t.name, slug: t.slug }))
      ];
    },
    filteredGames() {
      if (this.chosenGroup.slug === "*") {
        return this.listGames;
      }
      return this.gamesForTeam(this.chosenGroup.slug);
    }
  },
  created() {
    this.$store.dispatch("getUserById", this.$route.params.username);
    this.$store.dispatch("retrieveTeams");
  }
};
</script>

import Vue from 'vue';
import VueRouter from 'vue-router';

import updatePageTitle from './updatePageTitle';

import RootPage from '@/views/RootPage';
import UserDetail from '@/views/UserDetail';
import TeamDetail from '@/views/TeamDetail';
import GameDetail from '@/views/GameDetail';
import VersionDetail from '@/views/VersionDetail';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Root',
    component: RootPage,
    meta: {
      title: 'Roughcast',
    },
  },
  {
    path: '/u/:username',
    name: 'User',
    component: UserDetail,
    meta: {
      title: 'User | Roughcast',
    },
  },
  {
    path: '/t/:team',
    name: 'Team',
    component: TeamDetail,
    meta: {
      title: 'Team | Roughcast',
    },
  },
  {
    path: '/t/:team/:game',
    name: 'Game',
    component: GameDetail,
    meta: {
      title: 'Game | Roughcast',
    },
  },
  {
    path: '/t/:team/:game/:version',
    name: 'Version',
    component: VersionDetail,
    meta: {
      title: 'Version | Roughcast',
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  updatePageTitle(to, from, next);
  next();
});

export default router;

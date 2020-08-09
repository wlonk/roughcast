import Vue from 'vue';
import VueRouter from 'vue-router';

import updatePageTitle from './updatePageTitle';

import UserDetail from '@/views/UserDetail';
import PublisherDetail from '@/views/PublisherDetail';
import GameDetail from '@/views/GameDetail';
import VersionDetail from '@/views/VersionDetail';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Root',
    meta: {
      title: 'Roughcast',
    },
  },
  {
    path: '/u/:id',
    name: 'User',
    component: UserDetail,
    meta: {
      title: 'User | Roughcast',
    },
  },
  {
    path: '/p/:publisher',
    name: 'Publisher',
    component: PublisherDetail,
    meta: {
      title: 'Publisher | Roughcast',
    },
  },
  {
    path: '/p/:publisher/:game',
    name: 'Game',
    component: GameDetail,
    meta: {
      title: 'Game | Roughcast',
    },
  },
  {
    path: '/p/:publisher/:game/:version',
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

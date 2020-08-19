import Vue from 'vue';
import VueRouter from 'vue-router';

import updatePageTitle from './updatePageTitle';

import RootPage from '@/views/RootPage';
import UserDetail from '@/views/UserDetail';
import TeamDetail from '@/views/TeamDetail';
import GameDetail from '@/views/GameDetail';
import VersionDetail from '@/views/VersionDetail';
import LogInPage from '@/views/LogInPage';
import SignUpPage from '@/views/SignUpPage';
import ResetPasswordPage from '@/views/ResetPasswordPage';
import SetNewPasswordPage from '@/views/SetNewPasswordPage';
import VerificationDetail from '@/views/VerificationDetail';

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
    path: '/login',
    name: 'Log In',
    component: LogInPage,
    meta: {
      title: 'Log In | Roughcast',
    },
  },
  {
    path: '/signup',
    name: 'Sign Up',
    component: SignUpPage,
    meta: {
      title: 'Sign Up | Roughcast',
    },
  },
  {
    path: '/reset',
    name: 'Reset Password',
    component: ResetPasswordPage,
    meta: {
      title: 'Reset Password | Roughcast',
    },
  },
  {
    path: '/change',
    name: 'Change Password',
    component: SetNewPasswordPage,
    meta: {
      title: 'Change Password | Roughcast',
    },
  },
  {
    path: '/verification',
    name: 'Verification',
    component: VerificationDetail,
    meta: {
      title: 'Verification | Roughcast',
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

import Vue from 'vue';
import VueRouter from 'vue-router';

import updatePageTitle from './updatePageTitle';

import RootPage from '@/views/RootPage';
import TermsOfServicePage from '@/views/TermsOfServicePage';
import UserDetail from '@/views/UserDetail';
import TeamDetail from '@/views/TeamDetail';
import GameDetail from '@/views/GameDetail';
import VersionDetail from '@/views/VersionDetail';
import LogInPage from '@/views/LogInPage';
import SignUpPage from '@/views/SignUpPage';
import ResetPasswordPage from '@/views/ResetPasswordPage';
import SetNewPasswordPage from '@/views/SetNewPasswordPage';
import VerificationDetail from '@/views/VerificationDetail';
import EditUserPage from '@/views/EditUserPage';
import EditTeamPage from '@/views/EditTeamPage';
import EditGamePage from '@/views/EditGamePage';
import EditVersionPage from '@/views/EditVersionPage';

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
    path: '/tos',
    name: 'ToS',
    component: TermsOfServicePage,
    meta: {
      title: 'Terms of Service | Roughcast',
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
  // @@@ TODO: Maybe scope these all under `/accounts`?
  {
    path: '/reset',
    name: 'Reset Password',
    component: ResetPasswordPage,
    meta: {
      title: 'Reset Password | Roughcast',
    },
  },
  {
    path: '/change/:uid/:token',
    name: 'Change Password',
    component: SetNewPasswordPage,
    meta: {
      title: 'Change Password | Roughcast',
    },
  },
  {
    path: '/verification/:key?',
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
    path: '/u/:username/edit',
    name: 'Edit User',
    component: EditUserPage,
    meta: {
      title: 'Edit User Profile | Roughcast',
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
    path: '/t/:team/edit',
    name: 'EditTeam',
    component: EditTeamPage,
    meta: {
      title: 'Edit Team | Roughcast',
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
    path: '/t/:team/:game/edit',
    name: 'EditGame',
    component: EditGamePage,
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
  {
    path: '/t/:team/:game/:version/edit',
    name: 'EditVersion',
    component: EditVersionPage,
    meta: {
      title: 'Edit Version | Roughcast',
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

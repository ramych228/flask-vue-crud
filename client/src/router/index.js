import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import StudentsPage from "@/components/students_page/StudentsPage";
import ProjectsPage from "../components/projects_page/ProjectsPage";
import AccountPageStudent from "../components/account/AccountPageStudent";
import ExchangePage from "../components/exchange_page/ExchangePage";
import AuthPage from "../components/auth_page/LoginPage";
import LoginPage from "../components/auth_page/LoginPage";
import RegisterBlock from "../components/auth_page/RegisterBlock";
import RegisterPage from "../components/auth_page/RegisterPage";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/students',
      name: 'Students',
      component: StudentsPage,
    },
    {
      path: '/projects',
      name: 'Projects',
      component: ProjectsPage,
    },
    {
      path: '/burse',
      name: 'Burse',
      component: ExchangePage,
    },
    {
      path: '/login',
      name: 'Login page',
      component: LoginPage,
    },
    {
      path: '/register',
      name: 'Register page',
      component: RegisterPage,
    },
    {
      path: '*',
      redirect: '/not_found',
    },
  ],
  mode: 'history',
});

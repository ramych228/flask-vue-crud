import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import StudentsPage from "@/components/students_page/StudentsPage";
import ProjectsPage from "../components/projects_page/ProjectsPage";
import AccountPageStudent from "../components/account/AccountPageStudent";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/account',
      name: 'AccountPageStudent',
      component: AccountPageStudent,
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/students',
      name: 'Students',
      component: StudentsPage,
    },
    {
      path: '/projects',
      name: 'Projects',
      component: ProjectsPage,
    }
  ],
  mode: 'history',
});

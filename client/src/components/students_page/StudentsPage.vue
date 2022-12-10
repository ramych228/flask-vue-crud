<template>
  <div class="container">
    <h2>
      МОЛОДЫЕ<br/>
      ТАЛАНТЫ<br/>
      ИТМО
    </h2>
    <p>
      Страница с лучшими студентами
      Передовой Инженерной Школы ИТМО
    </p>
    <PrimeButton text="Подать заявку"/>
    <StudentsTable :students="students"/>
    <div class="partner-container">
      <div class="partner-text">
        <h2>Станьте партнером ЦИФРОВОЙ ПЛАТФОРМЫ</h2>
        <p>И получите доступ к полному портфолио всех участников
        <p/>
      </div>
      <PrimeButton text="Получить доступ"/>
    </div>
  </div>
</template>

<script>
import PrimeButton from "../default_components/PrimeButton";
import StudentsTable from "./StudentsTable";
import StudentCard from "./StudentCard";
import axios from "axios";

export default {
  name: "StudentsPage",
  components: {StudentCard, StudentsTable, PrimeButton},
  methods: {
    fetchStudents() {
      axios.get("http://localhost:5000/api/students")
        .then(response => {
          this.students = response.data;
        })
        .catch(error => {
          console.log(error);
        });
      // return [
      //   {
      //     id: 1,
      //     name: "Александр",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 2,
      //     name: "Алексей",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 3,
      //     name: "Андрей",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 4,
      //     name: "Антон",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 5,
      //     name: "Артем",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 6,
      //     name: "Вадим",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 7,
      //     name: "Валерий",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 8,
      //     name: "Василий",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      //   {
      //     id: 9,
      //     name: "Виктор",
      //     description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
      //   },
      // ]
    },
  },
  data() {
    return {
      students: [],
    };
  },
  mounted() {
    this.fetchStudents();
  },
}
</script>

<style scoped>
.partner-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  gap: 80px;
}

h2 {
  text-align: end;
}
</style>

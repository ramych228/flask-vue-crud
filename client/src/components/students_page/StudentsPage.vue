<template>
  <div>
  <div class="container">
    <h2 class="text_hollow"> МОЛОДЫЕ</h2>
    <h2 class="text_solid">ТАЛАНТЫ</h2>
    <h2 class="text_hollow">ИТМО</h2>
  </div>
  <div class="container2">
    <div class="text_plain">Страница с лучшими студентами
      Передовой Инженерной Школы ИТМО
    </div>
    <TextAnimationButton text="Подать заявку"/>
  </div>
  <StudentsTable :students="fetchStudents()"/>
  </div>
</template>

<script>
import PrimeButton from "../default_components/PrimeButton";
import StudentsTable from "./StudentsTable";
import StudentCard from "./StudentCard";
import axios from "axios";
import TextAnimationButton from "../default_components/TextAnimationButton.vue";

export default {
  name: "StudentsPage",
  components: { StudentCard, StudentsTable, PrimeButton, TextAnimationButton },
  methods: {
    fetchStudents() {
      axios.get("http://localhost:5000/api/students")
        .then(response => {
          this.students = response.data.students;
        })
        .catch(error => {
          console.log(error);
        });
      return [
        {
          id: 1,
          name: "Александр",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 2,
          name: "Алексей",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 3,
          name: "Андрей",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 4,
          name: "Антон",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 5,
          name: "Артем",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 6,
          name: "Вадим",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 7,
          name: "Валерий",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 8,
          name: "Василий",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
        {
          id: 9,
          name: "Виктор",
          description: "Студент 3 курса, ИТМО, ФИВТ, Информатика и вычислительная техника",
        },
      ]
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
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 300px;
  margin-right: 30px;
  margin-left: 30px;
}
.container2 {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 150px;
  width: 500px;
  margin-right: 30px;
  margin-left: 30px;
}
.text_solid {
  font-family: 'Montserrat', sans-serif;
  color: white;
  font-size: 5em;
  margin-top: 0px;
  margin-bottom: 0px;
  text-align: end;
}
.text_hollow {
  font-family: 'Montserrat', sans-serif;
  color:rgba(0, 0, 0, 0);
  -webkit-text-stroke: 2px #fff;
  font-size: 5em;
  margin-top: 0px;
  margin-bottom: 0px;
  text-align: end;
}


.text_plain {
  font-family: 'Montserrat', sans-serif;
  color:white;
  font-size: 1.5em;
  margin-top: 0px;
  margin-bottom: 0px;
  text-align: start;
}
 
.partner_container {
 
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  gap: 80px;
}

</style>

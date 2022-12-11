<template>
    <div class="wrapper">
        <div class="text_item">Цифровая платформа</div>
        
        <div class="balls">
            <div v-for="i in 25" class="ball">
                
            </div>
        </div> 
    </div>
</template>


<script>
export default {
    name: "Intro"
}
</script>


<style scoped>

.wrapper {
    display: flex;
    justify-content: space-around;
}


.balls {
    display: grid;
    grid: repeat(5, 5em) / repeat(5, 5em);
    width: 20px;
    height: 20px;
}

</style>
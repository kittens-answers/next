<template>
  <div>
    Test api {{ payload }}
  </div>
</template>

<script setup>
const { data: payload } = await useFetch('https://stage-api.kittensanswers.ru/')
</script>

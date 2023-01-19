<template>
  <div>
    Test api {{ fetchData }}
    <button v-on:click="fetchApi">click</button>
    <p>{{ tg }}</p>
  </div>
</template>

<script setup>
useHead({ script: { src: "https://telegram.org/js/telegram-web-app.js" } })
const fetchData = ref("")
const tg = useTG()
const fetchApi = async () => {
  const { data: payload } = await useFetch('https://stage-api.kittensanswers.ru/', { method: 'POST' })
  fetchData.value = payload.value
}
</script>

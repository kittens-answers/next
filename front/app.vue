<template>
  <div>
    Test api {{ fetchData }}
    <button v-on:click="fetchApi">click</button>
  </div>
</template>

<script setup>
const fetchData = ref("")
const fetchApi = async () => {
  const { data: payload } = await useFetch('https://stage-api.kittensanswers.ru/', { method: 'POST' })
  fetchData.value = payload.value
}
</script>

<template>
    <section class="section">
        <div class="container">
            <form class="box">
                <div class="field has-addons">
                    <div class="control is-expanded">
                        <input name="q" class="input" type="text" placeholder="Поиск в котиках">
                    </div>
                    <div class="control">
                        <button class="button is-info">
                            <span class="icon">
                                <ion-icon name="search-outline"></ion-icon>
                            </span>
                        </button>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <label class="checkbox">
                            <input type="checkbox" name="only-correct" checked value="True">
                            Только верные ответы
                        </label>
                    </div>
                </div>
            </form>
        </div>
    </section>
    <section class="section">
        <div class="container">
        </div>
    </section>
</template>

<script setup>
const route = useRoute()
</script>

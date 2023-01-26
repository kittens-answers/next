// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            link: [
                { rel: "stylesheet", href: "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css" }
            ],
            script: [
                { src: "https://telegram.org/js/telegram-web-app.js" },
                { type: "module", src: "https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js", tagPosition: "bodyClose" },
                { nomodule: true, src: "https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js", tagPosition: "bodyClose" }
            ]
        }
    }
})

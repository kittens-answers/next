export default function () {
    if (process.client) {
        return window.Telegram.WebApp.initData
    } else return ""
}
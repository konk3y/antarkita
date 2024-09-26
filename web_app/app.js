let tg = window.Telegram.WebApp;
tg.expand();

function sendOrder() {
  tg.sendData("Order placed");
}

function getSupport() {
  tg.sendData("Support requested");
}

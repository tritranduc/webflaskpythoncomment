$(document).ready(function() {
    $("#sendbutton").click(() => {
        data_get = click_send_button()
        if (data_get == null) {
            console.log(click_send_button());
            return;
        } else {
            console.log(data_get)
        }
    });
    setInterval(update_comment(), 4)
})
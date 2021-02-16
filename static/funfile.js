function click_send_button() {
    var data_get
    var data_append = []
    var data_user = $("#name").val();
    var data_comment = $("#myMessage").val();
    if (data_user == "") {
        $("#error").html("you must t type the name <br>");
        return null;
    } else {
        $("#error").html("hi " + data_user + " <br > ");
        console.log("hi " + data_user + " <br > ");
    }
    if (data_comment == "") {
        $("#error").html("you must t type the comment <br>");
        return null;
    } else {
        console.log(data_comment);
    }
    $.ajax({
        type: "post",
        url: "/addcomment",
        data: {
            comment_data: data_comment,
            user_name: data_user,
            like: 0
        },
        success: function(response) {
            var data_get = response["data"]
            data_get.forEach(data_get => {
                data_append.push("<li>user send :" + data_get["user_name"] + ", like : " + data_get["like"] + ", comment : " + data_get["comment"] + "<button id= '" + data_get["id_comment"] + "' > like </button> </li > ")
                console.log(data_get);
                $("#messages").html(data_append);
            });
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    })
    return data_get
}

function update_comment() {
    var url = "/readcomment"
    var data_append = []
    $.ajax({
        type: "get",
        url: url,
        success: function(response) {
            console.log(response["data"])
            var data_get = response["data"]
            data_get.forEach(data_get => {
                data_append.push("<li>user send :" + data_get["user_name"] + ", like : " + data_get["like"] + ", comment : " + data_get["comment"] + "<button id= '" + data_get["id_comment"] + "' > like </button> </li > ")
                console.log(data_get);
                $("#messages").html(data_append);
            })
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function sleep(milliseconds) {
    milliseconds = milliseconds * 1000
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds) {
            break;
        } else {
            console.log(i)
        }
    }
}
function send(str) {
    if (str) {
        $.ajax({
            type: 'POST',
            url: "/send",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                "message": str,
                "phone_number": "+3547894724",
            }),
            success: function (res) {
                console.log(res);
            },
            error: function (error) {
                console.log(error);
            },
            complete: function (data) {
                $("#btn-send").attr("disabled", false);
            }
        });
    }
}


$(document).ready(function () {
    $("#btn-1").click(function (e) {
        send("Halló þetta er Auður, Þú hefur búið til nýtt markið! Þú ert einu skrefi nær að rækta með okkur skóg!");
    });

    $("#btn-2").click(function (e) {
        send("Hæ! Auður hér, æðislegar fréttir! Við erum búin að planta tré í þýnu nafni.");
    });

    $("#btn-3").click(function (e) {
        send("Hæ! Auður hér, vildi bara minn á að spara, ráðstafaðu innan 5 daga til þess að halda þínu striki.");
    });
});
$(document).ready(function() {
    console.log("Initializing...")
    $("#title").keyup(validateTitle)
    console.log("Done.")
})


function validateTitle() {
    newShowTitle = $("#title").val()
    console.log("validating title: " + newShowTitle)
    $.ajax("/api/shows/exists/" + newShowTitle).done(function(response) {
        console.log(response)
        if (response.exists == true) {
           $("#title-error").show()
        } else {
            $("#title-error").hide()
        }
    })
    
}

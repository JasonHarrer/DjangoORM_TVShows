$(document).ready(init())


function init() {
    console.log("Initializing...")
    $("#title").change(validateTitle)
    console.log("Done.")
}


function validateTitle() {
    console.log("validating title")
    newShowTitle = $("#title").val()
    $.ajax("/api/shows/exists/" + newShowTitle).done(function(response) {
        if (response.exists == true) {
           $("#title-error").attr("display", "block") 
        } else {
            $("#title-error").attr("display", "none")
        }
    })
    
}


function logout(){
    $.ajax({
        url: "/logout/",
        method: "POST",
        success: function(data, status, xhr){
            if(data.created === "YES"){
                window.location.replace("/register");
            }
            
        },
        error: function(xhr, status, err){
            alert(err);
        }

    })

}
function about(){
    window.location.replace("/about/");
}
function home(){
    window.location.replace("/");
    
}
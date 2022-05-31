const { regexpToText } = require("nodemon/lib/utils");

function ou(){
    $.ajax({
        url: "/login/",
        method: "POST",
        data:{
            username: document.getElementById("z2").value,
            password: document.getElementById("z3").value,
        },
        success: function(data, status, xhr){
            if(data.created === "YES"){
                if(window.location.href == "/"){
                    window.location.reload();
                } else {
                    window.location.replace("/");
                }
                
            }
            else{
                alert("invalid ccredentials");
            }
            
        },
        error: function(xhr, status, err){
            alert(err);
        }
    
    
    })
}
function relreg(){
    window.location.replace("/register");
}
function rel2reg(){
    window.location.reload();
}
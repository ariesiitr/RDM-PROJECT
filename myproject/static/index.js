
function logout(){
    $.ajax({
        url: "logout/",
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
    window.location.replace("/about");
}
function fun1(){
    window.location.replace("/electronics");
}
function fun2(){
    window.location.replace("/eatable");
}
function fun3(){
    window.location.replace("/grocery");

}
function fun4(){
    window.location.replace("/clothes");


}
function home(){
    window.location.reload();
    
}
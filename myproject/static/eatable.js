
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
function buy1(clickID){
    
    console.log(clickID)
    $.ajax({
        url: "/cart/",
        method: "POST",
        data:{
            'detail': clickID,
        },
        success: function(data, status, xhr){
            alert("item added to your cart")
        },
        error: function(xhr, status, err){
            alert(err);
        }
    })
    

}
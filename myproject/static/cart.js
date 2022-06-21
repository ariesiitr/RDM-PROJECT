
function fun7(clickID){
    
    console.log(clickID)
    $.ajax({
        url: "/cart1/",
        method: "POST",
        data:{
            'detail': clickID,
        },
        success: function(data, status, xhr){
            window.location.reload()
        },
        error: function(xhr, status, err){
            alert(err);
        }
    })
    

}
function fun9(clickID){
    
    console.log(clickID)
    $.ajax({
        url: "/cart2/",
        method: "POST",
        data:{
            'detail': clickID,
        },
        success: function(data, status, xhr){
            window.location.reload()
        },
        error: function(xhr, status, err){
            alert(err);
        }
    })
    

}

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
function home(){
    window.location.replace("/");
    
}
let d=0;
function pay(){
    
    $.ajax({
        url: "/cart3/",
        method: "POST",
        success: function(data, status, xhr){
            alert("order succesfully placed ")
            window.location.reload()
        },
        error: function(xhr, status, err){
            alert(err);
        }

    })

}

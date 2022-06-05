
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
function ou(){
    console.log("reached1")


    if(document.getElementById("z").value==""||document.getElementById("z1").value==""||document.getElementById("z2").value==""||document.getElementById("z3").value==""||document.getElementById("z4").value==""||document.getElementById("z6").value==""||document.getElementById("z7").value==""||document.getElementById("z3").value!=document.getElementById("z4").value){
        alert("fill all the details correctly")
        console.log("reached2112")
        console.log("here ")
        console.log(document.getElementById("z").value)
        if(document.getElementById("z").value==""){
  
            document.getElementById("wr1").style.display="block";
        }
        if(document.getElementById("z1").value==""){
            document.getElementById("wr2").style.display="block";
        }
        if(document.getElementById("z2").value==""){
            console.log("two")
            document.getElementById("wr3").style.display="block";
        }
        if(document.getElementById("z3").value==""){
            document.getElementById("wr4").style.display="block";
        }
        if(document.getElementById("z6").value==""){
            console.log("two")
            document.getElementById("wr5").style.display="block";
        }
        if(document.getElementById("z7").value==""){
            document.getElementById("wr6").style.display="block";
            
        }
        if(document.getElementById("z4").value==""){
            document.getElementById("wr8").style.display="block";
            
        }
        if(document.getElementById("z4").value!=document.getElementById("z3").value){
            document.getElementById("wr9").style.display="block";
            
        }
       
        if(document.getElementById("z").value!=""){

            document.getElementById("wr1").style.display="none";
        }
        if(document.getElementById("z1").value!=""){
            document.getElementById("wr2").style.display="none";
        }
        if(document.getElementById("z2").value!=""){
            console.log("two")
            document.getElementById("wr3").style.display="none";
        }
        if(document.getElementById("z3").value!=""){
            document.getElementById("wr4").style.display="none";
        }
        if(document.getElementById("z6").value!=""){
            console.log("two")
            document.getElementById("wr5").style.display="none";
        }
        console.log(document.getElementById("wr6"))
        if(document.getElementById("z7").value!=""){
            console.log(document.getElementById("wr6"))
            document.getElementById("wr6").style.display="none";
            
        }
        if(document.getElementById("z4").value!=""){
            document.getElementById("wr8").style.display="none";
            
        }
        if(document.getElementById("z4").value==document.getElementById("z3").value){
            document.getElementById("wr9").style.display="none";
            
        }
    
    }else{
        $.ajax({
            url: "/register/",
            method: "POST",
            data: {
              firstname: document.getElementById("z").value,
              lastname: document.getElementById("z1").value,
              mobile: document.getElementById("z6").value,
              email: document.getElementById("z7").value,
              username: document.getElementById("z2").value,
              password: document.getElementById("z3").value,
              
            },
            success: function(data, status, xhr){
                if(data.created === "no1"){
                    alert("Given Username already exists \n try a new one")
                }else if(data.created === "no2") {
                    alert("The account already exists  \n try register a new one.");
                }else{
                    if(window.location.href == "/login"){
                        window.location.reload();
                    } else {
                        window.location.replace("/login");
                    }
                }
                
            },
            error: function(xhr, status, err){
                alert(err);
            }

        })


    } 

}
function relreg(){
    window.location.reload();
}
function rel2reg(){
    window.location.replace("/login");
}
function getRam(){
    fetch("/api/sysinfo/ram", {
        method:"GET"
    })
    .then(request => request.json())
    .then(data => {
        console.log(data)
    })


    //end of the fucntion
}


getRam()


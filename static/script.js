document.getElementById('send').addEventListener('click',function(){
    const baseDepart=document.getElementById('base_depart').value;
    const baseArrive=document.getElementById('base_arrive').value;
    const nbre=document.getElementById('nbre').value.replaceAll(" ","")
    
    fetch("/convertir",{
        method: "POST",
        headers: { "Content-Type":"application/json"},
        body: JSON.stringify({nombre:nbre,base_depart:baseDepart,base_arrivee:baseArrive})
    })
    .then(response=> response.json())
    .then(data =>{
        if (data.erreur){
            document.getElementById('result').innerHTML=data.erreur;
            document.getElementById('result').style.color="red"
        }else{
            document.getElementById('result').innerHTML=data.resultat;
        }
    })
});

nbre.addEventListener('input',()=>{
    document.getElementById('result').innerHTML=0;
})
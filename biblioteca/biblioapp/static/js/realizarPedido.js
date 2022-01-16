var resverarBtns = document.getElementsByClassName('reservar')




for (i = 0; i < resverarBtns.length; i++) {


    resverarBtns[i].addEventListener('click', function(){
        var bookid = this.dataset.book
        
        
        console.log( 'Book:', bookid)
       

        alert('Reserva recibida ' + user + ' !')
        console.log('USER:', user)
        submitOrderData( bookid)
      
               
      

    })
    
    

}


function submitOrderData(bookid){
    console.log('User is authenticated, sending data...')
    
    var url = '/process_order/'
   
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({ 'bookid': bookid})
        
    })
    .then((response) =>{
        return response.json()

    })

    .then((data) =>{

        // console.log('data:', data)
        location.reload()
        // window.location.href = "mis_reservas/"
        

    });
    console.log('llega')
    // window.location.href = "shop/"


}

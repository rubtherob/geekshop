window.onload = function (){
    $('.Product_card').on('click','button[type="button"]',function (){
        let t_href = event.target



        $.ajax(
            {
                url: "/baskets/add/" + t_href.id + '/',
                success: function (data){
                    $('Product_card').html(data.result)
                },
            }
        );
        event.preventDefault()

    })

}

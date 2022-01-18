// function uploadFile(event) {
// 	event.preventDefault();
//     var formData = new FormData(this); //get data of form elements for submission

//     alert(formData);

//     // formData.append('sg_id', '{{ sg_id }}');
// 	$.ajax({
// 		type:'POST',
// 		url:'/send_msg',
// 		enctype: 'multipart/form-data',
// 		data: {
// 			formData,
// 			trans_id: id,

// 			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
// 		},
// 		success: function(data){
// 			//alert(data)
// 		}
// 	});
// }

// $(function() {
//      $('#file-upload-form').submit(uploadFile(event));
// });


// $('#file_form').submit(function(event){
//     event.preventDefault();
//     var formData = new FormData(this); //get data of form elements for submission
//     formData.append('sg_id', '{{ sg_id }}'); //add additional data to form's data

//     alert(formData);

//     $.ajax({
//         url: "/send_msg",
//         type: "POST",
//         enctype: 'multipart/form-data',
//         data: formData,
//         processData: false,
//         contentType: false,
//         cache: false,
//         success: function (data) {
//             if(! data.created){
//                 location.reload();
//             } else if(! data.valid_extension){
//                 swal({
//                     title: 'You can only submit PDF files',
//                     text: '',
//                     icon: 'error',
//                     timer: 5000,
//                 });
//             }
//         }
//     });
// });
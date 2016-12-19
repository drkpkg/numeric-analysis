$(function(){
//    var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10],
//                                              axis:true,
//                                              zoom: {
//                                                  factorX:1.25,
//                                                  factorY:1.25,
//                                                  wheel:true,
//                                                  eps: 0.1
//                                                 }
//                                              });
    initValidate();
});

function initValidate(){
  $('#form')
  .form({
    onSuccess: function(event, fields) {
        SubmitForm(fields);
        event.preventDefault();
    },
    on: 'blur',
    fields: {
      equations: {
        identifier  : 'equations',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_gauss',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#body-table').empty();
            var eqc = eval(data.eqc);
            var sct = eval(data.sections);
            $.each(eqc, function(index, element){
                var actual = '<tr>';
                $.each(element, function(i, e){
                    actual = actual + '<td>' + e + '</td>';
                });
                actual = actual + '<td><strong>' + sct[index] + '</strong></td></tr>';
                $('#body-table').append(actual);
            });

        }
    });
}

//function drawPoints(board, a, b, error){
//    board.create('point', [a,b],{name: error+'%', withLabel:true});
//}
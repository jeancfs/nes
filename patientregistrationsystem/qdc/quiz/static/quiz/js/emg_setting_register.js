/**
 * Created by evandro on 5/5/16.
 */

$(function(){
    $("[data-toggle=tooltip]").tooltip();
});

function show_modal_remove_setting(emg_setting_type){
    var  modal_remove = document.getElementById('remove-setting');
    modal_remove.setAttribute("value", 'remove-' + emg_setting_type)
    $('#modalRemoveEquipment').modal('show');
}

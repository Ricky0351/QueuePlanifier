$(function () {
    function QueueplanifierViewModel(parameters) {
        var self = this;

        self.GetListe = function (data) {

            OctoPrint.simpleApiCommand("Queueplanifier", "RecupereListeFichiers", { "ip": "someIp" });



        };
    }

    ADDITIONAL_VIEWMODELS.push([
        QueueplanifierViewModel,
        ["settingsViewModel"],
        ["#tab_plugin_Queueplanifier"]
    ]);
});
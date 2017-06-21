import QtQuick 2.0
import QtQuick.Controls 1.2
import SDK 1.0

Rectangle {
	id: main
	width: 800
	height: 480
	
	RadialBar {
		width: 300
	    height: 300
	    penStyle: Qt.RoundCap
	    //dialType: RadialBar.FullDial
	    progressColor: "#1dc58f"
	    foregroundColor: "#191a2f"
	    dialWidth: 30
	    startAngle: 180
	    spanAngle: 70
	    minValue: 0
	    maxValue: 100
	    value: 50
	    textFont {
	        family: "Halvetica"
	        italic: false
	        pointSize: 16
	    }
	    suffixText: "%"
		textColor: "#FFFFFF"
	}	

}
	
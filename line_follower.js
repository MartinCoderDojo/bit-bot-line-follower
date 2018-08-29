let right = 0
let left = 0

basic.forever(() => {

    left = bitbot.readLine(BBLineSensor.Left)
    right = bitbot.readLine(BBLineSensor.Right)

    if (left == 1 && right == 0) {
        bitbot.drive(0)
        basic.showString("L")
        bitbot.driveTurn(BBRobotDirection.Left, 200)
    } else if (left == 0 && right == 1) {
        bitbot.drive(0)
        basic.showString("R")
        bitbot.driveTurn(BBRobotDirection.Right, 200)
    } else if (left == 1 && right == 1) {
        basic.showString("F")
        bitbot.drive(200)
    } else {
        basic.showString("S")
        bitbot.drive(0)
    }

    basic.pause(200)

})

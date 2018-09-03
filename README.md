# PiJuice-Bot

This project shows you how to use the PiJuice to drive a 2-wheel drive robot using the Ryanteck motor controller board. The PiJuice has the ability to drive external components using the VSYS output, which can be configured in the PiJuice software to output either a maximum of 500mA or 2100mA.

## What you need

You will need the following components to build this project:

- Raspberry Pi board with Wi-Fi
- PiJuice HAT
- Ryanteck motor controller board
- Robotic chassis
- Ultrasonic sensor (optional)
- 2x microswitches (optional)

## Software installation

We have compiled some software examples to use with the Ryanteck motor controller board and PiJuice HAT with different sensors attached to the board, such as the ultrasonic sensor which can detect objects at the front of the robotic chassis and also two micro switches connected to the front to detect when the robotic chassis bumps into objects.

### Auto-installation

Below is an auto installation script which will down load and install all the software dependancies as well as the projects file from the GitHub repository. To download the software simply copy and paste or insert the below command:

```bash
#PiJuice-Bot auto-installations script
curl -sSL https://raw.githubusercontent.com/ChristopherRush/pijuice-bot/master/install.sh | sudo bash
```

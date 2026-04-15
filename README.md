I just created a hackpad with 8 switches and 8 rgb LEDs! I am a beginner and this is my first project.

I built this project because I have been very interested in the custom keyboard community for a while now and want to try my hands at it. I found this oppurtunity off of instagram and I though it was a very cool thing I could do!

To use this, flash the firmware onto the macro pad and assemble with the sandwich mount design. The switches and LEDs need to be soldered onto the PCB and the keycaps go on at the end.

Challenges:

First: PCB design: KiCad

I had never touched a CAD software let alone designed a PCB. It started off generally easy with the PCB schematic which was self explanatory. However, next was the PCB editor. I spent almost 6 hours on this step. At first my switches and LEDs were in the wrong order, you couldn’t zigzag the LEDs or switches or else you would have a very hard time routing the PCB. Through trial and error, I learned how to route the PCB. 
<img width="425" height="751" alt="Screenshot 2026-04-15 at 12 01 54 AM" src="https://github.com/user-attachments/assets/d98c6034-6251-4a88-a225-c22b8ba37d72" />
<img width="986" height="640" alt="Screenshot 2026-04-15 at 12 02 50 AM" src="https://github.com/user-attachments/assets/fddc2ca6-f4d0-4748-9b6e-1ff67df9804f" />
<img width="327" height="686" alt="Screenshot 2026-04-09 at 6 52 57 PM" src="https://github.com/user-attachments/assets/1c07e6cc-a58c-4e65-af87-c336d638ed61" />

Although it didn’t look the prettiest, I was proud of what I’d done. I learned some valuable problem solving skills and some very useful things from this. It took a lot of logic to figure out the routing. I also learned that the voltage and ground lines could be linked up line to line.

Second: Case Design

This was my first time doing any sort of 3D design. I first used Fusion360 but due to its limited capabilities, I decided to switch to Onshape. The design was actually fairly difficult and time consuming. This was also where the most math was used to center all the cutouts and make sure the clearances were correct. Compared to the PCB, it was less difficult but more time consuming.
<img width="444" height="574" alt="Screenshot 2026-04-09 at 6 48 32 PM" src="https://github.com/user-attachments/assets/fb02a042-970a-4012-a592-422ad1b57ff3" />
<img width="445" height="576" alt="Screenshot 2026-04-09 at 6 48 54 PM" src="https://github.com/user-attachments/assets/6238042c-c809-45d0-94f2-d78f6fa1cbdc" />
https://cad.onshape.com/documents/ae2a962784265a0a15a314a3/w/fd7747368c903f62fc80b54c/e/c2a1514edb9aca260c24a683?renderMode=0&uiState=69d857150cda52f2ac39aa26 

Third: Firmware

This was actually the easiest part of the project. I just mapped each key to be an arbitrary macro key so the coding was very straight forward.

Summary:

I enjoyed this project a lot and learned a lot about 3D design, PCB design, and coding which I hope to use in other projects!

Materials: 
BOM:
8x Cherry MX Switches
8x SK6812 MINI-E LEDs
1x Seeeduino XIAO RP2040
8x Blank DCA Keycaps
4x M3 Screws
(Included in the kit)

Custom PCB
($5.12 from the HCB grant will be used)
<img width="1419" height="802" alt="Screenshot 2026-04-14 at 11 59 56 PM" src="https://github.com/user-attachments/assets/c766ff65-5404-4b24-8c0e-7b68fe9db961" />



Top Plate.step 
Bottom Plate.step
(Will be printed through printing legion) 


Others:
KMK Firmware

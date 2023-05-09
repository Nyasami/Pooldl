# Pooldl
A script to download mappools in osu! tourney for people who is really lazy to click buttons and the host didn't gave the zip file of the pool.

## Download 

```
git clone https://github.com/NagataAsami-chan/Pooldl
```
## Requirements
You need Python 3.x.x to run the script, then open cmd in the folder and type:
```
pip install -r requirements.txt
```
## Setup
### Update v1.1.0: Now you don't have to do these steps below, just authorize the app then it'll be okay, if it shows a warning, click onto the advaced option and click continue to Pool DL, after you authorize it, you won't have to do it again! ( It's okay trust me 100% not malware )
~~Go to https://console.cloud.google.com/projectselector2/apis/dashboard and create a new project, name the project to anything you like then press create.~~

~~Click onto the credential tab then find the `+ Create Credentials` button, click on it and choose `Service Account`, name it again to anything then click `Create and continue`, then you just need to press done.~~

~~Now there should have an account in the `Service Accounts` section, click onto that account, go to the `KEYS` tab and click `ADD KEY` --> `Create new key` --> choose JSON and create.~~

~~Now you should have a JSON file downloaded, rename it to `credential.json` and replace the original json file by paste the file into the app's folder and you're all set!~~

## Usage



https://user-images.githubusercontent.com/80683081/236291365-0afcd6fb-47e9-43a5-9303-afd44b07434a.mp4


### Detailed usage

On the mappool sheet, select all the cell that has the map url `linked` to it (hovering on those would have a box shows up the beatmap, and sheet maker usually let the map name in it)

Then you just gotta copy the url that leads to those cell by right clicking on it, open the script window and paste the url into the first text box, select your desired folder and click download button

After the the window will not responded (I *** hate tkinter) but no worries, you can check out the log under the window and let it download

## Special thanks
Beatconnect

Hosts that didn't make the zip file

Osu api v2 that won't let me download and I had to use mirror

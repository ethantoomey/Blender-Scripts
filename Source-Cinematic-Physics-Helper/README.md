## How to use the Source Cinematic Physics Helper Script **(VERSION 1.0)**

#### 1) Before we get started...
First things first, make sure to create your animated objects in blender, whether simulated with rigid bodies or a manual animation. 
>I recommend using the Blender addon 'Cell Fracture' to break your object like I did to this cube below if you're looking to get this kind of effect.

![](https://thumbs.gfycat.com/FaintQuarterlyAfricanjacana-size_restricted.gif)

####2 ) Getting Started:
Assuming you've already downloaded my script, make sure to put it somewhere you can load it in later. I recommend having a blender scripts folder for future uses! 

1. Open your Blender file, bring up the Text Editor in a new window.

2. Use the 'Open' button to open the script in the text editor.
 * Locate and load the script, which is called **'blender-source-cinematic-physics-helper.py'** *

3. Make sure to select all the objects to be animated by going into Wireframe mode by pressing **(Z)** and then selecting the objects by pressing **(B)**.

 ![](https://giant.gfycat.com/ComfortableTiredBlowfish.gif)

4. Now with all the objects selected, we can run our script by going back to the text editor with the script loaded and simply pressing 'Run Script' or pressing **(ALT+P)**

 ![](https://thumbs.gfycat.com/DismalRealGrizzlybear-size_restricted.gif)

  *If you did everything correctly, the script should 
 automatically create an Object called 'Physics 
 Objects', and nested within should be an armature 
 object with bones placed at all of the origin points 
 of each object, as well as the objects themselves.*

  The script automatically takes care of the grunt 
 work (weighting, bone creation, etc.) , leaving you 
 with a few simple button clicks away from exporting!
 Now, we can bake our animation from the objects, IE. 
 The rigid body simulation, into the pose bones, 
 allowing us to use the animation in Source. 

5. Now it's time to bake the animation into an action. Go into **Object Mode** and select one of the bones. then, on the 'Toolshelf' on the left side of the screen, Choose the 'Animation' tab.

 ![](https://i.imgur.com/0E4C0tz.png)

6. Now Click 'Bake Animation' and make sure the following are checked off in the prompt that appears.
 ![](https://i.imgur.com/0MDKk5l.png)

 **MAKE SURE BAKE DATA IS SET TO POSE!**

7. Hit 'OK', and now you can hide the 'Physics Armature' and its Parent 'Physics Objects' and select just the Mesh Objects again, and join them by pressing **(CTRL+J)**

 ![](https://thumbs.gfycat.com/SizzlingQuickBluemorphobutterfly-size_restricted.gif)


8. Select the joined Mesh Object, and remove the Rigid Body.

9. Now unhide the Physics Armature, add an Armature Modifier to the joined Mesh Object. Set the Object in the Armature modifier to be the Physics Armature.

 ![](https://i.imgur.com/brFF37p.png)

10. Play it back in blender. If Its playing the animation then you've successfully created the animation to export into source!

11. Make sure to both of the objects (The Armature & The Mesh) individually and press **(CTRL+A)** and apply **Location** & **Scale** for both.

12. Now using the [Blender Source Tools](http://steamreview.org/BlenderSourceTools/), you can easily export both the animation and the object by selecting the mesh object and the Armature and hitting export under 'Source Engine Export'

 ![](https://i.imgur.com/ldNQaC3.png)

The files exported! The animation will be under a subfolder called 'Anims' which you can easily reference when compiling the object with your QC File.





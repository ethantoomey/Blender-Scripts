import bpy, bmesh

objectname = "part"

objs = []
count = 0

scene = bpy.context.scene
scene.frame_current = 0

origin = bpy.data.objects.new( "empty", None )
bpy.context.scene.objects.link( origin )
origin.empty_draw_size = 2
origin.empty_draw_type = 'PLAIN_AXES'
origin.name = "Physics Objects"
origin.location = (0,0,0)
origin.lock_location[2] = True

Armature = bpy.data.armatures.new("Armature")
armatureobj = bpy.data.objects.new( "Physics Armature", Armature )
bpy.context.scene.objects.link( armatureobj )

armatureobj.parent = origin

for obj in bpy.context.selected_objects:
    objs.append(obj)
    
for obj in objs:
    
    count = count + 1
    obj.name = (objectname + str(count))
    
    obj.parent = origin
    
    bpy.context.scene.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')  

    mesh=bmesh.from_edit_mesh(obj.data)
    for v in mesh.verts:
        v.select = True    

    bpy.ops.object.vertex_group_add()    
    
    bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode='OBJECT')   
    
    bpy.context.active_object.vertex_groups[0].name = obj.name + "_bone"
    
    bpy.context.scene.objects.active = armatureobj
    bpy.ops.object.mode_set(mode='EDIT')
    
    bone = Armature.edit_bones.new(obj.name+"_bone")
    bone.tail[2] = 1
    
    bpy.ops.object.mode_set(mode='POSE')
    bonecnstr = armatureobj.pose.bones[bone.name].constraints.new('COPY_TRANSFORMS')
    bonecnstr.target = obj
    
    bpy.ops.object.mode_set(mode='OBJECT')

bpy.context.scene.objects.active = armatureobj
bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.armature_apply()



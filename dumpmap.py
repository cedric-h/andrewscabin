import bpy
import bmesh
import json

with open('./map.json', 'w') as fp:
    json.dump({
        'idx': [
            [int(x) for x in p.vertices]
                for p in bpy.context.active_object.data.polygons
        ],
        'vert': [x.co[:3] for x in bpy.context.active_object.data.vertices]
    }, fp)
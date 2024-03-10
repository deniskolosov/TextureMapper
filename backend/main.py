from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, Response
from starlette.status import HTTP_200_OK
from fastapi.middleware.cors import CORSMiddleware
from pygltflib import GLTF2, Texture, ImageFormat, Image
import shutil
from pathlib import Path
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


def apply_texture_and_generate_glb(texture_path):
    gltf = GLTF2().load("BoxTextured.glb")

    gltf.textures.pop()

    existing_image_index = gltf.materials[0].pbrMetallicRoughness.baseColorTexture.index
    gltf.images.pop()

    new_image = Image()
    new_image.uri = texture_path
    gltf.images.append(new_image)

    new_texture = Texture()
    new_texture.source = len(gltf.images) - 1
    gltf.textures.append(new_texture)
    gltf.meshes[0].primitives[0].material = len(gltf.materials) - 1
    gltf.convert_images(ImageFormat.DATAURI)
    gltf.save_binary("response.glb")


@app.get("/ping")
async def ping():
    return Response(content="pong", status_code=HTTP_200_OK)


@app.post("/render")
async def render(texture: UploadFile = File(...)):
    if texture.content_type not in ["image/jpg", "image/png"]:
        return Response(content="Unsupported file type", status_code=400)
    destination = Path("upload") / texture.filename
    with destination.open("wb") as buffer:
        shutil.copyfileobj(texture.file, buffer)

    texture_path = "upload/" + texture.filename
    apply_texture_and_generate_glb(texture_path)

    return FileResponse(path="response.glb", media_type="model/gltf-binary")

<template>
  <div>
    <div id="threejs-container"></div>
    <input type="file" @change="onFileSelected" />
    <button @click="uploadFile" :disabled="!selectedFile">Upload</button>
  </div>
</template>

<script>
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

export default {
  data() {
    return {
      selectedFile: null,
      scene: null,
      renderer: null,
      camera: null,
    };
  },
  methods: {
    initThree(url) {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth / window.innerHeight,
        1,
        10000
      );
      camera.position.set(1, 1, 1);

      camera.position.z = 1;
      const renderer = new THREE.WebGLRenderer({ alpha: true });
      const controls = new OrbitControls(camera, renderer.domElement);
      controls.update();
      const light = new THREE.AmbientLight(0xFFFFFF);
      light.position.set(10, 10, 10);
      scene.add(light);
      renderer.setSize(window.innerWidth , window.innerHeight );
      this.$el.appendChild(renderer.domElement);

      const loader = new GLTFLoader();

      loader.load(
        url,
        // called when the resource is loaded
        (gltf) => {
          scene.add(gltf.scene);
          animate();
        },
        (xhr) => {
          console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
        },
        (error) => {
          console.error("An error happened", error);
        }
      );

      function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
      }
    },
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    async uploadFile() {
      if (!this.selectedFile) {
        alert("Please select a file first.");
        return;
      }
      const formData = new FormData();
      formData.append("texture", this.selectedFile);
      try {
        const response = await this.$http.post("/render", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType: "blob",
        });
        if (response.status === 200) {
          try {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            this.initThree(url);
          } catch (error) {
            console.error("Error loading GLTF model:", error);
          }
        } else {
          console.error("Error uploading file:", response);
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    },
  },
};
</script>

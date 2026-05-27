// Three.js 3D Scene Setup
let scene, camera, renderer;
let particles = [];

function initThreeJS() {
  // Scene setup
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x1a1a2e);
  scene.fog = new THREE.Fog(0x1a1a2e, 100, 1000);

  // Camera
  camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.z = 30;

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.shadowMap.enabled = true;
  document.getElementById('canvas-container').appendChild(renderer.domElement);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
  scene.add(ambientLight);

  const pointLight = new THREE.PointLight(0x00d4ff, 1);
  pointLight.position.set(50, 50, 50);
  pointLight.castShadow = true;
  scene.add(pointLight);

  const pointLight2 = new THREE.PointLight(0xff006e, 0.5);
  pointLight2.position.set(-50, -50, 50);
  scene.add(pointLight2);

  // Create floating particles
  createParticles();

  // Create 3D geometric elements
  createGeometricElements();

  // Handle resize
  window.addEventListener('resize', onWindowResize);

  // Start animation loop
  animate();
}

function createParticles() {
  const particleGeometry = new THREE.BufferGeometry();
  const particleCount = 100;
  const positions = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 100;
    positions[i + 1] = (Math.random() - 0.5) * 100;
    positions[i + 2] = (Math.random() - 0.5) * 100;
  }

  particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

  const particleMaterial = new THREE.PointsMaterial({
    color: 0x00d4ff,
    size: 0.3,
    sizeAttenuation: true,
    transparent: true,
    opacity: 0.6,
  });

  const particleSystem = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particleSystem);

  particles.push({
    mesh: particleSystem,
    velocityX: (Math.random() - 0.5) * 0.02,
    velocityY: (Math.random() - 0.5) * 0.02,
    velocityZ: (Math.random() - 0.5) * 0.02,
  });
}

function createGeometricElements() {
  // Rotating cube
  const cubeGeometry = new THREE.BoxGeometry(5, 5, 5);
  const cubeMaterial = new THREE.MeshPhongMaterial({
    color: 0x00d4ff,
    wireframe: false,
    emissive: 0x003366,
  });
  const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
  cube.position.set(-15, 10, 0);
  cube.castShadow = true;
  scene.add(cube);

  // Rotating octahedron
  const octGeometry = new THREE.OctahedronGeometry(4, 0);
  const octMaterial = new THREE.MeshPhongMaterial({
    color: 0xff006e,
    wireframe: false,
    emissive: 0x660033,
  });
  const octahedron = new THREE.Mesh(octGeometry, octMaterial);
  octahedron.position.set(15, 10, 0);
  octahedron.castShadow = true;
  scene.add(octahedron);

  // Rotating torus
  const torusGeometry = new THREE.TorusGeometry(6, 2, 16, 100);
  const torusMaterial = new THREE.MeshPhongMaterial({
    color: 0x00ff88,
    wireframe: false,
    emissive: 0x003322,
  });
  const torus = new THREE.Mesh(torusGeometry, torusMaterial);
  torus.position.set(0, -5, 0);
  torus.castShadow = true;
  scene.add(torus);

  // Store for animation
  scene.userData.cube = cube;
  scene.userData.octahedron = octahedron;
  scene.userData.torus = torus;
}

function animate() {
  requestAnimationFrame(animate);

  // Rotate geometric elements
  if (scene.userData.cube) {
    scene.userData.cube.rotation.x += 0.005;
    scene.userData.cube.rotation.y += 0.008;
  }

  if (scene.userData.octahedron) {
    scene.userData.octahedron.rotation.x -= 0.006;
    scene.userData.octahedron.rotation.y -= 0.009;
  }

  if (scene.userData.torus) {
    scene.userData.torus.rotation.x += 0.003;
    scene.userData.torus.rotation.y += 0.004;
  }

  // Animate particles
  particles.forEach((particle) => {
    const positions = particle.mesh.geometry.attributes.position.array;
    for (let i = 0; i < positions.length; i += 3) {
      positions[i] += particle.velocityX;
      positions[i + 1] += particle.velocityY;
      positions[i + 2] += particle.velocityZ;

      // Wrap around
      if (positions[i] > 50) positions[i] = -50;
      if (positions[i] < -50) positions[i] = 50;
      if (positions[i + 1] > 50) positions[i + 1] = -50;
      if (positions[i + 1] < -50) positions[i + 1] = 50;
      if (positions[i + 2] > 50) positions[i + 2] = -50;
      if (positions[i + 2] < -50) positions[i + 2] = 50;
    }
    particle.mesh.geometry.attributes.position.needsUpdate = true;
  });

  renderer.render(scene, camera);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

// Initialize when page loads
window.addEventListener('load', initThreeJS);


This is a simple web application that allows users to render `.glb` (GLB) 3D model files with custom textures.


## Getting Started

1. Clone the repository:
```bash
git clone https://gitlab.com/deniskolosov/glb_render_example.git
cd glb_render_example
```

2. Build and run the containers using Docker Compose (make sure 8000 and 8080 ports are free):
```bash
docker-compose up -d
```

3. Run tests for backend
```bash
docker-compose exec backend pytest
```
4. Check logs for the apps
```bash
docker-compose logs
```

## Usage

Once the application is running, you can access:

- The Vue frontend at `http://localhost:8080`
- The FastAPI Swagger docs at `http://localhost:8000/docs`

To use the application, follow these steps:

1. Navigate to the frontend URL in your web browser.
2. Apply a custom texture by uploading an .png file.

## Development

### Frontend

The frontend is a Vue.js application. To work on it directly, navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

To serve the frontend application with hot-reload for development purposes:

```bash
npm run serve
```

### Backend

The backend is built using FastAPI. To check the backend code locally, navigate to the `backend` directory and set up a virtual environment:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
venv\Scripts\activate  # For Windows
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

To run the FastAPI server for development:

```bash
uvicorn main:app --reload
```

## API Endpoints

The FastAPI backend provides several endpoints for interaction with the frontend:

- `POST /render`: Endpoint to upload textures.
- `GET /ping`: Will reply "pong" to every request

Swagger documentation can be accessed at `http://localhost:8000/docs` once the backend service is running.

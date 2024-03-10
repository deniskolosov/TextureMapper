
This is a simple web application that allows users to render `.glb` (GLB) 3D model files with custom textures.


## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-project-name.git
cd your-project-name
```

2. Build and run the containers using Docker Compose:
```bash
docker-compose up -d
```

## Usage

Once the application is running, you can access:

- The Vue frontend at `http://localhost:8080`
- The FastAPI Swagger docs at `http://localhost:8000/docs`

To use the application, follow these steps:

1. Navigate to the frontend URL in your web browser.
2. Apply a custom texture by uploading an image file.

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

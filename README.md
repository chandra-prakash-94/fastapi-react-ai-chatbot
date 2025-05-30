# AI Chatbot Project

This is a full-stack AI chatbot application built with FastAPI (backend) and React (frontend). The project uses Google's Gemini AI model for generating responses and is structured as a monorepo with separate frontend and backend directories.

## Project Structure

```
.
├── chatbot-frontend/     # React frontend application
└── chatbot-backend/      # FastAPI backend server
```

## Frontend (React + Vite)

The frontend is built using React and Vite, providing a modern and fast development experience.

### Prerequisites

- Node.js (Latest LTS version recommended)
- npm or yarn

### Getting Started with Frontend

1. Navigate to the frontend directory:
   ```bash
   cd chatbot-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

The frontend will be available at `http://localhost:5173` by default.

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Backend (FastAPI)

The backend is a FastAPI server that integrates with Google's Gemini AI model to handle chat interactions.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Getting Started with Backend

1. Navigate to the backend directory:
   ```bash
   cd chatbot-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-dotenv google-generativeai
   ```

4. Create a `.env` file in the backend directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

The backend will be available at `http://localhost:8000` by default.

## Development

- Frontend runs on port 5173 (Vite default)
- Backend runs on port 8000 (FastAPI default)
- API documentation is available at `http://localhost:8000/docs`

## Technologies Used

### Frontend
- React
- Vite
- Axios for API calls
- ESLint for code linting

### Backend
- FastAPI
- Google Gemini AI
- Python 3.8+
- Uvicorn ASGI server
- Pydantic for data validation

## Environment Variables

### Backend (.env)
- `GOOGLE_API_KEY`: Your Google API key for Gemini AI

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
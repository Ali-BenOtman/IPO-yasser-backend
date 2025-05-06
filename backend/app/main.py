from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import users
from .routes import companies

# Create FastAPI app
app = FastAPI(
    title="IPO Backend API",
    description="API backend For IPO",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(companies.router)

# Root endpoint
@app.get("/", tags=["root"])
async def root():
    return {
        "message": "IPO Backend API",
        "docs": "/docs",
    }

# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 
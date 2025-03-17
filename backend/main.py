from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class RecipeRequest(BaseModel):
    ingredients: List[str]
    health_preferences: Optional[List[str]] = None
    nutrition_goals: Optional[str] = None
    mood: Optional[str] = None
    taste_preferences: Optional[List[str]] = None

@app.post("/generate-recipe")
def generate_recipe(request: RecipeRequest):
    return {
        "message": "Recipe generated!",
        "ingredients": request.ingredients,
        "health_preferences": request.health_preferences,
        "nutrition_goals": request.nutrition_goals,
        "mood": request.mood,
        "taste_preferences": request.taste_preferences
    }

@app.get("/")
def home():
    return {"message": "Welcome to the AI Recipe Generator!"}

from datetime import date

from application.dto import (
    HealthProfileDTO,
    DailyProgressDTO
)


WELCOME_MESSAGE = "Welcome! I am your Health Tracker bot.\nType /help for the list of commands."

WEIGHT_PROMPT = "Let's fill in your health profile!\n\nStep 1: Enter your weight (in kg)\n   Example: 75.5"
WEIGHT_INVALID = "Weight must be between 0 and 300 kg. Please try again:"
WEIGHT_CONFIRMATION = "Weight: {weight} kg\n\nStep 2: Enter your height (in cm)\n   Example: 180"

HEIGHT_INVALID = "Height must be between 0 and 250 cm. Please try again:"
HEIGHT_CONFIRMATION = "Height: {height} cm\n\nStep 3: Enter your age\n   Example: 25"

AGE_INVALID = "Age must be between 1 and 120 years. Please try again:"
AGE_CONFIRMATION = "Age: {age} years\n\nStep 4: Enter your desired daily activity in minutes\n   Example: 60"

ACTIVITY_INVALID = "Activity minutes must be between 0 and 1440. Please try again:"
ACTIVITY_CONFIRMATION = "Activity: {activity} minutes per day\n\nStep 5: Enter your city"

CITY_INVALID = "City name must be between 2 and 50 characters. Please try again:"
CITY_CONFIRMATION = "City: {city}\n\nStep 6: Enter your daily calorie goal (or use the calculated default value)\n   Example: 2500"

CALORIE_GOAL_INVALID = "Calorie goal must be between 500 and 10000. Please try again:"
CALORIE_GOAL_PROMPT = "Step 6: Enter your daily calorie goal (in kcal)\nCalculated default value: {default_calories} kcal\n\nExample: 2500"

RESTART_MESSAGE = "Starting over!\n\nStep 1: Enter your weight (in kg)\n   Example: 75.5"
BACK_TO_WEIGHT = "Step 1: Enter your weight (in kg)\n   Example: 75.5"
BACK_TO_HEIGHT = "Step 2: Enter your height (in cm)\n   Example: 180"
BACK_TO_AGE = "Step 3: Enter your age\n   Example: 25"
BACK_TO_ACTIVITY = "Step 4: Enter your desired daily activity in minutes\n   Example: 60"
BACK_TO_CITY = "Step 5: Enter your city"

PROFILE_SAVED_SUCCESS = "Profile saved successfully!"
PROFILE_SAVE_ERROR = "Error saving profile. Please try again later."

INVALID_NUMBER = "Please enter a valid number. Try again:"

PROFILE_NOT_FOUND = "Profile not found. Please fill it in using the /set_profile command."

PROGRESS_NOT_FOUND = "Daily progress not found. Please start tracking using the /set_profile command."

LOG_WATER_USAGE = "Usage: /log_water <amount_in_ml>"
LOG_WATER_INVALID = "Please enter a valid positive number for the amount of water in ml."
LOG_WATER_SUCCESS = "{amount} ml of water added to your daily progress."

LOG_FOOD_USAGE = "Usage: /log_food <food_name>"
LOG_FOOD_PROMPT = "Product: {food_name} - {calories_per_100g} kcal per 100 g.\n\nEnter the amount in grams that you ate:"
LOG_FOOD_SUCCESS = "Logged {calories} kcal."
LOG_FOOD_FAILURE = "Failed to log food information. Please try again later."
LOG_FOOD_INVALID = "Please enter a valid positive number for the amount of food in grams."
LOG_FOOD_CANCELLED = "Food logging cancelled."

LOG_WORKOUT_USAGE = "Usage: /log_workout <workout_type> <duration_in_minutes>"
LOG_WORKOUT_SUCCESS = "Logged {burned_calories} kcal burned, {additional_water_goal} ml of water added to your daily goal."
LOG_WORKOUT_FAILURE = "Failed to log workout information. Please try again later."
LOG_WORKOUT_INVALID = "Please enter a valid positive number for the workout duration in minutes."

DEFAULT_CALORIE_NOTICE = "(Calculated default value: {default_calories} kcal)"
USE_DEFAULT_CALORIE_BUTTON = "Use default value"


HELP_MESSAGE = (
    "Available commands:\n\n"
    "/start - Start interacting with the bot\n"
    "/help - Show this help message\n"
    "/set_profile - Set or update your health profile\n"
    "/profile - View your current health profile\n"
    "/log_water <amount_in_ml> - Log water intake\n"
    "/log_food <food_name> - Log food intake\n"
    "/log_workout <workout_type> <duration_in_minutes> - Log a workout\n"
    "/progress - View daily water and calorie progress\n"
    "/weekly_water - View weekly water progress\n"
    "/weekly_calories - View weekly calorie progress\n"
    "/workouts - View available workout types"
)


def get_confirmation_text(weight, height, age, activity, city, calorie_goal):
    return (
        "📋 Please review your profile data:\n\n"
        f"📊 Weight: {weight} kg\n"
        f"📏 Height: {height} cm\n"
        f"🎂 Age: {age} years\n"
        f"⚡ Activity: {activity} minutes per day\n"
        f"🌍 City: {city}\n"
        f"🍔 Calorie goal: {calorie_goal} kcal"
    )


def get_available_workouts_text(workout_types: list[str]) -> str:
    workout_list = "\n".join(f"- {workout[0].upper() + workout[1:]}" for workout in workout_types)
    return (
        "Available workout types:\n"
        f"{workout_list}\n\n"
        "Usage: /log_workout <workout_type> <duration_in_minutes>\n"
        "   Example: /log_workout running 30"
    )


def format_health_profile(profile: HealthProfileDTO) -> str:
    return (
        "📋 Your health profile:\n\n"
        f"📊 Weight: {profile.weight} kg\n"
        f"📏 Height: {profile.height} cm\n"
        f"🎂 Age: {profile.age} years\n"
        f"⚡ Activity: {profile.activity} minutes per day\n"
        f"🌍 City: {profile.city}\n"
        f"🍔 Calorie goal: {profile.calorie_goal} kcal"
    )


def format_daily_progress(progress: DailyProgressDTO) -> str:
    return (
        f"📅 Your daily progress for {date.today()}:\n\n"
        f"💧 Water: {progress.water_consumed}/{progress.water_goal} ml\n"
        f"🍽️ Calories consumed: {progress.calories_consumed}/{progress.calories_goal} kcal\n"
        f"🔥 Calories burned: {progress.calories_burned} kcal"
    )

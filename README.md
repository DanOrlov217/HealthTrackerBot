# HealthTracker

## Project Description

This project implements a Telegram bot that allows users to log their daily water intake, track calories consumed through food, and monitor calories burned through physical activity.

## Database

SQLite is used for data storage. The database contains tables for storing information about users, their health profiles, daily water consumption, and daily calorie stats.

### Data Schema

#### User
Table for storing bot user information.

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Unique identifier (primary key) |
| `telegram_id` | INTEGER | Unique Telegram user identifier |

**Relations:**
- `health_profile` (1:1) - User's health profile
- `daily_water_stats` (1:N) - Daily water consumption stats
- `daily_calories_stats` (1:N) - Daily calorie stats

---

#### HealthProfile
Table for storing user health data and goals. Filled in once via the registration form.

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Unique identifier |
| `user_id` | INTEGER | Foreign key to User (unique) |
| `weight` | FLOAT | Weight in kilograms |
| `height` | FLOAT | Height in centimeters |
| `age` | INTEGER | Age in years |
| `activity` | INTEGER | Desired daily activity in minutes |
| `city` | STRING | City of residence |
| `calorie_goal` | INTEGER | Daily calorie goal in kcal |

---

#### DailyWaterStats
Table for tracking daily water consumption.

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Unique identifier |
| `user_id` | INTEGER | Foreign key to User |
| `day` | DATE | Date |
| `water_goal` | INTEGER | Water goal in milliliters |
| `water_consumed` | INTEGER | Amount of water consumed in milliliters |

**Constraints:**
- Unique pair (user_id, day) — one record per user per day

---

#### DailyCaloriesStats
Table for tracking daily calorie consumption and burning.

| Field | Type | Description |
|-------|------|-------------|
| `id` | INTEGER | Unique identifier |
| `user_id` | INTEGER | Foreign key to User |
| `day` | DATE | Date |
| `calories_goal` | INTEGER | Daily calorie goal in kcal |
| `calories_consumed` | INTEGER | Calories consumed in kcal |
| `calories_burned` | INTEGER | Calories burned through physical activity in kcal |

**Constraints:**
- Unique pair (user_id, day) — one record per user per day

## Third-party APIs

The project uses the following third-party APIs:
1. **FatSecret API for calorie calculation**: Allows users to enter food names and receive calorie and nutritional information. The free tier only supports data in English. API authorization uses a token generated with a secret key that is valid for 24 hours. To avoid frequent token regeneration, it is cached in the application memory (in `data/save.example.json`).
2. **Google Translator**: Implemented via the `googletrans` library, used to translate food names from Non-English languages to English before sending requests to the FatSecret API.
3. **OpenWeatherMap API for weather data**: Used to factor in weather conditions when calculating the recommended daily water intake.

## Service
The service layer handles interactions with the database and third-party APIs. It includes functions for user registration, health profile updates, and adding/retrieving water and calorie statistics.

Workout tracking uses a configuration file with exercises and their calorie burn rate per minute (`exercises.yaml`). Users can only select exercises from this list when logging burned calories.

## Telegram Bot
The Telegram bot is built using the `aiogram` library.
The following main features are implemented:
- User registration (`/start`);
- Setting and updating the health profile (`/set_profile`);
- Logging water intake (`/log_water <amount_in_ml>`);
- Logging food intake (`/log_food <food_name>`);
- Logging calories burned through physical activity (`/log_workout <exercise_name> <duration_in_minutes>`);
- Viewing weekly water and calorie statistics (`/weekly_water`, `/weekly_calories`);
- Tracking progress toward goals (`/progress`);
- Viewing available exercises for calorie tracking (`/workouts`);
- Bot command help (`/help`).

The `/set_profile` and `/log_food` commands are implemented using FSM (finite state machine) for step-by-step data entry with the ability to cancel or go back to the previous step.

A middleware is also implemented to log all incoming messages and user commands to the console for debugging and monitoring.
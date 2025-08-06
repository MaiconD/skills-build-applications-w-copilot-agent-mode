# Dados de teste para o banco de dados octofit_db

test_data = {
    "users": [
        {"email": "user1@example.com", "name": "User One", "age": 25},
        {"email": "user2@example.com", "name": "User Two", "age": 30}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        {"name": "Team Beta", "members": []}
    ],
    "activities": [
        {"activity_id": 1, "name": "Running", "calories_burned": 300},
        {"activity_id": 2, "name": "Cycling", "calories_burned": 250}
    ],
    "leaderboard": [
        {"leaderboard_id": 1, "team": "Team Alpha", "points": 100},
        {"leaderboard_id": 2, "team": "Team Beta", "points": 50}
    ],
    "workouts": [
        {"workout_id": 1, "user": "user1@example.com", "activity": "Running", "duration": 30},
        {"workout_id": 2, "user": "user2@example.com", "activity": "Cycling", "duration": 45}
    ]
}

class GlowApp:
    def __init__(self):
        self.user_data = {}
        self.meal_history = []
        self.meal_schedule = {}
        self.water_intake = 0
        self.goals = {}
        self.recipe_database = {}

    def register_user(self, name, age, weight, height):
        self.user_data = {
            'name': name,
            'age': age,
            'weight': weight,
            'height': height
        }
        print("User registered successfully!")

    def calculate_bmi(self):
        weight = self.user_data.get('weight')
        height = self.user_data.get('height')

        if weight and height:
            bmi = weight / (height ** 2)
            return bmi
        else:
            return None

    def suggest_calorie_intake(self):
        age = self.user_data.get('age')
        weight = self.user_data.get('weight')
        height = self.user_data.get('height')

        if age and weight and height:
            # Use Harris-Benedict equation to     calculate BMR
            bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

            # Apply activity level multiplier to BMR to get calorie intake suggestion
            activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")
            activity_level_multipliers = {
                'sedentary': 1.2,
                'lightly active': 1.375,
                'moderately active': 1.55,
                'very active': 1.725
            }
            if activity_level in activity_level_multipliers:
                calorie_intake = int(bmr * activity_level_multipliers[activity_level])
                return calorie_intake
            else:
                return None
        else:
            return None

    def add_meal(self, meal_name, nutrients):
        meal = {
            'meal_name': meal_name,
            'nutrients': nutrients
        }
        self.meal_history.append(meal)
        print("Meal added successfully!")
    
    def schedule_meal(self, meal_name, time):
        self.meal_schedule[time] = meal_name
        print(f"Meal {meal_name} scheduled for {time}.")

    def analyze_nutrients(self):
        total_nutrients = {}
        for meal in self.meal_history:
            for nutrient, value in meal['nutrients'].items():
                if nutrient in total_nutrients:
                    total_nutrients[nutrient] += value
                else:
                    total_nutrients[nutrient] = value
        return total_nutrients

    def suggest_diet_plan(self, goal):
        if goal == 'weight_loss':
            # Suggest a diet plan for weight loss
            diet_plan = "Low in calories, high in protein, and rich in fruits and vegetables."
        elif goal == 'muscle_gain':
            # Suggest a diet plan for muscle gain
            diet_plan = "High in protein, moderate in carbohydrates, and includes strength training exercises."
        else:
            # Suggest a general balanced diet plan
            diet_plan = "Balanced diet with a mix of carbohydrates, proteins, and healthy fats."
        return diet_plan

    def set_goal(self, goal, target_nutrients):
        self.goals[goal] = target_nutrients
        print(f"Goal set: {goal}")

    def suggest_nutrient_intake(self):
        user_nutrients = self.analyze_nutrients()
        recommended_nutrients = {}
        for nutrient, target in self.goals.items():
            if nutrient in user_nutrients:
                if user_nutrients[nutrient] < target:
                    diff = target - user_nutrients[nutrient]
                    recommended_nutrients[nutrient] = diff
        return recommended_nutrients

    def record_water_intake(self, amount):
        self.water_intake += amount
        print(f"Water intake recorded. Total: {self.water_intake} ml")

    def add_recipe_to_database(self, recipe_name, nutrients):
        self.recipe_database[recipe_name] = nutrients
        print(f"Recipe '{recipe_name}' added to the database.")

    def suggest_recipe(self):
        user_goals = self.goals.keys()
        suggested_recipes = []
        for recipe, nutrients in self.recipe_database.items():
            if all(goal in nutrients for goal in user_goals):
              suggested_recipes.append(recipe)
     

# Example usage
app = GlowApp()
app.register_user('John Doe', 30, 70, 1.75)
bmi = app.calculate_bmi()
print(f"Your BMI is: {bmi}")
calorie_intake = app.suggest_calorie_intake()
print(f"Suggested Calorie Intake: {calorie_intake}")
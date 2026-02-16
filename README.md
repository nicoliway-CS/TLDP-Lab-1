# 🍎 Fruit Info CLI & 🐱 Cat Fact Saver

This repository contains two Python command-line scripts:

1. **Fruit Info CLI App** – fetches nutritional info for a fruit from the Fruityvice Public API.  
2. **Cat Fact Saver** – fetches a random cat fact from the Cat Facts API and saves it to a text file.



---

## 🍎 Fruit Info CLI App (Main Project)

### 📌 API Used
- **Fruityvice Public API**  
- Endpoint format: `https://www.fruityvice.com/api/fruit/{fruit_name}`  
- Returns JSON with nutritional information for the given fruit.

### 🔹 What the Script Does
1. Prompts the user to enter a fruit name.  
2. Sends a request to the Fruityvice API.  
3. Extracts:
   - Fruit name  
   - Botanical family  
   - Calories per 100g  
4. Displays this information in the terminal.

### ▶️ Example

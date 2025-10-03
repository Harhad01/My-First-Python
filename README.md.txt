
## 📁 File Details

### **1. main.py**
- **Role**: System coordinator
- **Responsibilities**:
  - User interface and input handling
  - Orchestrating interactions between all components
  - Main program loop and flow control

### **2. menu.py** 
- **Role**: Product catalog manager
- **Responsibilities**:
  - Store drink recipes and pricing
  - Validate menu item requests
  - Provide drink information to other components

### **3. coffee_maker.py**
- **Role**: Production system
- **Responsibilities**:
  - Manage ingredient inventory (water, milk, coffee)
  - Check resource availability
  - Deduct resources when brewing
  - Provide resource reports

### **4. money_machine.py**
- **Role**: Financial processor  
- **Responsibilities**:
  - Calculate coin values
  - Validate payment amounts
  - Process transactions and provide change
  - Track total profits

## 🚀 How to Run

```bash
# Navigate to project directory
cd coffee-machine-oops

# Run the application
python main.py
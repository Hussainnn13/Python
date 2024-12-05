import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("inspection.csv")

passed = data[data["Inspection passed"] == 1]
failed = data[data["Inspection passed"] == 0]

min_size = min(len(passed), len(failed))

data_balanced = pd.concat([passed.sample(min_size, random_state=42), failed.sample(min_size, random_state=42)])

X = data_balanced.drop("Inspection passed", axis=1)
y = data_balanced["Inspection passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

def predict():
    print("Enter the status for the following conditions:")
    
    roof = int(input("Is the roof good? (1 for Yes, 0 for No): "))
    while roof not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        roof = int(input("Is the roof good? (1 for Yes, 0 for No): "))
    
    plumbing = int(input("Is the plumbing good? (1 for Yes, 0 for No): "))
    while plumbing not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        plumbing = int(input("Is the plumbing good? (1 for Yes, 0 for No): "))
    
    electrical = int(input("Is the electrical system good? (1 for Yes, 0 for No): "))
    while electrical not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        electrical = int(input("Is the electrical system good? (1 for Yes, 0 for No): "))
    
    windows = int(input("Are the windows in good condition? (1 for Yes, 0 for No): "))
    while windows not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        windows = int(input("Are the windows in good condition? (1 for Yes, 0 for No): "))
    
    alarm = int(input("Is the alarm system functional? (1 for Yes, 0 for No): "))
    while alarm not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        alarm = int(input("Is the alarm system functional? (1 for Yes, 0 for No): "))
    
    doors = int(input("Are the doors in good condition? (1 for Yes, 0 for No): "))
    while doors not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        doors = int(input("Are the doors in good condition? (1 for Yes, 0 for No): "))
    
    flooring = int(input("Is the flooring in good condition? (1 for Yes, 0 for No): "))
    while flooring not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        flooring = int(input("Is the flooring in good condition? (1 for Yes, 0 for No): "))
    
    foundation = int(input("Is the foundation in good condition? (1 for Yes, 0 for No): "))
    while foundation not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        foundation = int(input("Is the foundation in good condition? (1 for Yes, 0 for No): "))
    
    heating_cooling = int(input("Is the heating/cooling system functional? (1 for Yes, 0 for No): "))
    while heating_cooling not in [0, 1]:
        print("Invalid input. Please enter 1 for Yes or 0 for No.")
        heating_cooling = int(input("Is the heating/cooling system functional? (1 for Yes, 0 for No): "))
    
    input_data = pd.DataFrame([[roof, plumbing, electrical, windows, alarm, doors, flooring, foundation, heating_cooling]],
                              columns=X.columns)
    
    prediction = model.predict(input_data)
    
    if prediction == 1:
        print("The inspection passed! All conditions are met!")
    else:
        print("The inspection failed. Here are the reasons:")
        if roof == 0:
            print("- Roof is not in good condition.")
        if plumbing == 0:
            print("- Plumbing is not in good condition.")
        if electrical == 0:
            print("- Electrical system is not in good condition.")
        if windows == 0:
            print("- Windows are not in good condition.")
        if alarm == 0:
            print("- Alarm system is not functional.")
        if doors == 0:
            print("- Doors are not in good condition.")
        if flooring == 0:
            print("- Flooring is not in good condition.")
        if foundation == 0:
            print("- Foundation is not in good condition.")
        if heating_cooling == 0:
            print("- Heating/cooling system is not functional.")

predict()

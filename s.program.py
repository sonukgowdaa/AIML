def find_s(training_data):
    """
    Find-S Algorithm:
    Finds the most specific hypothesis that is consistent
    with all positive training examples.
    """

    # Initialize hypothesis as None
    hypothesis = None

    # Find the first positive example
    for row in training_data:
        if row[-1] == "Yes":
            hypothesis = row[:-1].copy()
            break

    # If there are no positive examples
    if hypothesis is None:
        return "No positive instances found."

    # Generalize the hypothesis using other positive examples
    for row in training_data:
        if row[-1] == "Yes":
            for i in range(len(hypothesis)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = "?"

    return hypothesis


# Main Program
if __name__ == "__main__":

    # Dataset:
    # Sky, Temperature, Humidity, Wind, Water, Forecast, EnjoySport

    dataset = [
        ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
        ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
        ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
        ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
    ]

    # Apply Find-S algorithm
    most_specific_hypothesis = find_s(dataset)

    # Display result
    print("Training Data:")
    for row in dataset:
        print(row)

    print("\nMost Specific Hypothesis:")
    print(most_specific_hypothesis)
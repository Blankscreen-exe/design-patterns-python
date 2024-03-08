**Scenario:**

You're building a delivery management system for a restaurant chain. The system needs to create different delivery objects based on the order size and distance. Here are the types of deliveries:

- **Standard Delivery:** For small orders within a 5km radius, handled by regular delivery personnel on bikes.
- **Express Delivery:** For medium-sized orders or those within a 10km radius, requiring faster scooters.
- **Premium Delivery:** For large orders or those exceeding 10km, needing dedicated vans with drivers.

**Benefits of Using Factory Pattern:**

- **Flexibility:** Easily add new delivery types without modifying existing code.
- **Decoupling:** Client code doesn't need to know specific delivery class implementations.
- **Maintainability:** Code is more organized and easier to modify.

**Explanation:**

1. **Abstract Base Class (`Delivery`)**: Defines the interface for all delivery types with an abstract `deliver` method.
2. **Concrete Delivery Classes (`StandardDelivery`, `ExpressDelivery`, `PremiumDelivery`)**: Implement the `Delivery` interface, providing specific delivery methods.
3. **Delivery Factory Class (`DeliveryFactory`)**: Contains a static `create_delivery` method that takes order size and distance as inputs. Based on these criteria, it returns the appropriate concrete delivery object.

**Usage:**

1. The `main` function prompts the user for order size and distance.
2. It calls `DeliveryFactory.create_delivery` to get the appropriate delivery object.
3. The object's `deliver` method is called to perform the delivery action (printing a message in this example).

**Advantages:**

- The client code interacts only with the `Delivery` interface, making it easier to add new delivery types in the future without modifying existing code.
- The factory encapsulates the logic for creating different delivery objects, promoting better organization and maintainability.

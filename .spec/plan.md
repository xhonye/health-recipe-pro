# Implementation Plan: Advanced Health Recipe Expert

This plan outlines the development of a single-page web application for generating health recipes and managing food data, based on the requirements in `.spec/spec.md`.

## 1. File Structure

Due to the single-file requirement (`index.html`), the application will be structured as follows within the directory:

- `index.html`: The only source file.
    - **`<head>`**: Contains `<style>` block for CSS (Reset, Layout, Components).
    - **`<body>`**:
        - **Header**: Title and "Generate/Refresh" button.
        - **Main Display Area**: Container for the generated recipe cards.
        - **Floating Action Button (FAB)**: Bottom-right gear icon to open the Data Management Panel.
        - **Modal/Overlay**: Hidden by default. Contains the "Data Management" table and "Add New Item" form.
    - **`<script>`**: Embedded at the end of `<body>`.
        - **Constants**: `seedData` (80 items).
        - **State Management**: `localStorage` wrapper functions.
        - **Core Logic**: Recipe generator algorithm.
        - **UI Rendering**: Functions to create DOM elements for cards and table rows.
        - **Event Listeners**: Button clicks, form submissions.

## 2. Key Function Logic

### Data Persistence (`initStorage`)
- **On Load**: Check `localStorage.getItem('foodDatabase')`.
- **If Empty**:
    - Initialize `foodDatabase` with a hardcoded `seedData` array containing 80 items (categorized: Protein, Carb, Vegetable, Fat).
    - Save to `localStorage`.
- **If Exists**: Load data from `localStorage`.

### Recipe Generation (`generateRecipe`)
- **Goal**: Create a meal plan with:
    - 3 Proteins
    - 2 Carbs
    - 3 Vegetables
    - 2 Fats
- **Algorithm**:
    1.  Retrieve current data from `localStorage`.
    2.  Filter data into arrays by `category`.
    3.  Helper function `getRandomUnique(array, count)`:
        -   Shuffle array or pick random indices.
        -   Ensure no duplicates within the selection.
    4.  Combine selections into a single result list.
    5.  Pass result to `renderCards(items)`.

### Data Management
- **View**: Render table of all items in a Modal.
    -   Columns: Name, Category, Nutrient, Amount, NRV, Actions (Delete).
- **Add**: Form with fields (`name`, `category`, `nutrient`, `amount`, `unit`, `nrv`).
    -   **Validation**: All fields required. `amount` and `nrv` must be numbers.
    -   **Save**: Push to `foodDatabase` array -> `localStorage.setItem` -> Refresh UI and Table.

## 3. Implementation Steps

### Phase 1: Skeleton & Styling
1.  **HTML Structure**: Create semantic HTML5 layout with placeholders.
2.  **CSS Styling**:
    -   Use a modern, "premium" color palette (e.g., deep greens, soft creams, vibrant accents).
    -   Glassmorphism for the cards and modal.
    -   Responsive grid for recipe display (mobile-first).

### Phase 2: Data Layer
3.  **Seed Data Creation**: Generate the JSON array of 80 food items (20 Protein, 20 Carb, 20 Vegetable, 20 Fat) with realistic Chinese data.
4.  **Storage Logic**: Implement `loadData`, `saveData`, and `initializeData` functions.

### Phase 3: Core Logic (Generator)
5.  **Generator Function**: Implement the randomization logic with specific counts (3P, 2C, 3V, 2F).
6.  **Card Rendering**: Function to generate HTML for recipe cards dynamically, displaying Name, Nutrient, and NRV.

### Phase 4: Data Management UI
7.  **Management Panel**: Implement the modal open/close logic.
8.  **Form & Table**: Build the table rendering and the "Add Item" form handling.
9.  **Validation**: Ensure inputs are valid before saving.

### Phase 5: Verification
10. **Testing**:
    -   Verify initial load populates 80 items in `localStorage`.
    -   Verify "Generate" button creates valid sets of 10 items (3+2+3+2).
    -   Verify adding a custom item works and appears in future generations.

-- USERS
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE,
    nome TEXT
);

-- CATEGORIES
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE
);

-- EXPENSES
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    category_id INTEGER,
    valor REAL,
    data DATE,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

-- BUDGET
CREATE TABLE budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    limite REAL
);
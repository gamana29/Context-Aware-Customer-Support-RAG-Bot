import sqlite3

DATABASE_NAME = "users.db"

try:
    # Connect to SQLite database
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        membership_tier TEXT NOT NULL
    )
    """)

    # Sample users
    users = [
        (101, "Riya Sharma", "Gold"),
        (102, "Aman Verma", "Silver"),
        (103, "Neha Iyer", "Platinum"),
        (104, "CH Gamana", "Platinum"),
        (105, "B Gayathri", "Gold"),
        (106, "M Bangaruvalli", "Silver"),
        (107, "K Meenakshi", "Gold"),
        (108, "R Harshitha Reddy", "Silver"),
        (109, "K Architha", "Gold"),
        (110, "T Varshitha", "Silver"),
        (111, "K Sadhana", "Gold"),
        (112, "Tulja Manasvi", "Platinum"),
        (113, "Leela Krishna", "Gold"),
        (114, "Roshini", "Silver"),
        (115, "Jyotirmai", "Gold"),
        (116, "Spandana", "Silver"),
        (117, "Chandana", "Gold"),
        (118, "Siri Vennala", "Platinum"),
        (119, "Bhargavi", "Silver"),
        (120, "Rakshitha", "Gold"),
        (121, "Mahitha", "Silver")
    ]

    # Insert or update user records
    cursor.executemany("""
    INSERT OR REPLACE INTO users (user_id, name, membership_tier)
    VALUES (?, ?, ?)
    """, users)

    conn.commit()

    # Display all users
    cursor.execute("SELECT * FROM users")

    print("\n========== USERS DATABASE ==========\n")

    for user in cursor.fetchall():
        print(
            f"User ID: {user[0]:<3} | "
            f"Name: {user[1]:<20} | "
            f"Membership: {user[2]}"
        )

    print("\n====================================")
    print("Database created and seeded successfully!")

except sqlite3.Error as e:
    print(f"Database Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
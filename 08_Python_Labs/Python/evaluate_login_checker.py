def evaluate_login(username, login_time_ok, approved_users):
    if username in approved_users and login_time_ok:
        return "✅ Login approved: Access granted during organization hours."
    elif username not in approved_users:
        return "❌ Login denied: Username not on approved list."
    elif not login_time_ok:
        return "⚠️ Login denied: Attempt outside of organization hours."

# Sample data for testing
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Test cases
print(evaluate_login("lwilliams", True, approved_list))
print(evaluate_login("sgilmore", False, approved_list))
print(evaluate_login("tshah", True, approved_list))

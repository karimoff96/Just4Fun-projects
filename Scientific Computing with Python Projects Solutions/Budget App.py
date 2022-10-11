class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def deposit(self, amount, description=''):
        self.update_balance(amount)
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.update_balance(-amount)
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        stars_count = (30 - len(self.name)) // 2
        text = f"{'*' * stars_count}{self.name}{'*' * stars_count}\n"
        for item in self.ledger:
            amount = str("%.2f" % item.get('amount'))
            desc = item.get('description')
            chars_count = len(amount) + len(desc)
            if chars_count > 30:
                text += f"{desc[:23]} {amount}\n"
            else:
                text += f"{desc}{' ' * (30 - chars_count)}{amount}\n"
        text += f"Total: {self.get_balance()}"
        return text


def create_spend_chart(categories):
    statistics = []
    total_spent = 0

    for category in categories:
        total_wastes = 0
        for waste in category.ledger:
            amount = waste.get('amount')
            if amount < 0:
                total_wastes -= amount
        total_spent += total_wastes
        statistics.append({'category': category.name, 'spent': total_wastes})

    for item in statistics:
        persentage = item.get('spent') / total_spent * 100
        persentage -= persentage % 10
        item['persentage'] = round(persentage)

    text = "Percentage spent by category\n"

    for per in range(100, -10, -10):
        if per == 100:
            text += f"{per}|"
        elif per == 0:
            text += f"  {per}|"
        else:
            text += f" {per}|"

        for stat in statistics:
            if stat.get('persentage') >= per:
                text += " o "
            else:
                text += "   "
        text += " \n"

    text += f"    {'-' * len(categories) * 3}-\n"

    names = [item.name for item in categories]
    max_len = max([len(name) for name in names])

    for i in range(max_len):
        text += "    "
        for name in names:
            if len(name) - 1 >= i:
                text += f" {name[i]} "
            else:
                text += "   "
        if i + 1 == max_len:
          text += " "
        else:
          text += " \n"
    return text

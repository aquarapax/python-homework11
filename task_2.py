class CreditCard:
    def __init__(self, card_number, card_holder, card_date, card_cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.card_date = card_date
        self.card_svv = card_cvv
        
    def get_card_number(self):
        return self.card_number

    def get_card_holder(self):
        return self.card_holder

    def get_expiry_date(self):
        return self.card_date

    def get_cvv(self):
        return self.card_svv

    def charge(self, amount: float):
        if amount > 1000.00:  # Лимит платежа 1000
            raise ValueError("Сумма превышает лимит")
        return f"Сумма {amount} успешно списана."
        

class PaymentForm:
    def __init__(self, credit_card: CreditCard):
        self.credit_card = credit_card

    def pay(self, amount: float):
        return self.credit_card.charge(amount)

if __name__ == '__main__':
    card = CreditCard('1111-1111-1111-1111-1111','IVAN PETROV', '12/25','123')
    print(f'Номер карты: {card.get_card_number()}')
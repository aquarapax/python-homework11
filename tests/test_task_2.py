import unittest
from unittest.mock import MagicMock
from task_2 import CreditCard, PaymentForm

class TestPaymentForm(unittest.TestCase):
    def setUp(self):
        # Создание мок-объекта для CreditCard
        self.mock_card = MagicMock(spec=CreditCard)
        # Создаем объект PaymentForm, передавая мок-объект
        self.payment_form = PaymentForm(self.mock_card)

    def tearDown(self):
        # Очистка после каждого теста (если нужно)
        self.mock_card.reset_mock()

    def test_successful_payment(self):
        # Установим поведение мок-объекта
        self.mock_card.charge.return_value = "Сумма 50.0 успешно списана."
        
        # Вызов метода pay()
        result = self.payment_form.pay(50.00)
        
        # Убедимся, что метод charge был вызван с правильным аргументом
        self.mock_card.charge.assert_called_once_with(50.00)
        self.assertEqual(result, "Сумма 50.0 успешно списана.")

    def test_payment_exceeds_limit(self):
        # Установим поведение в случае превышения лимита
        self.mock_card.charge.side_effect = ValueError("Сумма превышает лимит")
        
        # Проверка на выброс исключения
        with self.assertRaises(ValueError) as context:
            self.payment_form.pay(1500.00)
        
        self.assertEqual(str(context.exception), "Сумма превышает лимит")
        self.mock_card.charge.assert_called_once_with(1500.00)

    def test_credit_card_initialization_valid(self):
        # Тест на корректную инициализацию CreditCard
        card = CreditCard('1234-5678-9012-3456', 'IVAN PETROV', '12/25', '123')
        self.assertEqual(card.get_card_number(), '1234-5678-9012-3456')
        self.assertEqual(card.get_card_holder(), 'IVAN PETROV')
        self.assertEqual(card.get_expiry_date(), '12/25')
        self.assertEqual(card.get_cvv(), '123')

    def test_credit_card_initialization_invalid_number(self):
        # Тест на некорректный номер карты
        with self.assertRaises(ValueError) as context:
            CreditCard('1234-5678-9012-345', 'IVAN PETROV', '12/25', '123')
        
        self.assertEqual(str(context.exception), "Номер карты должен состоять из 16 чисел в формате 'XXXX-XXXX-XXXX-XXXX'")

    def test_credit_card_initialization_invalid_date(self):
        # Тест на некорректный срок действия карты
        with self.assertRaises(ValueError) as context:
            CreditCard('1234-5678-9012-3456', 'IVAN PETROV', '1225', '123')
        
        self.assertEqual(str(context.exception), "Срок действия карты должен быть в формате 'MM/YY'")

    def test_credit_card_initialization_invalid_cvv(self):
        # Тест на некорректный CVC
        with self.assertRaises(ValueError) as context:
            CreditCard('1234-5678-9012-3456', 'IVAN PETROV', '12/25', '12')
        
        self.assertEqual(str(context.exception), "CVV должен состоять из трех цифр")


if __name__ == '__main__':
    unittest.main()
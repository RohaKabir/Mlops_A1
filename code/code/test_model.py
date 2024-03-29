
# test_model.py

import unittest
from model import load_iris_data, train_model, evaluate_model


class TestModel(unittest.TestCase):

    def setUp(self):
        self.X_train, self.X_test, self.y_train, self.y_test = load_iris_data()

    def test_data_loading(self):
        self.assertIsNotNone(self.X_train)
        self.assertIsNotNone(self.X_test)
        self.assertIsNotNone(self.y_train)
        self.assertIsNotNone(self.y_test)

    def test_model_training(self):
        model = train_model(self.X_train, self.y_train)
        self.assertIsNotNone(model)

    def test_model_evaluation(self):
        model = train_model(self.X_train, self.y_train)
        accuracy = evaluate_model(model, self.X_test, self.y_test)
        self.assertGreaterEqual(
            accuracy, 0.0
        )  # Assuming accuracy is always non-negative


if __name__ == '__main__':
    unittest.main()

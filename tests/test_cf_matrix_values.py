import unittest
from src.modeling.model import clfModel
import logging
logging.basicConfig(level=logging.DEBUG)

class TestConfusionMatrixValues(unittest.TestCase):
  def test_split(self):
    cm, acc = clfModel()
    spam = [44, 0]
    ham = [1, 43]
    
    logging.info("MATRIX VALUES TEST START")
    logging.info(f"Actual {cm[0].tolist()} expected: {spam}")
    self.assertEqual(cm[0].tolist(), spam)
    
    logging.info(f"Given value: {cm[1].tolist()} expected: {ham}")
    self.assertEqual(cm[1].tolist(), ham)
    
    logging.info(f"Actual: {acc} expected {acc} > {96}")
    self.assertGreater(acc, 96)
    
if __name__ == '__main__':
  unittest.main()
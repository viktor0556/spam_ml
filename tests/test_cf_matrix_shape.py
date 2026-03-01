import unittest
from src.modeling.model import clfModel
import logging
logging.basicConfig(level=logging.DEBUG)

class TestConfusionMatrixShape(unittest.TestCase):
  def test_split(self):
    cm, val = clfModel()
    
    logging.info(f"Actual: {cm.shape} expected: {(2, 2)}")
    self.assertEqual(cm.shape, (2, 2))
      
if __name__ == '__main__':
  unittest.main()
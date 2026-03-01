import unittest
from collections import Counter
from src.main import main
import logging
logging.basicConfig(level=logging.DEBUG)

class TestCounterDistribution(unittest.TestCase):
  def test_split(self):
    X, y = main(path="./messages_data/messages.csv")
    CounterY = Counter(y)
    
    logging.info("COUNTER DISTRIBUTION TEST START")
    # kulcsok
    listedKeys = list(CounterY.keys())
    keys = ['ham', 'spam']
    logging.info(f"Actual: {keys} expected: {listedKeys}")
    self.assertNotIn(listedKeys, keys)
  
  
    # értékek
    labelValues = sum(CounterY.values())
    logging.info(f"Actual: {labelValues} expected: {292}")
    self.assertEqual(labelValues, 292)

      
    # negatív szám
    labelValues = sum(CounterY.values())
    logging.info(f"Actual: {labelValues} expected: {292}")
    positiveNumb = labelValues is not None and labelValues >= 0 
    self.assertTrue(positiveNumb)
    
if __name__ == '__main__':
  unittest.main()
  
  
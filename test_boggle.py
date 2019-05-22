import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """Our test suite for boggle solver"""
    
    def test_can_create_an_empty_grid(self):
        """Test to see if we can create an empty grid"""
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid),0)
        
        
    def test_grid_size_is_width_times_height(self):
        """Test if the local size of the grid is equal to width"""
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordonates(self):
        """
        Test to ensure that all of the coordonates 
           inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        """assertIn check if is in grid"""
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        """check if if not in"""
        self.assertNotIn((2, 2), grid)
        
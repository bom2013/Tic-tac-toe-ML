import unittest
import perf_sys

class TestPerfSys(unittest.TestCase):
    blank_b = [[0,0,0],[0,0,0],[0,0,0]]


    def test_reverse_board(self):
        self.assertEqual(perf_sys.reverse_board(self.blank_b), self.blank_b)
        t1 = [[1,0,1],[2,1,0],[2,1,1]]
        t1_r = [[2,0,2],[1,2,0],[1,2,2]]
        self.assertEqual(perf_sys.reverse_board(t1), t1_r)


    def test_p_tag(self):
        self.assertEqual(perf_sys.p_tag(1), 2)
        self.assertEqual(perf_sys.p_tag(2), 1)
        self.assertEqual(perf_sys.p_tag(0), 0)


    def test_get_leg_moves(self):
        self.assertEqual(perf_sys.get_leg_moves(self.blank_b, 1), [[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]]])
        self.assertEqual(perf_sys.get_leg_moves(self.blank_b, 2), [[[2, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 2, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 2], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [2, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 2, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 2], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [2, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 2, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 2]]])
        t1 = [[1,0,0],[0,2,1],[0,0,0]]
        self.assertEqual(perf_sys.get_leg_moves(t1,2), [[[1,2,0],[0,2,1],[0,0,0]], [[1,0,2],[0,2,1],[0,0,0]],[[1,0,0],[2,2,1],[0,0,0]],[[1,0,0],[0,2,1],[2,0,0]],[[1,0,0],[0,2,1],[0,2,0]],[[1,0,0],[0,2,1],[0,0,2]]])
        t2 = [[1,2,1],[2,2,1],[1,2,1]]
        self.assertEqual(perf_sys.get_leg_moves(t2,2),[])


    def test_is_end_of_game(self):
        self.assertEqual(perf_sys.is_end_of_game(self.blank_b),0)
        t1 = [[1,0,0],[0,2,1],[0,0,0]]
        self.assertEqual(perf_sys.is_end_of_game(t1),0)

        t2 = [[1,1,2],[2,2,1],[1,2,1]]
        self.assertEqual(perf_sys.is_end_of_game(t2),3)
        t3 = [[1,1,1],[2,1,2],[2,1,2]]
        self.assertEqual(perf_sys.is_end_of_game(t3),1)
        
        ud1_1 = [[1,2,0],[1,2,0],[1,0,0]]
        ud2_1 = [[0,1,2],[0,1,2],[0,1,0]]
        ud3_1 = [[2,0,1],[2,0,1],[0,0,1]]
        self.assertEqual(perf_sys.is_end_of_game(ud1_1),1)
        self.assertEqual(perf_sys.is_end_of_game(ud2_1),1)
        self.assertEqual(perf_sys.is_end_of_game(ud3_1),1)

        rl1_1 = [[1,1,1],[2,2,0],[0,0,0]]
        rl2_1 = [[2,2,0],[1,1,1],[0,0,0]]
        rl3_1 = [[2,2,0],[0,0,0],[1,1,1]]
        self.assertEqual(perf_sys.is_end_of_game(rl1_1),1)
        self.assertEqual(perf_sys.is_end_of_game(rl2_1),1)
        self.assertEqual(perf_sys.is_end_of_game(rl3_1),1)


        ud1_2 = perf_sys.reverse_board(ud1_1)
        ud2_2 = perf_sys.reverse_board(ud2_1)
        ud3_2 = perf_sys.reverse_board(ud3_1)
        self.assertEqual(perf_sys.is_end_of_game(ud1_2),2)
        self.assertEqual(perf_sys.is_end_of_game(ud2_2),2)
        self.assertEqual(perf_sys.is_end_of_game(ud3_2),2)

        rl1_2 = perf_sys.reverse_board(rl1_1)
        rl2_2 = perf_sys.reverse_board(rl1_1)
        rl3_2 = perf_sys.reverse_board(rl1_1)
        self.assertEqual(perf_sys.is_end_of_game(rl1_1),1)
        self.assertEqual(perf_sys.is_end_of_game(rl2_1),1)
        self.assertEqual(perf_sys.is_end_of_game(rl3_1),1)

        xlr_1 = [[1,2,0],[2,1,0],[0,0,1]]
        xrl_1 = [[0,2,1],[2,1,0],[1,0,0]]
        self.assertEqual(perf_sys.is_end_of_game(xlr_1),1)
        self.assertEqual(perf_sys.is_end_of_game(xrl_1),1)

        xlr_2 = perf_sys.reverse_board(xlr_1)
        xrl_2 = perf_sys.reverse_board(xrl_1)
        self.assertEqual(perf_sys.is_end_of_game(xlr_2),2)
        self.assertEqual(perf_sys.is_end_of_game(xrl_2),2)

if __name__ == '__main__':
    unittest.main()

import unittest
from wrap import wrap_lines

class TestWrap(unittest.TestCase):
    def test_text_is_not_a_string(self):
        text = 555555
        number = 40
        justify = False
        result = wrap_lines(text, number, justify)

        self.assertEqual(result, "Value error!")

    def test_number_is_not_a_string(self):
        text = "example text"
        number = "number"
        justify = False
        result = wrap_lines(text, number, justify)

        self.assertEqual(result, "Value error!")

    def test_number_is_not_negative(self):
        text = "example text"
        number = -5
        justify = False
        result = wrap_lines(text, number, justify)

        self.assertEqual(result, "Value error!")

    def test_text_is_not_empty(self):
        text = " "
        number = 40
        justify = False
        result = wrap_lines(text, number, justify)

        self.assertEqual(result, "Value error!")

    def test_number_is_not_empty(self):
        text = "example text"
        number = " "
        justify = False
        result = wrap_lines(text, number, justify)

        self.assertEqual(result, "Value error!")

    def test_lines_doesnt_have_more_characters_than_the_input_number(self):
        text = """
            Praesent rhoncus est et porta convallis. Integer sed massa eu felis commodo euismod in vel est. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

            Quisque iaculis enim in nisi finibus, vitae fermentum justo aliquam. Praesent sodales venenatis ornare. Fusce a dui et nulla aliquet feugiat a vel urna. Cras feugiat non enim id euismod. Curabitur a ornare turpis.
        """
        number = 40
        justify = False
        result = wrap_lines(text, number, justify)

        paragraphs = result.split('\n')
        for p in paragraphs:
            self.assertTrue(len(p) <= number)

    def test_have_the_same_number_of_characters_of_input_number(self):
        text = """
            Praesent rhoncus est et porta convallis. Integer sed massa eu felis commodo euismod in vel est. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

            Quisque iaculis enim in nisi finibus, vitae fermentum justo aliquam. Praesent sodales venenatis ornare. Fusce a dui et nulla aliquet feugiat a vel urna. Cras feugiat non enim id euismod. Curabitur a ornare turpis.
        """
        number = 40
        justify = True
        result = wrap_lines(text, number, justify)

        paragraphs = result.split('\n')
        paragraphs = paragraphs[:-1] # O método split da linha anterior gera uma linha a mais vazia
        for p in paragraphs:
            self.assertTrue(len(p) == number)


if __name__ == '__main__':
    unittest.main()